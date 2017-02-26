def minmax(data):
	if isinstance(data, list):
		min, max = data[0], data[0]
		for _ in data:
			if min > _ :
			    min = _
			if max < _ :
				max = _
		return (min, max)
	else:
	    return (data, data)


print(minmax(1))
print(minmax([1,2,3,4,2,6,9,1]))