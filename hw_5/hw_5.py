'''
1.
2.
3.
'''

'''
task 1
    Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
print(f"{'':-^90}")
print('Задание 1')


def to_share(path: str) -> tuple[str, str, str]:
    way, _, file_name = path.rpartition('\\')
    file_name, _, file_exp = file_name.rpartition(".")
    print('путь к файлу -- ', way)
    print('имя файла -- ', file_name)
    print('расширение файла --', file_exp)



to_share("K:\GeekBrains\Python Web Development\Immersion in Python\project_python\hw_5.py")

'''
task 2
    Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь 
с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная 
на процент премии
'''
print(f"{'':-^90}")
print('Задание 2')

NAMES = ["Иван", "Александр", "Евгений", "Андрей"]
BET = [1_000, 2_300, 1_500, 3_000]
PERCENTS = ["10.25%", "7.00%", "20.00%", "30.00%"]


def gen_dict(names: list[str], bet: list[int], percents: list[str]):
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, bet, map(lambda x: float(x[:-1]), percents))))}
    return


def main():
    print(*gen_dict(NAMES, BET, PERCENTS))


if __name__ == "__main__":
    main()




'''
task 3
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
'''
print(f"{'':-^90}")
print('Задание 3')

FIB_SET = (5, 8, 10, 15)


def fib_gen(n: int) -> list[int]:
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    for n in FIB_SET:
        print(*fib_gen(n))


if __name__ == "__main__":
    main()