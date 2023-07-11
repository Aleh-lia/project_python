from custom_exception import NegativeSideError, ZeroSideError

class Rectangle:
    """Создает класс прямоугольник."""

    def __init__(self, a: int, b: int = None):
        """Мметод инициализации экземпляра класс."""

        if a >= 0: #Сделано так для реализации класса ZeroSideError
            self.a = a
        else:
            raise NegativeSideError(f'a = {a}')
        if b >= 0:
            self.b = b if b is not None else a
        else:
            raise NegativeSideError(f'b = {b}')
        if a == 0:
            raise ZeroSideError(a)
        if b == 0:
            raise ZeroSideError(b)




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
    rect1 = Rectangle(5, 0)
    rect2 = Rectangle(5, 10)

    print(f'{rect1.perimeter() = }, {rect1.area() = }')

