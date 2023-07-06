'''
Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''
SUBJECTS_FILE = 'items.csv'

class Text:

    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство {self.param_name} нельзя удалить')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} не является текстом.')
        if not value.istitle():
            raise AttributeError('Имя должно начинаться с заглавной буквы')
        if not value.isalpha():
            raise AttributeError('Имя должно состоять из букв')


class Item:

    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_item = '_' + name

    def __get__(self, object, object_type=None):
        return getattr(object, self.param_item)

    def __set__(self, object, value: dict):
        self.validate(value)
        setattr(object, self.param_item, value)

    def validate(self, value: dict):
        pass




class Student:
    first_name = Text(str.isupper)
    last_name = Text(str.isupper)
    evaluations = Item(2, 5 + 1)
    test = Item(0, 100 + 1)


    def __init__(self, last_name, first_name, evaluations: dict, test):
        self.last_name = last_name
        self.first_name = first_name
        self.evaluations = evaluations
        self.test = test

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



    def __str__(self):
        return f'{self.full_name} {self.evaluations} {self.test}'


if __name__ == '__main__':
    s = Student('Bванов', 'Bан', [2, 3, 4, 5, 5, 4], [20, 50, 30, 100])

    print(s)