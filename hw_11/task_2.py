class Matrix:
    """Класс матрица с инициализацией списка списков."""

    def __init__(self, list_of_lists: list[list[int]]):
        """Инициализация инит с аргументом list[list[int]]."""

        self.list_of_lists = list_of_lists

    def __str__(self):
        """Вывод списка построчно."""

        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __add__(self, other):
        """Переопределил метод поэлементного сложения матриц."""

        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __sub__(self, other):
        """Переопределил метод поэлементного сложения матриц."""

        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] - other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        """Умножения матриц."""
        m = len(self.list_of_lists)
        n = len(other.list_of_lists)
        k = len(other.list_of_lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list_of_lists[i][k] * other.list_of_lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 6], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_sub = matrix_1 - matrix_2
    print(matrix_sub)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
