def outOfBounds(seq,n):
	if isinstance(seq, list):
		try:
			return seq[n]
		except IndexError:
			return "Don't try buffer overflow attacks in Python!"
	else:
		return "This is not a sequence"


print(outOfBounds([1,2,3], 1))
print(outOfBounds([1,2,3], 7))
print(outOfBounds(1,2))