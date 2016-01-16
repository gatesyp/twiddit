# use: python twitterAgent.py <twitterID> <#oftweetswanted>
from __future__ import absolute_import, print_function

import AuthHandler
import codecs
import sys
import tweepy
import json
import pprint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
# specifics to have a bot 
# TODO put these in seperate file and add to .gitignore

pp = pprint.PrettyPrinter(indent=4)

def store(tweet, profile):
	global pp
	fp = codecs.open(profile + ".txt", "a", "utf-8")
	fp.write(tweet["text"])

# using OAuth to validate connection
api = AuthHandler.login()

# use first argvar for the Twitter ID
for tweet in tweepy.Cursor(api.user_timeline, id=sys.argv[1]).items():
	store(tweet._json, sys.argv[1])

