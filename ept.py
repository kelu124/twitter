#echOpen processing tweets
#usage : python ept.py tweets.tsv > graph.gdf

from math import *
import sys
import string
import re
import unicodedata

try:
    sys.argv[1]
except NameError:
    eptFile = 'Missing an arg'
else:
    eptFile = sys.argv[1]

paireds = []
tHList = []
tUsers = []
tHashes = []
i = 0

with open(eptFile, 'r') as Tweets:
	for line in Tweets:
		line = unicode(line,'utf-8')
		line = unicodedata.normalize('NFD', line).encode('ascii', 'ignore')     
		line = line.split('\t')
		del line[-1]
		#print line

		usered = line[1].lower()

		tmp = line[2].lower()
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
	


