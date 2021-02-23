# Written and maintained by Max Paul
# maxkpaul21@gmail.com
#
# A project of XamPak Open Source Software
# Follow my github for more !
# https://github.com/XamNalpak
#
# Last updated 2/22/21
#
#
# Interested in more ideas? Let me know !!##
#
#
#
#



# importing Python Packages
import praw
import pandas as pd
from datetime import datetime
import time


#Reddit API information from https://www.reddit.com/prefs/apps
# sign into your account and set up an app
reddit = praw.Reddit(
    username='DisastrousEquipment9', # this is your reddit username
    password='Arthur1085297', # this is your reddit password 
    client_id="eWmNLnOFjDRPPQ", # client ID from the top left of the information box
    client_secret="-zCfmJ9AOLC_0RXd6yS6LhzJ-SiWEA", # secret code developed by reddit 
    user_agent="maxs" # the agent name you assigned 
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


old = pd.read_csv('nbatop.csv')






#random printing stuff
print(f'Before this pull there are {len(old)} entries.')
print(f"Today there were {len(todays_subs)} on {datetime.now().strftime('%Y-%m-%d')}")

# appending new data to the csv
todays_subs.to_csv('nbatop.csv',index=False,header=False,mode='a')


# reading the new amount of data avaiablle and keeping only the latest version of duplicates
new = pd.read_csv('nbatop.csv')



new = new.drop_duplicates(subset=['url'],keep='last')


new.to_csv('nbatop.csv',index=False,header=True)

print(f'Now there are {len(new)} entries, youre ending number may be the same as the starting number based upon how many pulls you do in a certain period of time!')