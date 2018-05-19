import tweepy
import pymongo

C_KEY = "c_key"
C_SECRET = "c_secret"

A_TOKEN="token"
A_TSECRET="secret"

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TSECRET)
api = tweepy.API(auth)


from pymongo import MongoClient
client = MongoClient()
db = client['tweepy_y']
tcollection = db['tweepy_t']

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tcollection.insert_one(status._json)
        print("===Inserted 1==")





myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['python', 'flask', 'cyrpto', 'btc', 'trump', 'india', 'green', 'bus', 'train', 'airplane'], async=True)
