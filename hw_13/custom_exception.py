'''
Задание №3
📌 Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
'''

class CustomException(Exception):
    pass


class NegativeSideError(CustomException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Сторана прямоугольника не может быть меньше 0, а вас сторана {self.value}'


class ZeroSideError(CustomException): #Этот класс сделан для тренировки
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Сторана прямоугольника не может быть равна 0'