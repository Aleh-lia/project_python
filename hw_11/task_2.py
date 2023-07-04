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
        """Cложения матриц."""

        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __sub__(self, other):
        """Вычитания матриц."""

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

    def __eq__(self, other) -> bool:
        """Сравнения матриц."""
        return True if self.list_of_lists == other.list_of_lists else False


if __name__ == '__main__':
    matrix_1 = Matrix([[9, 8, 6], [5, 6, 3], [1, 3, 7]])
    matrix_2 = Matrix([[3, 4, 6], [3, 5, 7], [1, 9, 8]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_sub = matrix_1 - matrix_2
    print(matrix_sub)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    if matrix_3 == matrix_4:
        print('True')
    else:
        print('False')

    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')
