import os
import requests
import json

class ApiConnection():
    def __init__(self, bearer_token=os.getenv('BEARER_TOKEN')):
        self.bearer = bearer_token
        self.URL = 'https://api.twitter.com/2'


    def get_tweets(self, tweet_ids=[]):
        headers = { 'Authorization': f'Bearer {self.bearer}' }
        payload = { 'ids': ','.join(map(str, tweet_ids)) }
        request = requests.get(f'{self.URL}/tweets', headers=headers, params=payload)
        response = json.loads(request.text)

        return response['data']


    def get_tweet(self, tweet_id):
        tweet = self.get_tweets([tweet_id])[0]

        return tweet
