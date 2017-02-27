def countVowels(seq):
	if isinstance(seq, str):
		s = set(["a", "e", "i", "o", "u"])
		vowels = 0
		for _ in seq:
			if _ in s:
				vowels += 1
		return vowels

	else:
		return "This is not a string"


print(countVowels("This is not a sequence"))
print(countVowels("aeiou"))
print(countVowels(""))
print(countVowels([1, 2, 3]))
print(countVowels(5))