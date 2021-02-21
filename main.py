import praw
import pandas as pd
from datetime import datetime
import time



reddit = praw.Reddit(
    username='DisastrousEquipment9',
    password='Arthur1085297',
    client_id="eWmNLnOFjDRPPQ",
    client_secret="-zCfmJ9AOLC_0RXd6yS6LhzJ-SiWEA",
    user_agent="maxs"
)

subreddit = reddit.subreddit('nbatopshot')
new_subreddit = subreddit.new(limit=1000)



topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num": [],
                "date": [],
                "body":[]}


for submission in new_subreddit:
    topics_dict["id"].append(submission.id)
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["date"].append(datetime.fromtimestamp(submission.created).strftime('%Y-%m-%d'))
    topics_dict["body"].append(submission.selftext)
    topics_dict["url"].append(submission.url)


topics_data = pd.DataFrame(topics_dict)

# make a function to sort out the posts only with the current days date to make sure we are not writting in the same post on accident 

todays_subs = topics_data[topics_data['date'] >= datetime.now().strftime('%Y-%m-%d')]

print(f'Today there were {len(todays_subs.length)} on {datetime.now().strftime('%Y-%m-%d')}')


todays_subs.to_csv('nbatop.csv',index=False,header=False,mode='a')