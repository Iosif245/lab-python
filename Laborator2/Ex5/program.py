def replace_below_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(min(i, cols)):
            matrix[i][j] = 0

    return matrix

print (replace_below_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]))