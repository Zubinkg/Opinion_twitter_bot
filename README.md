# Opinion Twitter Bot

This project is a Twitter bot meant to generate retweets to opinionated tweets that reflect a certain point of view on something. This is achieved by training a natural language generation neural network on tweets retrieved via the twitter API. The user can then input tweets which are analyzed for their sentiment and for predefined keywords and can choose between automatically generated responses which will then be posted to Twitter.

## Setup

First, apply for a twitter developer account. This will be necessary to create a twitter bot, and several keys are necessary for interacting with the API.

Before any tweets can be generated or the neural network can be trained, a library of training data must be compiled. To do this, enter your account keys into get_tweets.py and specify a twitter user and the number of tweets to pull from their account. When run, get_tweets.py will retrieve the most recent specified number of tweets from the users account and append it to the end of training.txt. For the purpose of this bot, it is useful to collect several thousand strongly opinionated tweets with a low density of non-text items (i.e. urls, emojis) from a selection of accounts.

Next, run training.txt to tune a gpt2 language model to the retrieved tweets. The step value for the model can be reduced to speed up the training process, but may result in less coherent results.

Finally, enter your account keys into bot.py and create a list of keywords that the bot will respond to. Each keyword consists of a string and a value representing the bot's opinion of the string. For instance, if the bot should disagree with Bob for any given tweet, the keyword should be ["Bob", -1]. Keep in mind that keywords earlier in the array will be given priority over later keywords. Next, add the username of an account you want to create responses to and replace the 'count' value with the number of tweets you want to respond to. Now, when run, bot.py will retrieve recent tweets and suggest a response for each tweet, assuming a keyword is found in it. If the response is not suitable, you may press n to generate a new response until a suitable one is found. Otherwise, the response will be retweeted to the tweet in question.
