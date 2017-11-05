import sys

def breakdown(line):
	letters={}
	for n in line:
		if n not in letters and n.isalpha():
			letters[n.lower()]=1
		elif n in letters:
			letters[n.lower()]+=1
	keys = sorted(letters.keys())
	for key in keys:
		print(key,letters[key])

breakdown('hello friendo ``123')
