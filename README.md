# twiddit
Using sentiment analysis on a user's tweet in order to create a custom reddit account for them

Dependencies: 
Register a twitter app for OAuth
tweepy
IBM AlchemyAPI key 
reddit python API

I am using Python for development, heavy reliance on JSON

TODO: do in C++ or Java for learning purposes

1. Download 50-100 tweets (store content in database?  ) 
2. Take content of each tweet and concatenate bunches of 20 tweets together
3. Use AlchemyAPI on batch of tweets
4. Take results, find highest positive probabilities in the Entity and Keyword which are also positive (above 70 percent)
5. Find related subreddits
	a. using google queries: 'site: reddit.com "steelers"' and go to the top two links, subscribe to each subreddit using reddit API
