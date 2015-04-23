#-----------------#
# GoldFact        #
# By: /u/Saroekin #
#-----------------#



#Files or importations that are used elsewhere in program.
import praw
import time
import sqlite3
from random import randint

print ("\nOpening database...")
#SQL database setup/ignition.
sql = sqlite3.connect('sql.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS total_data(cid_storage TEXT, ignore_authors TEXT)')
sql.commit()

#User's username and password.
Username = ""
Password = ""

#What reddit sees from the bot's requests.
user_agent = "/u/GoldFact is an API by /u/Saroekin. If 'summoned' by a user, /u/GoldFact will reply with a random fact. As well as /u/GoldFact will watch over the gilded section of /r/lounge and /r/all, and congratulate any newly gilded users with a gold fact (not everyone, there's chances behind /u/GoldFact replying to gilded users)."
r = praw.Reddit(user_agent = user_agent)
print("\n\nLogging in...\n\n")
r.login(Username, Password)

#List of gold facts.
goldFactsList = ["The term “gold” is the from the Proto-Indo-European base *ghel / *ghol meaning “yellow,” “green,” or possibly “bright.”", "Gold is so rare that the world pours more steel in an hour than it has poured gold since the beginning of recorded history.", "Gold has been discovered on every continent on earth.", "Gold melts at 1064.43° Centigrade. It can conduct both heat and electricity and it never rusts. ", "Due to its high value, most gold discovered throughout history is still in circulation. However, it is thought that 80% of the world’s gold is still in the ground. ", "Seventy-five percent of all gold in circulation has been extracted since 1910. ", "A medical study in France during the early twentieth century suggests that gold is an effective treatment for rheumatoid arthritis. ", "Gold is so pliable that it can be made into sewing thread. An ounce of gold can be stretched over 50 miles. ", "Gold is edible. Some Asian countries put gold in fruit, jelly snacks, coffee, and tea. Since at least the 1500s, Europeans have been putting gold leaf in bottles of liquor, such as Danziger Goldwasser and Goldschlager. Some Native American tribes believed consuming gold could allow humans to levitate. ", "The largest gold nugget ever found is the “Welcome Stranger” discovered by John Deason and Richard Oates in Australia on February 5, 1869. The nugget is 10 by 25 inches and yielded 2,248 ounces of pure gold. It was found just two inches below the ground's surface. ", "Amid recession fears in March 2008, the price of gold topped $1,000 an ounce for the first time in history. ", "Traditionally, investors try to preserve their assets during hard economic times by investing in precious metals, such as gold and silver. The World Gold Council released a report in February 2009 that indicated the demand for gold rose sharply in the last half of 2008. ", "The Dow/Gold ratio, which shows how much gold it would take to buy one share of the Dow, is a good indicator of how bad a recession is. In early 2009, the Dow/Gold ratio appeared to be heading toward the same low ratios that occurred during the 1930s and 1980s. ", "Gold is chemically inert, which also explains why it never rusts and does not cause skin irritation. If gold jewelry irritates the skin, it is likely that the gold was mixed with some other metal. ", "One cubic foot of gold weighs half a ton. The world’s largest gold bar weighs 200 kg (440 lb). ", "In 2005, Rick Munarriz queried whether Google or gold was a better investment when both seemed to have equal value on the stock market. By the end of 2008, Google closed at $307.65 a share, while gold closed the year at $866 an ounce. ", "The Olympic gold medals awarded in 1912 were made entirely from gold. Currently, the gold medals must be covered in six grams of gold.", "The Incas thought gold represented the glory of their sun god and referred to the precious metal as “tears of the Sun.” Because gold was not yet used for money, the Inca’s love of gold was purely aesthetic and religious. ", "Around 1200 B.C., the Egyptians used unshorn sheepskin to mine for gold dust from the sands of the Black Sea. This practice is most likely the inspiration for the “Golden Fleece.” ", "In ancient Egypt, gold was considered the skin or flesh of the gods, particularly the Egyptian sun god Ra. Consequently, gold was unavailable to anyone but the pharaohs, and only later to priests and other members of the royal court. The chambers that held the King's sarcophagus was known as the “house of gold.” ", "The Turin Papyrus shows the first map of a gold mine in Nubia, a major gold producer in antiquity. Indeed, the Egyptian word for gold was “nub,” from gold-rich Nubia. While Egyptian slaves often suffered terribly in gold mines, Egyptian artisans who made gold jewelry for the nobles enjoyed a high, almost priestly status. ", "Though the ancient Jews apparently had enough gold to create and dance around a golden calf while Moses was talking to God on Mt. Sinai, scholars speculate that it never occurred to the Jews to bribe themselves out of captivity because gold was not yet associated with money. ", "There are more than 400 references to gold in the Bible, including specific instructions from God to cover furniture in the tabernacle with “pure gold.” Gold is also mentioned as one of the gifts of the Magi. ", "The Greeks thought that gold was a dense combination of water and sunlight. ", "In 560 B.C., the Lydians introduced the first gold coin, which was actually a naturally occurring amalgam of gold and silver called electrum. Herodotus criticizes the materialism of the Lydians, who also were the first to open permanent retail shops. When the Lydians were captured by the Persians in 546 B.C., the use of gold coins began to spread. ", "Before gold coins were used as money, various types of livestock, particularly cattle, and plant products were used as currency. Additionally, large government construction projects were completed by slave labor due to the limited range of money uses. ", "The chemical symbol for gold is Au, from the Latin word aurum meaning “shining dawn” and from Aurora, the Roman goddess of the dawn. In 50 B.C., Romans began issuing gold coins called the Aureus and the smaller solidus. ", "When honking geese alerted the Romans that the Gauls were about to attack the temple where the Romans stored their treasure, the grateful Roman citizens built a shrine to Moneta, the goddess of warning. The link between rescued treasure and Moneta led many centuries later to the English words “money” and “mint.” ", "Between A.D. 307 and 324, the worth of one pound of gold in Rome rose from 100,000 denarii (a Roman coin) to 300,000 denarii. By the middle of the fourth century, a pound of gold was worth 2,120,000,000 denarii—an early example of runaway inflation, which was partly responsible for the collapse of the Roman Empire. ", "The Trial of the Pyx (a public test of the quality of gold) began in England in 1282 and continues to this day. The term “pyx” refers to a Greek boxwood chest in which coins are placed to be presented to a jury for testing. Coins are currently tested for diameter, chemical composition, and weight. ", "During the fourteenth century, drinking molten gold and crushed emeralds was used as a treatment for the bubonic plaque. ", "In 1511, King Ferdinand of Spain coined the immortal phrase: “Get gold, humanely if possible—but at all hazards, get gold.” ", "Both Greeks and Jews begin to practice alchemy in 300 B.C. The search to turn base metals into gold would reach its pinnacle in the late Middle Ages and Renaissance. ", "In 1599, a Spanish governor in Ecuador taxed the Jivaro tribe so excessively that they executed him by pouring molten gold down his throat. This form of execution was also practiced by the Romans and the Spanish Inquisition. ", "Venice introduced the gold ducat in 1284 and it became the most popular gold coin in the world for the next 500 years. Ducat is Latin for “duke.” It is the currency used in Shakespeare’s Romeo and Juliet and is referenced in The Merchant of Venice. In his song “I Ain’t the One,” rapper Ice Cube sings that “he’s getting juiced for his ducats.” The ducat is also used in the “Babylon 5” sci-fi series as the name of the Centauri race’s money. ", "Originally the U.S. mint made $2.50, $10, and $15 coins of solid gold. Minting of gold stopped in 1933, during the Great Depression. ", "The San Francisco 49ers are named after the 1849 Gold Rush miners. ", "Gold and copper were the first metals to be discovered by humans around 5000 B.C. and are the only two non-white-colored metals. ", "The value of gold has been used as the standard for many currencies. After WWII, the United States created the Bretton Woods System, which set the value of the U.S. dollar to 1/35th of a troy ounce (888.671 mg) of gold. This system was abandoned in 1971 when there was no longer enough gold to cover all the paper money in circulation. ", "The world’s largest stockpile of gold can be found five stories underground inside the Federal Reserve Bank of New York’s vault and it holds 25% of the world's gold reserve (540,000 gold bars). While it contains more gold than Fort Knox, most of it belongs to foreign governments. ", "The “troy ounce” of gold comes from the French town of Troyes, which first created a system of weights in the Middle Ages used for precious metals and gems. One troy ounce is 480 grains. A grain is exactly 64.79892 mg. ", "The gold standard has been replaced by most governments by the fiat (Latin for “let it be done”) standard. Both Thomas Jefferson and Andrew Jackson strongly opposed fiat currency. Several contemporary economists argue that fiat currency increases the rate of boom-bust cycles and causes inflation. ", "The Mines of South Africa can descend as far as 12,000 feet and reach temperatures of 130°F. To produce an ounce of gold requires 38 man hours, 1400 gallons of water, enough electricity to run a large house for ten days, and chemicals such as cyanide, acids, lead, borax, and lime. In order to extract South Africa’s yearly output of 500 tons of gold, nearly 70 million tons of earth are raised and milled. ", "Only approximately 142,000 tons of gold have mined throughout history. Assuming the price of gold is $1,000 per ounce, the total amount of gold that has been mined would equal roughly $4.5 trillion. The United States alone circulates or deposits over $7.6 trillion, suggesting that a return to the gold standard would not be feasible. While most scholars agree a return to a gold standard is not feasible, a few gold standard advocates (such as many Libertarians and Objectivists), argue that a return to a gold standard system would ease inflation risks and limit government power. ", "The first recorded gold ever discovered in the United States was a 17-pound nugget found in Cabarrus, North Carolina. When more gold was discovered in Little Meadow Creek, North Carolina, in 1803, the first U.S. gold rush began. ", "In 1848, while building a sawmill for John Sutter near Sacramento, California, John Marshal discovered flakes of gold. This discovery sparked the California Gold Rush and hastened the settlement of the American West. ", "In 1933, Franklin Roosevelt signed Executive Order 6102 which outlawed U.S. citizens from hoarding gold. Owning gold (except for jewelers, dentists, electricians, and other industry workers) was punishable by fine up to $10,000 and/or ten years in prison. ", "Tiny spheres of gold are used by the Amersham Corporation of Illinois as a way to tag specific proteins to identify their function in the human body for the treatment of disease. ", "The purity of gold is measured in carat weight. The term “carat” comes from “carob seed,” which was standard for weighing small quantities in the Middle East. Carats were the fruit of the leguminous carob tree, every single pod of which weighs 1/5 of a gram (200 mg). ", "Carat weight can be 10, 12, 14, 18, 22, or 24. The higher the number, the greater the purity. To be called “solid gold,” gold must have a minimum weight of 10 carats. “Pure gold” must have a carat weight of 24, (though there is still a small amount of copper in it). Pure gold is so soft that it can be molded by hand.", "Gold is bright yellow and has a high luster. Apart from copper and caesium it is the only non white colored metal. Gold’s attractive warm colour has led to its widespread use in decoration.", "Chocolate gold is derived from a relatively new method created in Italy. Referred to as physical vaporization and deposition, it entails placing gold (usually rose-colored) in a suction compartment and blasting it with electrodes. This approach causes the gold's surface to oxidize in a controlled environment, resulting in the metal's color changing at a molecular level and producing a rich chocolate color. This permanently alters the metal and can only be removed by scraping off the outer layers."]

