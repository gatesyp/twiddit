# use: python twitterAgent.py <twitterID> <#oftweetswanted>
from __future__ import absolute_import, print_function

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

consumer_key="Gra7ryY50P7Wr2oqfjen6C8Q5"
consumer_secret="vz2IRxjqSUAyiGIqAvFHMtHN3DzcGt3DHl2LnI6zSGwXvP3rqG" 
access_token="378220962-EZjtEVdg9DVvIt9FqfgiJw38j8iLnAFyc0cGOrnU"
access_token_secret="RJm3zc30b3hq4TdQLS1WyLW194lLfLINLKqo8zwCsKOfo"

pp = pprint.PrettyPrinter(indent=4)

def store(tweet, profile):
	global pp
	fp = codecs.open(profile + ".txt", "a", "utf-8")
	fp.write(tweet["text"])

# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# use first argvar for the Twitter ID
for tweet in tweepy.Cursor(api.user_timeline, id=sys.argv[1]).items():
	store(tweet._json, sys.argv[1])

