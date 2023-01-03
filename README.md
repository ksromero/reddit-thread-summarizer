
# Reddit Thread Summarizer

A Reddit thread summarizer is a tool that generates a summary of the main points or 
themes discussed in a Reddit thread (a discussion forum on the website Reddit). 
The summarizer may also provide information about the overall sentiment expressed in 
the thread **(including the users comment)**. 
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

To get the **CLIENT_ID** and **CLIENT_SECRET** from reddit follow this [easy guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)

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
    "overall_summary": "This list of hip hop beats includes classic
        tracks such as \"Shook Ones, Pt II\" by Mobb Deep, \"Ante Up\" by MOP,
        and \"Wicked\" by Ice Cube, as well as more modern tracks like
        \"My Choppa Hate Niggas\" by 21 Savage and \"Neon Guts\" by Lil Uzi Vert.
        Other notable songs include \"Deep Cover\" by Dr. Dre, \"X Is Coming\" by DMX,
        \"Beware\" by Big Pun, \"Lose Yourself\" by Eminem, and \"Victory\" by Puff Daddy.",
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
        "overall_summary": "Reddit users have mixed opinions on the Netflix show 
            Emily in Paris. Some find it entertaining and fashionable, while others find 
            it too cliche and unrealistic. Despite the criticism, the show has been renewed 
            for multiple seasons and is still popular with viewers. It is a light, 
            shallow show with extravagant outfits and has been criticized for its 
            unrealistic portrayal of relationships and lack of diversity.",
        "title": "[DISCUSSION] Emily in Paris is SO bad",
        "upvotes": 1141
    },
    {
        "content_body": "Like Fight Club, The Illusionist, Midsommar… something that takes you aback with brilliance.\n\nEdit: thank you all so much, so many suggestions I haven’t seen. It’ll get me through being stuck at home. Y’all rock my fellow movie people.\n\nAlso sorry I can’t respond, I didn’t expect this many! I’m writing down each one I haven’t seen there are a lot!",
        "created_at": "Thu, 29 Dec 2022 23:29:29 GMT",
        "num_of_comments": 520,
        "overall_summary": "Reddit users have recommended a variety of movies with 
            unexpected twists and turns, ranging from classic thrillers to horror films 
            and comedies. These movies include The Sixth Sense, The Prestige,
            Donnie Darko, Mr. Robot, Memento, The Changeling, Uncut Gems, The Departed, 
            The Crying Game, Oculus, Fracture, The Village, Saint Maud, Shutter Island, 
            The Mist, Prisoners, Layer Cake, Identity, Cabin in the Woods, Behind Her Eyes, 
            Se7en, Get Out, Saw, Perfect Blue, All About Lily Chou Chou, Bodies Bodies Bodies,
            Primal Fear, Arrival, Where the Crawfish Sing, Awake, The Machinist, 
            American History X, Pan's Labyrinth, Mystic River, Side Effects, The Orphanage,
            Colossus: The Forbin Project, Planet of the Apes, Soylent Green, American Psycho,
            Bandersnatch, Vanilla Sky, Requiem of a Dream, Fat Girl, The Vanishing,
            The Art of Self Defense, 400 Days, Dark City, The Usual Suspects, Archive,
            Oldboy, A Cure for Wellness, Once Upon a Time in Hollywood, Snowpiercer,
            The Barbarian, The Signal, Unbreakable, Split, Time Crimes, Predestination,
            Primer, Red Notice, Laura, The Power of the Dog, Lucky Number Sleven,
            Possessor, Orphan, Inception, Dodgeball, Remember Me, Samaritan 2022, 
            The Departed, Black Butterfly, The Empty Man, The Mist Triangle, 
            The Rental, Clueless, Glass Onion, Dead Again, Wild Things, The Boy, 
            Housebound, Seven Psychopaths, The Grey, Come True, Enemy, Citizen Kane, 
            Barbarians, From Dusk Till Dawn, Inside Number 9, The Girl with All the Gifts,
            Extinction, The Guest, You're Next, Life, 10 Cloverfield Lane,
            I'm Thinking of Ending Things, and Sorry to Bother You.",
        "title": "[Request] Movies that have wtf ending. Something you wouldn’t expect but changes the whole movie",
        "upvotes": 652
    },
    {
        "content_body": "",
        "created_at": "Tue, 03 Jan 2023 01:56:38 GMT",
        "num_of_comments": 260,
        "overall_summary": "Reddit users are frustrated with Netflix's decision to
            cancel a series before it had a chance to gain momentum, leaving viewers
            with an unfinished story. They feel that Netflix does not understand the
            streaming audience or their platform, and that other streaming services
            have better content. People are disappointed and questioning why Netflix
            would cancel a show that was popular and had potential for future seasons.",
        "title": "[Discussion] 1899 got cancelled for season 2🤧...It just hurta to see like one of the best show I've seen on Netflix is not getting 2nd season🤧",
        "upvotes": 495
    }
]
```

## Limitations

- OpenAI API will throw an error **"a server overload error"** if you make many request
- Request can take a minute depending on the number of the comments on thread
