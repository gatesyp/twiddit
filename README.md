# twiddit
GOAL:
	Using sentiment analysis on a user's twitter profile in order to create a custom reddit account.

Dependencies: 
Register a twitter app for OAuth
register an app for Google API
tweepy 3.4
IBM AlchemyAPI
reddit python API(I am using PRAW)

Technology used: Python 3.5

TODO: 
	1. Fix encoding errors from twitter\n
	2. Register with Google API services to allow for more requests\n
	3. Instead of .txt file, upload to MySQL database and include more information about each tweet\n
	4. Create website for interfacing\n

Procedure:
	1. Download all tweets
	2. Take content of tweets and append to text file
	3. Pipe text file to AlchemyAPI
	4. Take results, find highest positive probabilities in the Entity and Keyword which are also relevant(above 40 percent to account for diluted tweets)
	5. Find related subreddits using crude recommendation system
		. using google queries: 'site: reddit.com "steelers"' and return top 2 URL's 
	6. Tokenize the resulting URLs and subscribe to appropriate subreddit

github notes: 

git checkout -b dev

git commit 'file' -m "<msg>"

git push


git checkout master

git merge dev

git push
