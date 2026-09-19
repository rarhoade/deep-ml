def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
			
	m = len(b)
	if len(a) > 0:
		if m != len(a[0]):
			return -1
	product = []
	for column in a:
		if len(column) != m:
			return -1
		i = 0
		total = 0
		while i < m:
			total = total + (column[i] * b[i])
			i = i + 1
		product.append(total)
	return product
	pass