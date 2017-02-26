import collections
from random import randrange as rr

def choice(n):
	if isinstance(n, collections.Sequence):
		return n[0] if len(n) == 1 else rr(n[0], n[-1])
	else :
		return "This is not a sequence"

print(choice([10,2000]))
print(choice(1))
print(choice([10]))

