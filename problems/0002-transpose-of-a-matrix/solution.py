def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    m = len(a)
    n = len(a[0])
        
    i = 0
    j = 0
    # m x n => n x m
    transpose = []
    while i < n:
        column = []

        while j < m:
            print(j, i, a[j][i])
            column.append(a[j][i])
            j = j + 1
        j = 0
        transpose.append(column)
        i = i + 1
    return transpose

    # Your code here
    pass