class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        try:
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[i])):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(self.matrix)
        except IndexError:
            return f'Ошибка!!! Матрицы должны быть одинаковый длины'


matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_2 = Matrix([[1, 3, 23], [24, 0, 5], [-4, 3, -5]])
matrix_3 = Matrix([[8, 1, 15], [23, 1, 2], [-2, 5, -5]])
matrix_4 = Matrix([[8, 1, 15], [23, 1, 2], [-2, 5, -5]])
print(matrix_1 + matrix_2 + matrix_3 + matrix_4)
