#!/usr/bin/python
import sys
from TwitterSearch import *
# Requis pour MySQL connection
# Requis pour MySQL connection
import MySQLdb
from datetime import datetime
import os


from tecpass import * 

    
def remo_na(text):
    return ''.join(i for i in text if ord(i)<128)



cursor=db.cursor()

add_tweet = ("INSERT INTO tweets "
               "(tWho, tWhat, tDate, tUID) "
               "VALUES (%s, %s, %s, %s)")

# USAGE
# python patent.py US3541840 US3714817 US3864660

try:
    tuo = TwitterUserOrder('echopenorg') # create a TwitterUserOrder


    # it's about time to create a TwitterSearch object with our secret tokens


    for tweet in ts.search_tweets_iterable(tuo):
        twText = " "
	twText = remo_na(tweet['text'])

	twID = tweet['id']
	#print '%s' % tweet['created_at']
	tWho = '@' + tweet['user']['screen_name']
	created = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

	query = ("SELECT tID FROM tweets "
	"WHERE tUID LIKE %s ")
	numrows = cursor.execute(query, twID)
	if not(numrows): # (tWho, tWhat, tDate, tUID) 
		data_tweet = (tWho.decode('unicode_escape').encode('ascii','ignore'), twText.encode('ascii', 'ignore'), created, twID )
		cursor.execute(add_tweet, data_tweet)
	if numrows:
		print "Tweet deja enregistre"




except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

		





db.commit()
cursor.close()
db.close()

