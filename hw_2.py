import fractions

# task 1
'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

print(f"{'':-^90}")
print('Задание 1')

num = int(input('Введите число: '))
h = hex(num)

digits = '0123456789ABCDEF'
hexad = 16
res = ""
while num > 0:
    res = digits[num % hexad] + res
    num = num // hexad

print(res)
print()
print('Проверка с помощью функции hex:', h[2:])


# task 2
'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
'''


print(f"{'':-^90}")
print('Задание 2')

num1 = fractions.Fraction(input('Введите первую дробь вида a/b : '))
num2 = fractions.Fraction(input('Введите первую дробь вида a/b : '))

result1 = num1 + num2
result2 = num1 * num2
print(f'{num1} + {num2} =', result1)
print(f'{num1} * {num2} =', result2)
