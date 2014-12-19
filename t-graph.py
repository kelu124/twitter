#!/usr/bin/python
import sys
from urllib2 import urlopen
import bs4 as BeautifulSoup
import urllib2
# Requis pour MySQL connection
# Requis pour MySQL connection
import MySQLdb
from tecpass import * 
import string
import re


# USAGE 
# python graph.py > ./Bureau/graph.gdf

cursor=db.cursor()


query = ("SELECT tWho, tWhat FROM tweets ")

cursor.execute(query,)
result = cursor.fetchall()	

# let's clean the data 
paireds = []
tHList = []
tUsers = []
tHashes = []
i = 0
for row in result:
	# for bugbs in my mysql dump due to bad retweets
	 
	usered = row[0].lower()
	tmp = string.replace(row[1], 'RT ', 'RT @') 
	tmp = string.replace(tmp, '@@', '@')
	tmp = tmp.lower()
	users = []
	users = re.findall("@\w+", tmp)
	
	tHashers = re.findall("#\w+", tmp)
	users.append(usered)
	
	users = users + tHashers 
	tHashes.append(tHashers)
	#print users
	paireds.append(users)
	#paireds.append(tHashers)

	i = i +1 
	tUsers.append(usered)
	tHList = tHList + tHashers

#print paireds
#print tUsers
tUserUnique = []
[tUserUnique.append(item) for item in tUsers if item not in tUserUnique]
tH = []
[tH.append(item) for item in tHList if item not in tH]
#print tUserUnique

print 'nodedef> name VARCHAR,label VARCHAR'
for user in tUserUnique:
	print "%s, %s" % (user, user)
for user in tH:
	print "%s, %s" % (user, user)

print 'edgedef> node1 VARCHAR,node2 VARCHAR'
for seque in paireds:
	l = len(seque)
	#print seque
	#print l
	if l>1:
		L = 0
		while L < l-1:
			#print L
			#print seque[L]
			#print seque[b]
			LL = L + 1
			
			while LL < l:
				print "%s, %s" % ( seque[L], seque[LL] )
				LL = LL + 1
			L = L+ 1
	


cursor.close()
db.close()
