from time import time


class MyString(str):
    """Создайте класс Моя Строка, где: будут доступны все возможности str дополнительно хранятся имя автора строки и время создания."""

    def __new__(cls, value: str, name: str):
        '''Расштиряемый метод str с параметрами value и name.'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time()
        return instance

    def __repr__(self):
        return f'{self.name}, {self.created_at}'

    def __str__(self):
        return f'Cтрока: {self.name} Время: {self.created_at}'



if __name__ == '__main__':
    mystr = MyString('Cама строка', 'доп. параметр')

    print(mystr)
    print(f'{mystr = }')
    print(mystr.upper())

