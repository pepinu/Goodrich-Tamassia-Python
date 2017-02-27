def isoddpair(seq):
	if isinstance(seq, list) and len(seq) > 1:
		cnt = 2
		for _ in seq:
			if cnt == 0:
				return "Yes"
			elif _ & 1:
				cnt -= 1 
		return "No"

	else:
		return "This is not a sequence"

print(isoddpair([1, 2]))
print(isoddpair([1]))
print(isoddpair(1))
print(isoddpair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))