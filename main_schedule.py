"""
Twits random lines from La Celestina at specific times during the day
using schedule library. It also saves them in a log file.
"""

from datetime import datetime
import schedule
import time

# tweepy, authentication, etc.
import tweepy
from secrets import choice
from credentials import cfg

# List of selected lines from La Celestina
from celestina import celines



def get_client():
    """
    Authenticates and returns client object (API v2)
    """
    client = tweepy.Client(
        bearer_token=cfg["bearer_token"],
        consumer_key=cfg["consumer_key"],
        consumer_secret=cfg["consumer_secret"],
        access_token=cfg["access_token"],
        access_token_secret=cfg["access_token_secret"],
    )
    return client


def get_tweet_text(source_collection):
    """
    Gets a random line from a given list
    """
    text = choice(source_collection)
    return text


def new_tweet(tweet_text):
    """
    Twits a given string
    """
    client = get_client()
    client.create_tweet(text=tweet_text)


def twit_random_celestina():
    """
    Twits a random line from La Celestina
    """
    tweet = get_tweet_text(celines)
    new_tweet(tweet)
    now = datetime.now().ctime()
    with open("log", "a") as f:
        f.write(f"{now}\t{tweet}\n")
    print(f"Twitted: {tweet} at {now} GMT.")
    

def scheduler():
    print(f"Scheduler at work since {time.asctime()}")
    schedule.every().day.at("08:00").do(twit_random_celestina)
    schedule.every().day.at("11:30").do(twit_random_celestina)
    schedule.every().day.at("13:30").do(twit_random_celestina)
    schedule.every().day.at("16:30").do(twit_random_celestina)
    schedule.every().day.at("19:30").do(twit_random_celestina)
    schedule.every().day.at("21:30").do(twit_random_celestina)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    try:
        scheduler()
    except (KeyboardInterrupt, SystemExit):
        pass
