#Looks at r/chess post stream and private messages my reddit account to let me know about when Magnus Carlsen is being discussed
import praw
import re
import os

reddit = praw.Reddit('bot')

if not os.path.isfile('sent_record'):       #storing previously interacted-with posts in text file. Assume it does not exist
    sent_record = []
else:
    with open("reply_record", "r") as file:    #if code has been run at least once - add all values from text file to sent_record list
       sent_record = file.read()
       sent_record = sent_record.split("\n")
       sent_record = list(filter(None, sent_record))

for post in reddit.subreddit('chess').stream.submissions():
    if post.id not in sent_record:
        if re.search('carlsen\b', post.title, re.IGNORECASE):  
            reddit.redditor('testuser1234').message('Discussion about Carlsen detected!', post.shortlink)   #looks for carlsen in post title and messages me if so
            sent_record.append(post.id)

with open('sent_record', "w") as file:     #update text file
    for post_id in sent_record:
        file.write(post_id + "\n") 
 