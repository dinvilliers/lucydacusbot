# thoroughbreds-bot

import tweepy
import random
import time

consumer_key = 'PgKiSmJzBZDBfwEg653fRby1D'
consumer_secret = '6tQb3IL9Fl8TCipTYlN0fV62Ehv4SXMvntDQKjKBXVAhyE9Gby'
access_token = '1464702032967839748-F8ToKGhMia8evWS1j2cQH3gKzxCIK4'
access_secret = 'X9bFvuGZIaywYUEEWxIB0Z3ie9ERq97KsBin1w5mRSHcl'

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

for script_status in open('lucy.txt'):

    try:
        print(random_line)
        if random_line != '\n':
            api.update_status(random_line('lucy.txt'))
            time.sleep (10800)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    time.sleep (1)
