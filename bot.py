import tweepy
import gpt_2_simple as gpt2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

    api = getAPI()
    account = "Add account to reply to here"
    tweets = api.user_timeline(screen_name=account, count='20', tweet_mode='extended')
    
    model = gpt2.start_tf_sess()
    gpt2.load_gpt2(model, run_name="run1")
    
    analysis = SentimentIntensityAnalyzer()

    keywords = [["keyword", 0]] #input keywords and bot's position on them (1 to agree, -1 to disagree)
    
    for tweet in tweets:
        tweet_id = tweet.id
        tweet = tweet.full_text
        sentiment = analysis.polarity_scores(tweet).get("compound")
        accepted = 0
        print(tweet + "        " + str(tweet_id) + "\n")
        for keyword in keywords:
            if (tweet.find(keyword[0]) != -1):
                if (sentiment * keyword[1] >= 0):
                    while (accepted == 0):
                        reply = gpt2.generate(model, prefix="<>I love that " + keyword[0], temperature=0.9, return_as_list=True, length = 70)[0]
                        reply = reply.split("<>")[1]
                        print(reply + "\n")
                        if (input("y if acceptable, n to regenerate  ") == "n"):
                            accepted = 0
                        else:
                            accepted = 1
                            break
                else:
                    while (accepted == 0):
                        reply = gpt2.generate(model, prefix="<>I hate that "  + keyword[0], temperature=0.9, return_as_list=True, length = 70)[0]
                        reply = reply.split("<>")[1]
                        print(reply + "\n")
                        if (input("y if acceptable, n to regenerate  ") == "n"):
                            accepted = 0
                        else:
                            accepted = 1
                            break
        
        print("final: " + reply + "\n")
        api.update_status(reply, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
    

if __name__ == '__main__':
    run()

