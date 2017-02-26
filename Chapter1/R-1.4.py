def sumsquare(n):
	result = 0
	for _ in range(1,n):
		result += _**2
	return result

print(sumsquare(5))
print(sumsquare(1))
print(sumsquare(3))