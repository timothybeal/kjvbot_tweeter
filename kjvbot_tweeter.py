'''
Created on Apr 11, 2016

@author: timothybeal

Builds its utterance as a Markov chain based on a randomly 
selected series of three start words and a selection from the KJV 
Bible (prophets, Gospels, or Revelation, or the whole KJV) and then, 
if it is <= 130 characters, tweets it to @KJVBot.
'''

import markovbot
from random import choice

w = ["the", "them", "thee", "him"]
l = ["looked", "saw", "beheld", "heard"]
x = [["Woe", "unto", choice(w), "kjv_prophets.txt"], 
     ["And", "the", "priest", "kjv.txt"], 
     ["And", "I", choice(l), "kjv_revelation.txt"], 
     ["Behold", ",", "I", "kjv.txt"], 
     ["And", "to", "the", "kjv_revelation.txt"], 
     ["And", "he", "answered", "kjv_gospels.txt"],
     ["In", "the", "beginning", "kjv.txt"]]

[word1, word2, word3, fileid] = choice(x)

utterance = markovbot.markovize(word1, word2, word3, fileid, char_limit=125)
tweet = '"' + utterance + '"'
tweet_len = len(tweet)

# twitter api keys and secrets (get these for your account at apps.twitter.com)
consumer_key = 'dnz75t8CWUC5znIce3gWmQ0a2'
consumer_secret = '83Sk8bT5vVLloadULrgWPbTrEcjxpTW64Fb7WW7QN2cvO4AHMB'
access_key = '4467417379-SBJb28RkD9RX0E7DwCdYTMrLxuymFpbqrL6HATk'
access_secret = 'cDkNn0Hj9GzmAEiMYQJ1rCrbkhBWAPWG8BnlR2Pn6lIEo'  

# call function to tweet utterance    
print(tweet, '\n', tweet_len)
markovbot.post_tweet(consumer_key, consumer_secret, access_key, access_secret, tweet)