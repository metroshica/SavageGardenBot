import praw
import credentials
import time
import logger
import sys


# Initial connection and subreddit selection
def connect():
    reddit = praw.Reddit(client_id=credentials.id,
                         client_secret=credentials.secret,
                         password=credentials.password,
                         user_agent='SavageGarden Moderator by /u/Metroshica',
                         username=credentials.username)
    return reddit.subreddit('savagegarden')


# Find posts that have one or more new grower keywords
def findposts(subreddit):
    keywords = [
        'help', 'newbie', 'noob', 'dying', 'trouble', 'new', 'advice', 'advise', 'tips', ' id ', 'id.', 'id?',
        'identify', 'save', 'trouble', 'first time'
    ]
    for submission in subreddit.new(limit=3):
        if any(word in submission.title.lower() for word in keywords):
            foundwords = []
            for word in keywords:
                if word in submission.title.lower():
                    foundwords.append(word)
            if checkifresponded(submission) is False:
                    respond(submission, foundwords)


# Check if bot has already responded or not
def checkifresponded(submission):
    responded = False
    commentlist = submission.comments.list()
    for comment in commentlist:
        if comment.author == 'SavageGardenBot':
            responded = True
    return responded


# Respond to post with helpful links
def respond(submission, foundwords):
    title = submission.title.lower()
    vfttext = '**Venus Flytraps**\t\n\t\n[Growing Guide](http://www.flytrapcare.com/store/venus-fly-trap-care-sheet)\t\n\t\n[Dormancy](http://www.flytrapcare.com/venus-fly-trap-dormancy.html)\t\n\t\n'
    sarrtext = '**Sarracenias**\t\n\t\n[Growing Guide](http://www.flytrapcare.com/store/sarracenia-care-sheet)\t\n\t\n[Dormancy](http://www.flytrapcare.com/store/sarracenia-care-sheet#tip6)\t\n\t\n'
    neptext = '**Nepenthes**\t\n\t\n[Growing Guide](http://www.flytrapcare.com/store/nepenthes-care-sheet/)\t\n\t\n[Temperature Chart](https://www.carnivorousplants.co.uk/resources/nepenthes-interactive-guide/)\t\n\t\n'

    responsetext = '''Welcome to /r/SavageGarden! Looks like you're looking for some help. Here are some great growing
    guides and a link to our FAQ that covers the most common questions we receive:\t\n\t\n'''

    faq = '**General Questions**\t\n\t\n[Frequently Asked Questions](http://sarracenia.com/faq.html)'
    vftwords = ['flytrap', 'fly trap', 'vft']

    if any(word in title for word in vftwords):
        responsetext = responsetext + vfttext
    elif 'pitcher' in title:
        responsetext = responsetext + sarrtext + '\n\n' + neptext
    elif 'nepenthes' in title:
        responsetext = responsetext + neptext
    elif 'sarr' in title:
        responsetext = responsetext + sarrtext
    else:
        responsetext = responsetext + vfttext + sarrtext + neptext

    submission.reply(responsetext + faq).mod.distinguish()

    print(submission.title + " - https://www.reddit.com" + submission.permalink + " " + str(foundwords))
    logger.log(submission.title + " - https://www.reddit.com" + submission.permalink + " " + str(foundwords))


def main():
    while True:
        try:
            subreddit = connect()
            findposts(subreddit)
        except:
            logger.log("Unexpected error: " + str(sys.exc_info()[0]))
        time.sleep(60)


if __name__ == "__main__":
    main()
