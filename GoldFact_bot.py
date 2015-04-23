#Files or importations that are used elsewhere in program.
import praw
import time
import sqlite3
from random import randint

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
goldFactsList = [] #: Shh, secret. Amount / list of gold facts are hidden for . . . well, to keep secret / private.

#Set of variables for program.
print ("Arranging variables...\n\n")
randomNum = 0
commentNum = 0
ignore_requests_string = "ignore-/u/goldfact"
obey_requests_string = "obey-/u/goldfact"

#Message/link variables.
ignore_message = "https://www.reddit.com/message/compose/?to=GoldFact&subject=Ignore-/u/GoldFact.&message=ignore-/u/goldfact"
obey_message = "https://www.reddit.com/message/compose/?to=GoldFact&subject=Obey-/u/GoldFact.&message=obey-/u/goldfact"
source_link = "https://github.com/Saroekin/GoldFact"

#Function for running (is defining) bot.
#In this definition, we are collecting user ignore requests.
def ignore_requests():
    for message in r.get_unread():
        message_text = message.body.lower()
        mauth = message.author.name
        #Checking throught SQL database.
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [mauth])
        if not cur.fetchone():
            if message.subject == "username mention" or "comment reply" and type(message) == praw.objects.Comment and ignore_requests_string in message_text:
        	    #Adding authors that wish to be ignored into a database.
                cur.execute('INSERT INTO ignore_authors VALUES(?)', [mauth])
                sql.commit()                
                message.mark_as_read()
            elif message.subject == "Ignore-/u/GoldFact." and type(message) == praw.objects.Message and ignore_requests_string in message_text:
                cur.execute('INSERT INTO ignore_authors VALUES(?)', [mauth])
                sql.commit()
                callback = message.reply("You have successfully ignored /u/GoldFact.")
                message.mark_as_read()
        elif not cur.fetchone():
        	callback = message.reply("Can't comply, for you have already ignored /u/GoldFact.")
        	message.mark_as_read()

#Function for running (is defining) bot.
#In this definition, we are reapplying /u/GoldFact towards users who request acknowledgement.
def obey_requests():
    for message in r.get_unread():
        message_text = message.body.lower()
        mauth = message.author.name
        #Checking throught SQL database.
        cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [mauth])
        if cur.fetchone():
            if message.subject == "username mention" or "comment reply" and type(message) == praw.objects.Comment and obey_requests_string in message_text:
                #Removing authors that have been entered into the ignored database.
                cur.execute('DELETE VALUES(?) FROM total_data', [mauth])
                sql.commit()
                message.mark_as_read()
            elif message.subject == "Obey-/u/GoldFact." and type(message) == praw.objects.Message and obey_requests_string in message_text:
                cur.execute('DELETE VALUES(?) FROM total_data', [mauth])
                sql.commit()
                callback = message.reply("You have successfully stopped ignoring /u/GoldFact.")
                message.mark_as_read()
        elif not cur.fetchone():
            callback = message.reply("Can't comply, for you haven't ignored /u/GoldFact.")
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
            if message.subject == "username mention" or "comment reply" and type(message) == praw.objects.Comment and "n-/u/goldfact" in message_text:
                message.mark_as_read()  
            elif message.subject == "username mention" and type(message) == praw.objects.Comment:
                #Selects a random gold fact.
                randomNum = randint(0,51)
                callback = message.reply("It looks as though I've been summoned! Here's the gold fact as you've requested:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
                message.mark_as_read()
            elif message.subject == "comment reply" and type(message) == praw.objects.Comment and "/u/goldfact" in message_text:
                randomNum = randint(0,51)
                callback = message.reply("It looks as though I've been summoned! Here's the gold fact as you've requested:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
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
        if not cur.fetchone():
            cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [cauth])
            if not cur.fetchone():
                try:
                    comment_text = comment.body.lower()
                    if str(comment.author) != Username:
                        randomNum = randint("input num","input num") #: Amount of random numbers taken out so the privacy of /u/GoldFact's fact count is kept exclusive.
                        commentNum = randint(0,99)
                        #To add a random factor whilst commenting.
                        if commentNum == 2:
                            comment.reply("Hello there ol' chap! It seems to me that you've been gilded, therefore congratulations! Here's a gold fact to celebrate:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
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
        if not cur.fetchone():
            cur.execute('SELECT * FROM ignore_authors WHERE ID=?', [cauth])
            if not cur.fetchone():
                try:
                    comment_text = comment.body.lower()
                    if str(comment.author) != Username:
                        randomNum = randint("input num","input num") #: Amount of random numbers taken out so the privacy of /u/GoldFact's fact count is kept exclusive.
                        commentNum = randint(0,998)
                        #To add a random factor whilst commenting.
                        if commentNum == 2:
                            comment.reply("Hello there ol' chap! It seems to me that you've been gilded, therefore congratulations! Here's a gold fact to celebrate:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
                except AttributeError:
                    pass
                #Adding comment id into SQL database.
                cur.execute('INSERT INTO cid_storage VALUES(?)', [cid])
                sql.commit()

#Where bot begins (continues) to run.
print("/u/GoldFact (bot) is running...")
while True:
    ignore_requests()
    obey_requests()
    run_bot_messages()
    run_bot_comments_lounge()
    run_bot_comments_all()
