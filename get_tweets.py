import tweepy

CONSUMER_KEY = "add consumer key here"
CONSUMER_SECRET = "add consumer secret here"

ACCESS_TOKEN = "add access token here"
ACCESS_SECRET = "add access secret here"


# Sets up the Twitter API
def getAPI():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    return api

def run():
    training = open("training2.txt", 'a')
    api = getAPI()
    account = "___specify twitter handle here___"
    tweets = api.user_timeline(screen_name=account, count='500', tweet_mode='extended') #specify number of tweets here by changing the value of 'count'
    for tweet in tweets:
        if (tweet.full_text.startswith("RT")):
            print("retweet")
            i = 2
            while (tweet.full_text[i] != ':'):
                i = i + 1
            print("<> " + tweet.full_text.split("https")[0][(i + 2):])
            training.write("<> " + tweet.full_text.split("https")[0][(i + 2):] + "\n")
        #print(str(tweet.full_text[0]))
        else:
            print("<> " + tweet.full_text.split("https")[0])
            training.write("<> " + tweet.full_text.split("https")[0] + "\n")
    training.close()

if __name__ == '__main__':
    run()