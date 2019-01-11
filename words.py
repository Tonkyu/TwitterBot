#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

def puttweet():

    twitter = OAuth1Session(os.environ["Ff82TWynJFSsl2FmXYPxr7sXd"], os.environ["1x4PfII5BDTtBrkl4XutydbTWPzyyxlQfpZ8GBcYmR4PZroNUA"], os.environ["1083391370180550657-E9AnSe8w1owhQk78Zqj4ZFQRu848Tz"], os.environ["vmgHw8ZCyMOrMyFDJqLjIQ5glTdau6w5Jj6tGLkddv6rm"])

    tweets = ["文章1",\
    "文章2",\
    "文章3",\
    "文章4",\
    "文章5"]
    randomtweet = tweets[random.randrange(len(tweets))]
    params = {"status": randomtweet} 
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)