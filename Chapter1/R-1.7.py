def sumoddsquares(n):
	return sum([x**2 for x in range(1,n,2)])

print(sumoddsquares(5))
print(sumoddsquares(1))
print(sumoddsquares(3))