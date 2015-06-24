#! /usr/bin/python

import sys
import re
total = 0
urlString = ""
myUrls = {}
def processFile(filename):
	tmptotal = 0
	pos = 0
	line = filename.readline()
	while line :
		try : 
			if line.split()[0] == "POS_SIDER":
				pos = line.split()[1]
				break
		except : pass
		line = filename.readline()
	pos = int(pos)
	filename.seek(pos)
	urls = int(filename.readline().split()[1])
	for i in range(1,urls):
		tmptotal = 0
		lineArray = filename.readline().split()
		validURL =  re.match(r'/labs/[a-z]+[0-9]+/exp[0-9]+/$',lineArray[0])
		if validURL != None :
			
			tmptotal += int(lineArray[1])
			myUrls[lineArray[0]] = tmptotal

for i in sys.argv[1:]:
	awfile = open(i)
	processFile(awfile)
	for key in sorted(myUrls.keys()):
		print key,myUrls[key]
