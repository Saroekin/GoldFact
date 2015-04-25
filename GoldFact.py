# Name: GoldFact (/u/GoldFact)
# Author: Saroekin (/u/Saroekin)
# Version: Python 3.4.3


#Files or importations that are used elsewhere in program.
import os
import praw
import time
import sqlite3
from random import randint
from random import choice

print ("\n\nOpening database...")
#SQL database setup/ignition.
sql = sqlite3.connect('sql.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS cid_storage(ID TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS ignore_authors(ID TEXT)')
sql.commit()

#User's username and password.
Username = "" #: Enter your own username here.
Password = "" #: Enter your own password here.

#What reddit sees from the bot's requests.
user_agent = "" #: Enter your own user_agent here.
r = praw.Reddit(user_agent = user_agent)
print("\n\nLogging in...\n\n")
r.login(Username, Password)

#List of gold facts.
goldFactsList = [] #: Shh, secret. Amount of gold facts are hidden for . . . well, to keep private.

#Set of variables for program.
print ("Arranging variables...\n\n")
commentNum = 0
ignore_requests_string = "ignore-/u/goldfact"
obey_requests_string = "obey-/u/goldfact"

#Message/link variables.
ignore_message = "https://www.reddit.com/message/compose/?to=GoldFact&subject=Ignore-/u/GoldFact.&message=ignore-/u/goldfact"
obey_message = "https://www.reddit.com/message/compose/?to=GoldFact&subject=Obey-/u/GoldFact.&message=obey-/u/goldfact"
source_link = "https://github.com/Saroekin/GoldFact"
pm_link = "https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact"
info_post = "http://redd.it/339ec5"

#Templates for messages and comments (and variables).
MENTION_TEMPLATE_FACT = """
It looks as though I've been summoned! Here's the gold fact as you've requested:

>%s

---
^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator]({pm_link})].

^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post]({info_post})].

=
^| ^[[Ignore]({ignore_message})] ^| ^[[Obey]({obey_message})] ^| ^[[Source]({source_link})] ^|
""".format(pm_link = pm_link, info_post=info_post, ignore_message=ignore_message, obey_message=obey_message, source_link=source_link)

COMMENT_TEMPLATE_FACT = """
Hello there ol' chap! It seems to me that you've been gilded, therefore congratulations! Here's a gold fact to celebrate:

>%s

---
^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator]({pm_link})].

^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post]({info_post})].

=
^| ^[[Ignore]({ignore_message})] ^| ^[[Obey]({obey_message})] ^| ^[[Source]({source_link})] ^|
""".format(pm_link = pm_link, info_post=info_post, ignore_message=ignore_message, obey_message=obey_message, source_link=source_link)

COULD_NOT_REPLY = """
/u/GoldFact couldn't respond towards your message because you have ignored him. If you think this is a mistake, then look upon one of /u/GoldFact's post/comments, and click the "Obey" button formatted near the bottom. 

---
Tip: If you\'d like to use /u/GoldFact's name without him reacting, then use the command:

>n-/u/GoldFact
""".format()

mentionreply = MENTION_TEMPLATE_FACT % choice(goldFactList) #Selects random gold fact.
commentsubmit = COMMENT_TEMPLATE_FACT % choice(goldFactList)
notreply = COULD_NOT_REPLY

#Function for running (is defining) bot.
#In this definition, we are collecting user ignore requests.
def ignore_requests():
    for message in r.get_unread():
        message_text = message.body.lower()
        if ignore_requests_string not in message_text:
            continue
        mauth = message.author.name
        message = "You have successfully ignored /u/GoldFact."
        #Checking throught SQL database.
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [mauth])
        if not cur.fetchone():
            if message.subject in ['username mention', 'comment reply'] and type(message) == praw.objects.Comment:
                send_message(mauth, "Ignored /u/GoldFact.", message)                
            elif message.subject == "Ignore-/u/GoldFact." and type(message) == praw.objects.Message:
                callback = message.reply(message)
            #Adding authors that wish to be ignored into a database.
            cur.execute('INSERT INTO ignore_authors VALUES(?)', [mauth])
            sql.commit()
            message.mark_as_read()
        else:
            if message.subject in ['username mention', 'comment reply'] and type(message) == praw.objects.Comment:
                send_message(mauth, "Ignored /u/GoldFact.", message)
            elif message.subject == "Ignore-/u/GoldFact." and type(message) == praw.objects.Message:
                callback = message.reply(message)
            message.mark_as_read()

