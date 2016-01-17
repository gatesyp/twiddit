# use: python twitterAgent.py <twitterID> <#oftweetswanted>
from __future__ import absolute_import, print_function

import time
import codecs
import tweepy
import json
import pprint

def store(tweet, profile, timestamp):

	fp = codecs.open("./tweetsRepo/" + profile + timestamp + ".txt", "a", "utf-8")
	print(tweet["text"])
	fp.write(str(tweet["text"].encode('utf-8')))
def getTweets(api, profile):
	timestamp = str(time.time())
	filename = profile + timestamp
	# use first argvar for the Twitter ID
	for tweet in tweepy.Cursor(api.user_timeline, id=profile).items():
		store(tweet._json, profile, timestamp)
	return filename
