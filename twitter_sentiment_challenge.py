import tweepy
from textblob import TextBlob
from pprint import pprint

class TwitterClient:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def set_query(self, query = ' '):
        self.query = query

    def set_with_sentiment(self, with_sentiment = 'false'):
        self.with_sentiment = with_sentiment

    def get_tweet_sentiment(self, tweet):
        sentiment = TextBlob(self.clean_tweet((tweet)))
        if sentiment.sentiment.polarity > 0:
            return 'positive'
        elif sentiment.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, max_tweets = 100, retweets_only = False):
        tweets = []

        try:
            received_tweets = self.api.search(q = self.query, count = max_tweets)
            for tweet in received_tweets:
                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text
                parsed_tweet['user'] = tweet.user.screen_name

                if self.set_with_sentiment == 1:
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                else:
                    parsed_tweet['sentiment'] = 'unavailable'

                if tweet.retweet_count > 0 and retweets_only == True:
                    if parsed_tweet not in tweets:
                        print("entering 1")
                        tweets.append(parsed_tweet)
                elif retweets_only == False:
                    if parsed_tweet not in tweets:
                        print("entering 2")
                        tweets.append(parsed_tweet)
            return tweets

        except tweepy.TweepError as error:
            print("Error : " +str(error))






consumer_key = ' ' 
consumer_secret = ' '
access_token = ' '
access_secret = ' ' 


ClientOne = TwitterClient(consumer_key, consumer_secret, access_token, access_secret)
ClientOne.set_query(query='carrie')
for tweets in ClientOne.get_tweets():
    pprint(tweets)

#kstep 1 authenticate







