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
    username='', # this is your reddit username
    password='', # this is your reddit password 
    client_id='', # client ID from the top left of the information box
    client_secret='', # secret code developed by reddit 
    user_agent='' # the agent name you assigned 
)

# intializing which subreddit we want to look at
subreddit = reddit.subreddit('nbatopshot')

#which section we want to look at and the limit of entries to return
# i.e this subreddit isn't active enought for 1000 posts a day at the moment of 2/22/21
new_subreddit = subreddit.new(limit=1000)

# creating a dictionary to return the submission values and create a dataframe

topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num": [],
                "date": [],
                "body":[]}

# returning all the values from each post
for submission in new_subreddit:
    topics_dict["id"].append(submission.id)
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["date"].append(datetime.fromtimestamp(submission.created).strftime('%Y-%m-%d'))
    topics_dict["body"].append(submission.selftext)
    topics_dict["url"].append(submission.url)

# turning the dict to a df
topics_data = pd.DataFrame(topics_dict)

# only taking the posts w/ todays data
todays_subs = topics_data[topics_data['date'] >= datetime.now().strftime('%Y-%m-%d')]

# reading in for counting purposes
old = pd.read_csv('nbatop.csv')

#random printing stuff for length of data
print(f'Before this pull there are {len(old)} entries.\n')
print(f"Today there were {len(todays_subs)} on {datetime.now().strftime('%Y-%m-%d')}\n")

# appending new data to the csv
todays_subs.to_csv('nbatop.csv',index=False,header=False,mode='a')


# reading the new amount of data avaiablle and keeping only the latest version of duplicates
new = pd.read_csv('nbatop.csv')


#dropping duplicates for if you run the script more than once on the same day
# keeps the latest entry of the multiple if any
new = new.drop_duplicates(subset=['url'],keep='last')

# taking df without dups and creating a csv file.
new.to_csv('nbatop.csv',index=False,header=True)

print(f'Now there are {len(new)} entries, youre ending number may be the same as the starting number based upon how many pulls you do in a certain period of time!')