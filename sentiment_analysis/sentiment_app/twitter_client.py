import tweepy
import time
from django.conf import settings

class TwitterClient:
	def __init__(self):
		
		TWITTER_API_KEY = '5qTpRosAxr8dX9IOmv9tPg7Yj'
		TWITTER_API_SECRET_KEY = 'nYCStCuuxdB1UVNRbwPnk4bQUx3uBQJp8451tO3BLf8woJIVHg'
		TWITTER_ACCESS_TOKEN = '1781060980014817280-MLrYLLTblSJEFIyApUkPYPgexvuGKx'
		TWITTER_ACCESS_TOKEN_SECRET = 'J1C9Uj68jHEeYWqsxNEZUx4fvVxoGviktGkQFY5SEQq3T'
		BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACf9wwEAAAAAfMleXQ2i%2BOENsHiwPdQGPfZ9j2k%3DNYDKubDiBMHRObFEnOuTWW97vRCKIZPvvag3TAU6kBpAFYLEnk'
		
		auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
		auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(auth)
		self.client = tweepy.Client(bearer_token=BEARER_TOKEN)
	
	def fetch_tweets(self, query, max_results=1):
		try:
			response = self.client.search_recent_tweets(
				query=query,
				max_results=max_results,
				tweet_fields=['created_at', 'text', 'author_id', 'lang']
			)
			return response.data
		except Exception as e:
			print(f"Error fetching tweets: {e}")
			return []
			

