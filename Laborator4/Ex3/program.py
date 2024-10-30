class Matrix:
    def __init__(self, rows, cols, fill=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(" numărul de coloane al primei matrice trebuie să fie egal cu numărul de rânduri al celei de-a doua matrice.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.set(i, j, sum(self.get(i, k) * other.get(k, j) for k in range(self.cols)))
        return result

    def transform(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


matrix1 = Matrix(2, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)

print(matrix1)
transposed = matrix1.transpose()
print(transposed)

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 1)
matrix2.set(0, 1, 2)
matrix2.set(1, 0, 3)
matrix2.set(1, 1, 4)
matrix2.set(2, 0, 5)
matrix2.set(2, 1, 6)

multiplied = matrix1.multiply(matrix2)
print(multiplied)

matrix1.transform(lambda x: x + 1)
print(matrix1)
