import os
import tweepy as tw
import pandas as pd
import re
import csv
import json


consumer_key = 'nbQQrucJZi1JSPT8G3zVFR77z'
consumer_secret = 'f7xFboiaPa8Ljcg7OaKJPFDu0CsPFUjjH7sKPaJAPVQzf1KLpP'
access_token = '846238461258551296-JyV4cj0RO3weeQyPCQGorgQjNetCsMS'
access_token_secret = 'gxAN1KAJw9A5zaeDUbGHd4d0gPjxFdTHCxypXzWwoX6zS'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = ["Canada","University","Dalhousie University","Halifax","Canada Education"]

happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])
sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])

emoticons = happy.union(sad)
emojiptn = re.compile("["
         u"\U0001F600-\U0001F64F"  
         u"\U0001F300-\U0001F5FF"  
         u"\U0001F680-\U0001F6FF"  
         u"\U0001F1E0-\U0001F1FF"  
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)


i=1


for words in search_words:
    tweets = tw.Cursor(api.search,
              q=words,
              lang="en",
              ).items(3500)
    for tweet in tweets:
        tweet_text = re.sub(r':', '', tweet.text)
        tweet_text = re.sub(r'‚Ä¶', '',  tweet_text)
        tweet_text = re.sub(r'[^\x00-\x7F]+', ' ',  tweet_text)
        tweet_text = emojiptn.sub(r'',  tweet_text)
        tweet_text = re.sub(r'http\S+', '',  tweet_text)
        for k in tweet_text.split("\n"):
            tweet_text =re.sub(r"[^a-zA-Z0-9]+", ' ', k)


        print(tweet_text)
        with open('tweet_text.txt', mode='a', encoding="utf-8") as txt_file:
            txt_file.write(tweet_text+"\n")

        with open('tweetextracted.csv', mode='a',encoding="utf-8") as csv_file:
            fieldnames = ['id', 'tweet_text', 'tweet_created','source','favorite_count','retweet_count']
            fieldnames1 = [tweet.id, tweet_text, tweet.created_at,tweet.source,tweet.favorite_count,tweet.retweet_count]


            if i == 1:
                writer = csv.writer(csv_file, lineterminator='\n')
                writer.writerow(fieldnames)
                writer.writerow(fieldnames1)

                i = i + 1
            else:
                writer = csv.writer(csv_file, lineterminator='\n')
                writer.writerow(fieldnames1)

        csv_file.close()
        txt_file.close()



