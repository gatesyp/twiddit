import praw
from urllib.parse import urlparse

def urlScrub(url):
	o = urlparse(url)
#	print(o.path)
	return o.path[3:]
def subscribe(url, user, passw):
	url = urlScrub(url)
	user_agent = "<androidOS>:<twiddit>:<1.0> (by /u/biszti)"
	r = praw.Reddit(user_agent=user_agent)
	r.login(user, passw)
	
	r.subscribe(url)
def subscriber(url, user, passw):	
	o = urlparse(url)
	print(o.path)
	s = o.path[3:]
	return s
#subscriber("http://www.reddit.com/r/dota2", "mybiszti", "lolipop123")
