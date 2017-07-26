import praw
import credentials

keywords = ['help', 'newbie', 'noob', 'dying', 'trouble','new', 'advice', 'advise', 'tips', ' id ', 'id.', 'id?',
            'identify', 'save', 'trouble']
possiblekeywords = ['vft', 'flytrap', 'fly trap']

reddit = praw.Reddit(client_id=credentials.id,
                     client_secret=credentials.secret,
                     password=credentials.password,
                     user_agent='SavageGarden Moderator by /u/Metroshica',
                     username=credentials.username)

subreddit = reddit.subreddit('savagegarden')

count = 0
for submission in subreddit.new(limit=100):
    #if any(word in submission.title.lower() for word in keywords):
    printstring = submission.title
    found = False
    #for word in keywords:
        #if word in submission.title.lower():
         #   printstring = printstring + " " + word
        #    found = True
    #if found == True:
        #print(printstring)
    print(submission.title)
    #count = count + 1

print(count)

def respond():
    pass