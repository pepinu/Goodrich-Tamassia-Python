def sumoddsquares(n):
	sum = 0
	for _ in range(1,n,2):
		sum += _**2
	return sum

print(sumoddsquares(5))
print(sumoddsquares(1))
print(sumoddsquares(3))