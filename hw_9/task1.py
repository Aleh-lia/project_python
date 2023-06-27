'''
1.Решить задачи, которые не успели решить на семинаре.
    Напишите следующие функции:
        Нахождение корней квадратного уравнения
        Генерация csv файла с тремя случайными числами в каждой строке.
    100-1000 строк.
        Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
        Декоратор, сохраняющий переданные параметры и результаты работы
    функции в json файл.
'''
import math
from typing import Callable
import csv
from random import randint
import json
import os.path
import datetime



def deco_csv(func: Callable):
    create_csv()

    def wrapper() -> object:
        with open('equation_sqr.csv','r', encoding='UTF-8') as file_sqr:
            data = csv.reader(file_sqr, quoting=csv.QUOTE_NONNUMERIC)
            for numb in data:
                if numb and numb[0] != 0:
                    func(*numb)

    return wrapper



def deco_json(func: Callable):
    res = {}
    if os.path.exists(f'{func.__name__}.json'):
        with open(f'{func.__name__}.json', 'r', encoding='UTF-8') as file_json:
            res = json.load(file_json)

    def wrapper(*args):
        result = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': result}
        res_key = f'{datetime.datetime.now()}'[:-7]
        res[res_key] = res.get(res_key) + [solve_dict] \
            if res.get(res_key) \
            else [solve_dict]
        with open('json_result.json', 'w', encoding='UTF-8') as file_json:
            json.dump(res, file_json, indent=2)
        return result

    return wrapper




def create_csv():
    with open('equation_sqr.csv', 'w', encoding='UTF-8') as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(randint(1, 10)):
            writer.writerow([randint(-100, 100), randint(-100, 100), randint(-100, 100)])



@deco_csv
@deco_json
def equation_sqr(*args) -> tuple | float | None:
    a, b, c = args
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('корней нет')
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        print(f'один корень x = {x1}')
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f'корней будет два {x1}, {x2}')


equation_sqr()
