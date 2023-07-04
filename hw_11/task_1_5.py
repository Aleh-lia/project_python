

class Rectangle:
    """Создает класс прямоугольник."""

    def __init__(self, a: int, b: int = None):
        """Мметод инициализации экземпляра класс."""
        self.a = a
        self.b = b if b is not None else a


    def area(self) -> int:
        """Площадь прямоугольника."""

        return self.a * self.b

    def perimeter(self) -> int:
        """Периметр прямоугольника."""

        return 2 * self.a + 2 * self.b

    def __add__(self, other):
        """Сложение прямоугольников."""

        new_perimeter = self.perimeter() + other.perimeter()
        new_a =self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        """Вычитание прямоугольников."""

        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a =min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __repr__(self):
        return f'{self.perimeter()} {self.area()}'

    def __str__(self):
        return f'Пиреметр: {self.perimeter()} Площадь: {self.area()}'


if __name__ == "__main__":
    rect1 = Rectangle(2, 5)
    rect2 = Rectangle(5, 10)

    print(f'{rect1.perimeter() = }, {rect1.area() = }')

    print(rect2)

    res_sum = rect1 + rect2
    print(res_sum.a, res_sum.b)
    res_sub = rect1 - rect2
    print(res_sub.a, res_sub.b)