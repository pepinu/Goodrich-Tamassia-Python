def dotproduct(a, b, n):
	if isinstance(a, list) and isinstance(b, list):
		c = [0] * n
		for _ in range(n):
			c[_] = int(a[_]) * int(b[_])
		return c
	else:
		return "This is not a sequence"

print(dotproduct([1, 2, 3, 4], [4, 3, 2, 1], 4))
print(dotproduct([1.2, 1.3], [3.1, 4.4], 2))
print(dotproduct(2, 1, 1))