#Set of variables for program.
print ("Arranging variables...\n\n")
randomNum = 0
commentNum = 0
ignore_requests_string = "ignore-/u/goldfact"
obey_requests_string = "obey-/u/goldfact"
#delete_comments_string = "delete-comment-/u/GoldFact"
ignore_authors = []
cid_storage = []

#Message/link variables.
ignore_message = "https://www.reddit.com/message/compose/?to=/u/GoldFact&subject=Ignore-/u/GoldFact.&message=ignore-/u/goldfact"
obey_message = "https://www.reddit.com/message/compose/?to=/u/GoldFact&subject=Obey-/u/GoldFact.&message=obey-/u/goldfact"
#delete_message = "https://www.reddit.com/message/compose/?to=/u/GoldFact&subject=Delete-/u/GoldFact's-comment.&message=delete-comment-/u/GoldFact%20{thing_id}"
source_link = "https://github.com/Saroekin/GoldFact"

#Function for running (is defining) bot.
#In this definition, we are collecting user ignore requests.
def ignore_requests():
    for message in r.get_unread():
        message_text = message.body.lower()
        mauth = message.author
        #Checking throught SQL database.
        cur.execute('SELECT * FROM total_data WHERE ignore_authors=?', [cauth])
        if not cur.fetchone():
            if message.subject == "username mention" or "comment reply" and type(message) == praw.objects.Comment and ignore_requests_string in message_text:
        	    #Adding authors that wish to be ignored into a database.
                cur.execute('INSERT INTO total_data (ignore_authors) VALUES(?)', [cauth])
                sql.commit()                
                message.mark_as_read()
            elif message.subject == "Ignore-/u/GoldFact." and type(message) == praw.objects.Comment and ignore_requests_string in message_text:
                cur.execute('INSERT INTO total_data (ignore_authors) VALUES(?)', [cauth])
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
        mauth = message.author
        #Checking throught SQL database.
        cur.execute('SELECT * FROM total_data WHERE ignore_authors=?', [cauth])
        if cur.fetchone():
            if message.subject == "username mention" or "comment reply" and type(message) == praw.objects.Comment and obey_requests_string in message_text:
                #Removing authors that have been entered into the ignored database.
                cur.execute('DELETE VALUES(?) FROM total_data', [cauth])
                sql.commit()
                message.mark_as_read()
            elif message.subject == "Obey-/u/GoldFact." and type(message) == praw.objects.Comment and obey_requests_string in message_text:
                cur.execute('DELETE VALUES(?) FROM total_data', [cauth])
                sql.commit()
                callback = message.reply("You have successfully stopped ignoring /u/GoldFact.")
                message.mark_as_read()
        elif not cur.fetchone():
            callback = message.reply("Can't comply, for you haven't ignored /u/GoldFact.")
            message.mark_as_read()

