class Archive:
    """Создает класс Архив, который хранит свойства."""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Переопределяемый метод __new__ для создания экземпляра класс."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Мметод инициализации экземпляра класс."""
        self.number = number
        self.value = value

    def __repr__(self):
        return f'{self.numbers} {self.values}'

    def __str__(self):
        return f'Номер: {self.numbers} Значение: {self.values}'



if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, 'Два')
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, 'c')
    print(f'{a_3.numbers} {a_3.values}')

    help(Archive)