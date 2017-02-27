import sys

def reverseInput():
	seq = []
	for line in sys.stdin:
		seq.append(line.strip('\n'))
	return seq[::-1]

print(reverseInput())

