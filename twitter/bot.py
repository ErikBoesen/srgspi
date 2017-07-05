import tweepy
import time
import sys
import yaml

with open('coptions.yaml') as yf:
    OP = yaml.load(yf.read())

auth = tweepy.OAuthHandler(OP['consumer-key'], OP['consumer-secret'])
auth.set_access_token(OP['access-key'], OP['access-secret'])
t = tweepy.API(auth)

#t.update_status('Look, it\'s almost like I actually tweeted!')
