#!/bin/python3

import sys

def pangram(s):
	s="We promptly judged antique ivory buckles for the next prize"
	li=[]
	j=0;
	for i,ch in enumerate(s):
		if ch not in li:
			li.append(ch)
			j=j+1
	print j
	if j >= 26
		return "pangram"
	else
		return "not pangram"
		
s = raw_input().strip()
result = pangram(s)
print(result)
