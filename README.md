
# Reddit Thread Summarizer

A Reddit thread summarizer is a tool that generates a summary of the main points or 
themes discussed in a Reddit thread (a discussion forum on the website Reddit). 
The summarizer may also provide information about the overall sentiment expressed in 
the thread (including users comment). 
This can be useful for quickly getting a sense of the main points of discussion in a long 
or complex thread, or for identifying trends or common opinions among Reddit users. 






## Tech Stack

**Server:** Python, Flask, OpenAI (text-davinci-003) Completion





## Get Started

**Backend**

**Step 1:** First copy the contents of **.env.example**, paste it into a new **.env** file
| key | Description                |
| :-------- | :------------------------- |
| `CLIENT_ID` | **Required**. To be able to access reddit API |
| `CLIENT_SECRET` | **Required**. To be able to access reddit API |
| `API_KEY` | **Required**. To be able to access OpenAI API |

To get the CLIENT_ID and CLIENT_SECRET from reddit follow this [guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)

**Step 2:** We need to [install pipenv](https://pipenv.pypa.io/en/latest/install/)

```bash
pipenv install
flask --app index run
```

**Step 3:** Finally, access the app on http://127.0.0.1:5000




## Reminder
- Kindly monitor your OpenAI usage to keep track of the costs


## API Reference

#### Summarize a reddit thread

```http
  POST /thread-summary
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. Reddit thread URL |


Reddit URL Example: https://www.reddit.com/r/hiphop101/comments/bjan0i/hardest_beats_of_all_time/

Sample Input:
```
{
    "url": "https://www.reddit.com/r/hiphop101/comments/bjan0i/hardest_beats_of_all_time/"
}
```

Sample Output:
```
{
    "content_body": "I’m talking anything from trap to boom bap and everything in between.\n\nwhat are the beats where you just gotta nod your fucking head?",
    "created_at": "Wed, 01 May 2019 00:03:21 GMT",
    "num_of_comments": 42,
    "overall_summary": "\n\nIn summary, this comment is a celebration of the wide variety 
        of hip-hop music available, from classic hits to lesser-known beats. 
        It highlights some of the most popular and hard-hitting hip-hop songs and 
        artists of the early 2000s, such as Big Pun, Dr. Dre, Mobb Deep, MOP, and 
        Devilish Trio.",
    "title": "Hardest beats of all time?",
    "upvotes": 17
}
```
#### Summarize each of top 3 weekly of subreddit

```http
  POST /subreddit-top3-weekly
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `subreddit_name`      | `string` | **Required**. Subreddit name |

Subreddit name example: **"NetflixBestOf"**

Sample Input:
```
{
    "subreddit_name": "NetflixBestOf"
}
```

Sample Output:
```
[
    {
        "content_body": "Even in the new season Emily continues to be such a cliché of an ignorant US-American. I’m not even French but her entitlement leaves me speechless sometimes. Interrupts a Black DJ to make her play a shitty song by her friend? No biggie. Bringing up her French class after food poisoning a client at work? Sure thing. Using the gay co workers a props? Emily got this!\n\nAnd she Never had a single bureaucracy problem? LOL. I don’t even want to hate watch it.",
        "created_at": "Tue, 27 Dec 2022 20:45:58 GMT",
        "num_of_comments": 258,
        "overall_summary": "\n\nOverall, the comments on Emily in Paris are mixed, with some 
            people enjoying the show for its lightheartedness and escapist nature, 
            while others find it too cliche and unrealistic. There is also criticism of the show's
            lack of realism, with some noting that the characters' fashion choices are unrealistic. 
            Additionally, some people find the show's cultural imperialism and ignorance to be
            problematic. There is also discussion about the DJ's race and the bechdel test, 
            as well as whether race or gender should be relevant to the show. 
            In conclusion, people have different opinions about the show, but it is 
            generally seen as a light and entertaining show.",
        "title": "[DISCUSSION] Emily in Paris is SO bad",
        "upvotes": 1140
    },
    {
        "content_body": "Like Fight Club, The Illusionist, Midsommar… something that takes you aback with brilliance.\n\nEdit: thank you all so much, so many suggestions I haven’t seen. It’ll get me through being stuck at home. Y’all rock my fellow movie people.\n\nAlso sorry I can’t respond, I didn’t expect this many! I’m writing down each one I haven’t seen there are a lot!",
        "created_at": "Thu, 29 Dec 2022 23:29:29 GMT",
        "num_of_comments": 520,
        "overall_summary": "\n\nOverall, the comments suggest that there are a variety of 
            movies with unexpected and mind-bending endings that have been enjoyed by viewers. 
            These movies range from classic thrillers to more recent films, as well as horror films,
            psychological thrillers, and foreign films. People have shared their experiences 
            with the movies, such as having the endings spoiled for them, and shared their 
            opinions on the movies. They have also recommended other movies with twist endings, 
            such as The Merchant and the Alchemist’s Gate.",
        "title": "[Request] Movies that have wtf ending. Something you wouldn’t expect but changes the whole movie",
        "upvotes": 653
    },
    {
        "content_body": "",
        "created_at": "Tue, 03 Jan 2023 01:56:38 GMT",
        "num_of_comments": 204,
        "overall_summary": "\n\nOverall, this conversation reflects the general sentiment 
            that Netflix is canceling good series too quickly, leaving viewers with no ending 
            and no chance to gain momentum. Many viewers are frustrated with Netflix's decisions 
            and are now turning to other streaming services such as HBO Max and Hulu. 
            They are also disappointed that Netflix is focusing on unscripted reality shows and 
            teen dramas, rather than adult content. People are also disappointed that the show 1899 
            was canceled before they had a chance to finish it, as it had a lot of unanswered 
            questions and potential for a second season. Despite this, some viewers have enjoyed
            shows like Dark and Mr Robot, and have expressed their disappointment when they were 
            removed from the platform.",
        "title": "[Discussion] 1899 got cancelled for season 2🤧...It just hurta to see like one of the best show I've seen on Netflix is not getting 2nd season🤧",
        "upvotes": 405
    }
]
```

## Limitations

- OpenAI API will throw an error **"a server overload error"** if you make many request
- Request can take a minute depending on the number of the comments on thread