#Function for running (is defining) bot.
#In this definition, the bot is deleting its own comment in the say of the orignial comment author.
#def deleting_comments():
    #for message in r.get_unread():
	    #message_text = message.body.lower()
	    #if message.subject == "Delete-/u/GoldFact's-comment." and type(message) == praw.objects.Comment and delete_comments_string in message_text:
		    #if 

#Function for running (is defining) bot.
#In this definition, the bot is replying to messages (both username mentions and comment replies).
def run_bot_messages():
    for message in r.get_unread():
        message_text = message.body.lower() 
        cauth = comment.author
        #Checking throught SQL database.
        cur.execute('SELECT * FROM total_data WHERE ignore_authors=?', [cauth])
        if not cur.fetchone():       
            if message.subject == "username mention" and type(message) == praw.objects.Comment:
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
        cauth = comment.author
        #Checking throught SQL database.
        cur.execute('SELECT * FROM total_data WHERE cid_storage=?', [cid])
        if not cur.fetchone():
            cur.execute('SELECT * FROM total_data WHERE ignore_authors=?', [cauth])
            if not cur.fetchone():
                try:
                    comment_text = comment.body.lower()
                    if str(comment.author) != Username:
                        randomNum = randint(0,51)
                        commentNum = randint(0,32)
                        #To add a random factor whilst commenting.
                        if commentNum == 2:
                            comment.reply("Hello there ol' chap! It seems to me that you've been gilded, therefore congratulations! Here's a gold fact to celebrate:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
                except AttributeError:
                    pass
                #Adding comment id into SQL database.
                cur.execute('INSERT INTO total_data (cid_storage) VALUES(?)', [cid])
                sql.commit()

#Function for running (is defining) bot.
#In this definition, the bot is posting/commenting to gilded comments from /r/all (and maybe submissions later on).
def run_bot_comments_all():
    subreddit = r.get_subreddit("all")
    comments = subreddit.get_comments(gilded_only=True, limit=100)
    for comment in comments:
        cid = comment.id
        cauth = comment.author
        #Checking throught SQL database.
        cur.execute('SELECT * FROM total_data WHERE cid_storage=?', [cid])
        if not cur.fetchone():
            cur.execute('SELECT * FROM total_data WHERE ignore_authors=?', [cauth])
            if not cur.fetchone():
                try:
                    comment_text = comment.body.lower()
                    if str(comment.author) != Username:
                        randomNum = randint(0,51)
                        commentNum = randint(0,998)
                        #To add a random factor whilst commenting.
                        if commentNum == 2:
                            comment.reply("Hello there ol' chap! It seems to me that you've been gilded, therefore congratulations! Here's a gold fact to celebrate:" + "\n" + "\n" + ">" + str(goldFactsList[randomNum]) + "\n" + "\n" + "---" + "\n" + "^I ^am ^a ^bot. ^If ^you ^have ^any ^questions ^or ^requests, ^please ^contact ^my ^[[creator](https://www.reddit.com/message/compose/?to=Saroekin&subject=/u/GoldFact)]." + "\n" + "\n" + "^If ^you ^would ^like ^to ^read ^or ^learn ^more ^about ^my ^functionalities, ^please ^head ^over ^to ^this ^[[post](https://www.reddit.com/r/Saroekin_redditBots/comments/339ec5/ugoldfact_information/)]." + "\n\n" + "^| ^[[Ignore](" + ignore_message + ")] ^| ^[[Obey](" + obey_message + ")] ^| ^[[Source](" + source_link + ")] ^|")
                except AttributeError:
                    pass
                #Adding comment id into SQL database.
                cur.execute('INSERT INTO total_data() (cid_storage) VALUES(?)', [cid])
                sql.commit()

#Where bot begins (continues) to run.
print("/u/GoldFact (bot) is running...")
#For testing purposes.
spot=0
while spot < 1:
    ignore_requests()
    obey_requests()
    #deleting_comments()
    run_bot_messages()
    run_bot_comments_lounge()
    run_bot_comments_all()
    spot += 1



#-------------------------------------------------
#Taken out code (also ideas), could possibly use again later:
#: "Here's a gold fact!" + "\n" + "\n" +
#: Include a delete function, if the user would like it so. "If you'd rather have this comment (fact) be removed, click [[delete]()]." 
#: Be able to have a user direct the message to another user (where the other user may delete the comment provided by /u/GoldFact).
#: To be able to delete and 
