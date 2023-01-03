import praw
import openai
from openai.error import RateLimitError
from os import getenv
from dotenv import load_dotenv
import concurrent.futures
import backoff
import queue
import datetime
from threading import BoundedSemaphore
from flask import Flask, request, jsonify

app = Flask(__name__)
load_dotenv()
openai.api_key = getenv('API_KEY')
sem = BoundedSemaphore(4) 

reddit = praw.Reddit(
    client_id=getenv('CLIENT_ID'),
    client_secret=getenv('CLIENT_SECRET'),
    user_agent="Comment Extraction (by u/USERNAME)"
)

def check_text_moderation(input):
    response = openai.Moderation.create(input=input)

    return response["results"][0]["flagged"]

def openai_create(prompt):
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0, max_tokens=500)

    return response["choices"][0]["text"]

def get_comments_summary_chunk(chunk, summary_queue):
    prompt = f"""Summarize this in English from a general perspective:\n\n"{" ".join(chunk)}"""
    response = openai_create(prompt)
    summary_queue.put(response)

def get_comments_summary(comments):
    summary = ""
    chunk_size = 38
    futures = []
    summary_queue = queue.Queue()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(0, len(comments), chunk_size):
            with sem:
                chunk = comments[i:i+chunk_size]
                future = executor.submit(get_comments_summary_chunk, chunk, summary_queue)
                future.chunk = chunk
                futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            future.result()
    while not summary_queue.empty():
        summary += summary_queue.get()

    summary = summary.strip()

    return summary

def get_comments(thread):
    comments = []
    thread.comments.replace_more(limit=None)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        comment_futures = []
        for comment in thread.comments:
            future = executor.submit(check_text_moderation, comment.body)
            comment_futures.append((comment.body, future))
        for comment_body, future in comment_futures:
            result = future.result()
            if not result:
                comments.append(comment_body)

    summary = get_comments_summary(comments)
    overall_summary = openai_create(f'"{summary}"\nSummarize the above information, highlighting the most important ideas expressed in the comments of Reddit users:').strip()
 
    return comments, overall_summary

def process_submission(submission):
    top = []
    score = submission.score
    id = submission.id

    if score > 0:
        submission = reddit.submission(id)
        _, overall_summary = get_comments(submission)
        top.append(
            dict(
                title=submission.title,
                content_body=submission.selftext,
                upvotes=score,
                num_of_comments=submission.num_comments,
                created_at=datetime.datetime.fromtimestamp(submission.created_utc, tz=datetime.timezone.utc),
                overall_summary=overall_summary
            )
        )

    return top

@app.route('/subreddit-top3-weekly', methods =['POST'])
@backoff.on_exception(backoff.expo, RateLimitError)
def get_subreddit_top3_thread_this_week():
    data = request.get_json()

    if 'subreddit_name' not in data:
        raise Exception("subreddit_name not existing on request")

    subreddit_name  = data['subreddit_name']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        submissions = reddit.subreddit(subreddit_name).top(time_filter="week", limit=3)
        futures = []
        for submission in submissions:
            future = executor.submit(process_submission, submission)
            futures.append(future)
        top_submissions = []
        for future in concurrent.futures.as_completed(futures):
            top_submissions += future.result()

    top_submissions.sort(key=lambda submission: submission['upvotes'], reverse=True)

    return jsonify(top_submissions)

@app.route('/thread-summary', methods =['POST'])
@backoff.on_exception(backoff.expo, RateLimitError)
def get_subreddit_thread_summary():
    data = request.get_json()

    if 'url' not in data:
        raise Exception("url key not existing on request")

    url  = data['url']
    submission = reddit.submission(url=url)
    result = process_submission(submission)

    return jsonify(result[0])

if __name__ == '__main__':
    app.run()
