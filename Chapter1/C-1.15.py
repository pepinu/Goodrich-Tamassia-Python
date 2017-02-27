def alldistinct(seq):
	if isinstance(seq, list) and len(seq) > 1:
		x = set(seq)
		if len(x) == len(seq):
			return "All elements are distinct"
		else:
			return "The sequence contains duplicates"
	else:
		return "This is not a sequence"


print(alldistinct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(alldistinct([1,2,3,4,3,5,2,1]))
print(alldistinct([1,1]))
print(alldistinct([1]))
print(alldistinct(1))