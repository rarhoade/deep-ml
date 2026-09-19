import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m = len(a)
	n = len(a[0])
	if (new_shape[0] != n or new_shape[1] != m):
		if new_shape[0] != m or new_shape[1] != n:
			return []
	reshaped_matrix = []
	for c in range(n):
		reshaped_matrix.append([0] * m)
	
	i = 0
	j = 0
	b = 0
	c = 0
	while i < m:
		while j < n:
			reshaped_matrix[b][c] = a[i][j]
			c = c + 1
			if c >= m:
				c = 0
				b = b + 1
			j = j + 1
		j = 0
		i = i + 1

	return reshaped_matrix