#Function for running (is defining) bot.
#In this definition, we are reapplying /u/GoldFact towards users who request acknowledgement.
def obey_requests():
    for message in r.get_unread():
        message_text = message.body.lower()
        if obey_requests_string not in message_text:
            continue
        mauth = message.author.name
        message = "You have successfully stopped ignoring /u/GoldFact."
        #Checking throught SQL database.
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [mauth])
        if cur.fetchone():
            if message.subject in ['username mention', 'comment reply'] and type(message) == praw.objects.Comment:
                send_message(mauth, "Acknowledged /u/GoldFact.", message)             
            elif message.subject == "Obey-/u/GoldFact." and type(message) == praw.objects.Message:
                callback = message.reply(message)
            #Removing authors that have been entered into the ignored database.
            cur.execute('DELETE FROM ignore_authors WHERE ID=?', [mauth])
            sql.commit()
            message.mark_as_read()
        else:
            if message.subject in ['username mention', 'comment reply'] and type(message) == praw.objects.Comment:
                send_message(mauth, "Acknowledged /u/GoldFact.", message)
            elif message.subject == "Obey-/u/GoldFact." and type(message) == praw.objects.Message:
                callback = message.reply(message)
            message.mark_as_read()

#Function for running (is defining) bot.
#In this definition, the bot is replying to messages (both username mentions and comment replies).
def run_bot_messages():
    for message in r.get_unread():
        message_text = message.body.lower() 
        mauth = message.author.name
        #Checking throught SQL database.
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [mauth])
        if not cur.fetchone(): 
            if message.subject in ['username mention', 'comment reply'] and type(message) == praw.objects.Comment and "n-/u/goldfact" in message_text:
                message.mark_as_read()  
            elif message.subject == "username mention" and type(message) == praw.objects.Comment:
                callback = message.reply(mentionreply)
                message.mark_as_read()
            elif message.subject == "comment reply" and type(message) == praw.objects.Comment and "/u/goldfact" in message_text:
                callback = message.reply(mentionreply)
                message.mark_as_read()
        else:
            if message.subject == "username mention" and type(message) == praw.objects.Comment:
                message = notreply
                send_message(mauth, "Error.", message)
                message.mark_as_read()
            elif message.subject == "comment reply" and type(message) == praw.objects.Comment and "/u/goldfact" in message_text:
                message = notreply
                send_message(mauth, "Error.", message)
                message.mark_as_read()

#Function for running (is defining) bot.
#In this definition, the bot is posting/commenting to gilded comments from /r/lounge (and maybe submissions later on).
def run_bot_comments_lounge():
    subreddit = r.get_subreddit("lounge")
    comments = subreddit.get_comments(gilded_only=True, limit=50)
    for comment in comments:
        cid = comment.id
        cauth = comment.author.name
        #Checking throught SQL database.
        cur.execute('SELECT * FROM cid_storage WHERE ID=?', [cid])
        if cur.fetchone():
            continue
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [cauth])
        if cur.fetchone():
            continue
        try:
            comment_text = comment.body.lower()
            if str(comment.author) != Username:
                commentNum = randint(0,19)
                if commentNum == 2:
                    comment.reply(commentsubmit)
        except AttributeError:
            pass
        #Adding comment id into SQL database.
        cur.execute('INSERT INTO cid_storage VALUES(?)', [cid])
        sql.commit()

#Function for running (is defining) bot.
#In this definition, the bot is posting/commenting to gilded comments from /r/all (and maybe submissions later on).
def run_bot_comments_all():
    subreddit = r.get_subreddit("all")
    comments = subreddit.get_comments(gilded_only=True, limit=100)
    for comment in comments:
        cid = comment.id
        cauth = comment.author.name
        #Checking throught SQL database.
        cur.execute('SELECT * FROM cid_storage WHERE ID=?', [cid])
        if cur.fetchone():
            continue
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [cauth])
        if cur.fetchone():
            continue
        try:
            comment_text = comment.body.lower()
            if str(comment.author) != Username:
                commentNum = randint(0,39)
                if commentNum == 2:
                    comment.reply(commentsubmit)
        except AttributeError:
            pass
        #Adding comment id into SQL database.
        cur.execute('INSERT INTO cid_storage VALUES(?)', [cid])
        sql.commit()

#Where bot begins (continues) to run.
print("/u/GoldFact (bot) is running...\n")
while True:
    ignore_requests()
    obey_requests()
    run_bot_messages()
    run_bot_comments_lounge()
    run_bot_comments_all()
