import tweepy, time, sys, datetime

class BotInfo:

    #bot settings to look more human
    def __init__(self):
        #account info
        self.USERNAME = "NormanRoss04"
        self.CASHAPP = "NormanRoss04"

        #search settings
        self.TWEET_SEARCH_LIMIT = 25
        self.SEARCH_TIMER = 17 * 60
        self.LIKE_RETWEET_ONLY_TIMER = 15 * 60
        self.TWEET_LIMIT_PER_SEARCH = 5
        self.RUNS_BEFORE_SWITCH = 4
        self.OVERFLOW_SEARCH_REPEAT = 3
        self.OVERFLOW_EXTRA_SEARCHES = 20

        #limits before removing old tweets or likes
        self.TWEET_LIMIT = 3000
        self.TWEET_RESET_LIMIT = 1000
        self.FRIEND_LIMIT = 1901
        self.FRIEND_RESET_LIMIT = 1400

        #dates
        self.GO_BACK_TIME = 5
        self.DELETE_DATE = datetime.datetime.utcnow() - datetime.timedelta(days=self.GO_BACK_TIME)

        #counters
        self.total_tweets_since_start = 0

    consumer_key = 'rh49Ko8HT6xTosu75FlARoRVG'
    consumer_secret = 'j7iQQJ5MKoqizW2eyfn1Z4KBk7Qb59C4VHG7bwAel4OiZe5kqJ'
    access_token = '1711405795-SZogLj2487SkoDgk4c4cjePOWhHHL1K5NkL8jeF'
    access_token_secret = '1HhsiuTs25wFyTI832M1ItnYIrzUOsF6VLXex8QK6FbrO'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #number of days to go back in time for the search date
    goBackTime = 0
    date_since = (datetime.datetime.now() - datetime.timedelta(days=goBackTime)).date()
    print(date_since)

    #defines search terms
    tag_list = ["Segga86", "SYM_Persian", "CHRISTYSWEENEY1", "WippydeeWaen", "peppers_jay", "Crayola888", "Goog1234Hey", "Molex2_5"]
    search_words = ["retweet to win", "retweet giveaway", "cashapp retweet giveaway", "steam giveaway retweet"]
    filtered_words = ["bot", "b0t", "comment", "screenshot", "proof", "sugar", "sugardaddy", "sugarbaby", "robux", "sugar baby", "sugar momma", "porn", "roblox", "sex", "fortnite", "vbucks"]
    filtered_users = ["bot", "b0t", "spotter", "sp0tter", "followandrt2win", "muckzuckerburg", "retweeejt"]
