import praw
import credentials


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
        'identify', 'save', 'trouble'
    ]
    for submission in subreddit.new(limit=20):
        if any(word in submission.title.lower() for word in keywords):
            if checkifresponded(submission) is False:
                respond(submission)


# Check if bot has already responded or not
def checkifresponded(submission):
    responded = False
    commentlist = submission.comments.list()
    for comment in commentlist:
        if comment.author == 'SavageGardenBot':
            responded = True
    return responded


# Respond to post with helpful links
def respond(submission):
    responsetext = "Looks like you're new here. Here's some info..."
    submission.reply(responsetext)
    print('Found one')
    pass


def main():
    subreddit = connect()
    findposts(subreddit)


if __name__ == "__main__":
    main()
