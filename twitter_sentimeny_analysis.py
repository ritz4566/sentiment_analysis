from textblob import TextBlob
import tweepy

consumer_key = 'xBs2s0jeSgaArvQucYqf9Vg8a'
consumer_secret = 'eFYLUDyXJWMCnIh5f0ffqguK33mdz3L4EZBffw8pzSfdAyi9uB'

access_token = '1154231799087808513-dcmh5IUIs0Ge6wkHiFqF5QDGurjDtr'
access_token_secret = 'kgXccowy29MV5AmX7sYpMH62pjWdfzGj6Fx2RH8ctUkiv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('India')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)