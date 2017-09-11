#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function

#	s = "AAA"
	j=0
	n = len(s)
	n = n - 1	
	print "Length = ",n
	for ind,ch in enumerate(s[:-1]):
	#	print ind," ",len(s)
		if(ch == s[ind+1]):
			j=j+1
	#		print s
	return j

q = int(raw_input().strip())
for a0 in range(q):
	s = raw_input().strip()
	result = alternatingCharacters(s)
	print(result)
