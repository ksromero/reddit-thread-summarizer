
# Reddit Thread Summarizer

A Reddit thread summarizer is a tool that generates a summary of the main points or 
themes discussed in a Reddit thread (a discussion forum on the website Reddit). 
The summarizer may also provide information about the overall sentiment expressed in 
the thread (including comments). 
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
[
    {
        "content_body": "I’m talking anything from trap to boom bap and everything in between.\n\nwhat are the beats where you just gotta nod your fucking head?",
        "created_at": "Wed, 01 May 2019 00:03:21 GMT",
        ""num_of_comments"": 42,
        "overall_summary": "\n\nThe overall summary is a celebration of the best hip-hop music 
            from a variety of artists, including Dipset, Philthy Rich, Mozzy, Just Blaze, 
            Twinz, Big Pun, Fat Joe, 2Pac, Kendrick Lamar, Joey Badass, MOP, Nas, Bone Crusher, 
            Stitches, Ludacris, Pharaoh Monch, Lil Wayne, Jay-Z, Diplomats, Camron, $UICIDEBOY$, 
            Pusha T, Kanye West, J. Cole, 21 Savage, Curren$y, DJ Paul, Germ, 
            Lord Infamous, Three 6 Mafia, Tommy Wright III, C Murder, Young Buck, 
            Dead Prez, Ace Hood, Nipsey Hussle, Starlito, Token, Tyler, The Creator,
            Black Rob, The Game, Danny Brown, ODB, Gravediggaz, Mobb Deep, Ski Mask, 
            Playboy Carti, Denzel Curry, Travis Scott, Higher Brothers, Missy Elliott,
            88rising, Kanye/Cudi, Rich Brian, Aminé, Jules Santana, Heatmakerz, Havoc,
            Don Cannon, Manny Fresh, Juvenile, Bink, Dr. Dre, Swizz Beatz, Bangladesh, 
            Buckwild, Royce Da 5’9”, DJ Premier, Shawty Redd, Metro Boomin, Flight Distance, 
            and Diddy. These songs are praised for their hard beats, raw energy, and ability to 
            transport listeners to another plane of existence.",
        "title": "Hardest beats of all time?",
        "upvotes": 17
    }
]
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
        "num_of_comments": 256,
        "overall_summary": "\n\nOverall, Emily in Paris has been met with mixed reviews. Some people enjoy the show for its lightheartedness and escapist nature, while others find it too cliche and unrealistic. The show has been renewed for more seasons, likely due to its popularity, and the creators have taken critiques into consideration. Despite the mixed reviews, the show has a large fanbase and continues to be a guilty pleasure for many. The comments also mention a black DJ, but it is unclear why this is an issue. Ultimately, it is up to the individual to decide if they are ready for a sexual encounter, and it is not up to anyone else to judge.",
        "title": "[DISCUSSION] Emily in Paris is SO bad",
        "upvotes": 1140
    },
    {
        "content_body": "Like Fight Club, The Illusionist, Midsommar… something that takes you aback with brilliance.\n\nEdit: thank you all so much, so many suggestions I haven’t seen. It’ll get me through being stuck at home. Y’all rock my fellow movie people.\n\nAlso sorry I can’t respond, I didn’t expect this many! I’m writing down each one I haven’t seen there are a lot!",
        "created_at": "Thu, 29 Dec 2022 23:29:29 GMT",
        "num_of_comments": 520,
        "overall_summary": "\n\nThis summary of comments is about a variety of movies with unexpected endings that leave viewers shocked and surprised. These movies include The Sixth Sense, Unbreakable, Split, Snowpiercer, Barbarian, The Signal, The Fountain, Triangle, Prestige, Time Crimes, Predestination, Usual Suspects, Primer, Red Notice, Laura, The Power of the Dog, Lucky Number Sleven, Possessor, Orphan, Inception, Dodgeball, Remember Me, Samaritan 2022, Memento, The Departed, Black Butterfly, The Empty Man, Donnie Darko, and Arlington Road. People have discussed their experiences with these movies, such as having the endings spoiled for them, and shared their opinions on the movies. They have also recommended these movies to each other, noting that they should go into them blind and not look into them or expect much in order to enjoy them.",
        "title": "[Request] Movies that have wtf ending. Something you wouldn’t expect but changes the whole movie",
        "upvotes": 653
    },
    {
        "content_body": "",
        "created_at": "Tue, 03 Jan 2023 01:56:38 GMT",
        "num_of_comments": 166,
        "overall_summary": "\n\nThis summary is about a discussion about Netflix's decision to cancel a show after two seasons, and the implications of their decision-making. People are disappointed and frustrated with the decision, arguing that Netflix does not understand the streaming audience or their platform, and that they should wait longer before canceling shows. They also criticize Netflix for replacing good content with unscripted reality shows and teen dramas, and for paying Adam Sandler for an 8 movie deal. Ultimately, it is suggested that Netflix should be more mindful of their data when making decisions.",
        "title": "[Discussion] 1899 got cancelled for season 2🤧...It just hurta to see like one of the best show I've seen on Netflix is not getting 2nd season🤧",
        "upvotes": 346
    }
]
```
