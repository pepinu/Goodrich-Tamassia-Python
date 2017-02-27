import random

def shuffle(data):
	if isinstance(data, list):
		l = len(data)
		for _ in range(l):
			ch = random.randint(0,l-1)
			data[_], data[ch] = data[ch], data[_]
		return data
	else:
		return "This is not a sequence"



print(shuffle([1, 2, 3,4]))
print(shuffle([1]))
print(shuffle(1))
print(shuffle([1, 2, 3, 4, 5, 6]))