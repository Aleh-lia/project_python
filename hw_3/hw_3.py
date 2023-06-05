

'''
task 1
1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

print(f"{'':-^90}")
print('Задание 1')

myList = [9, 4, 1, 5, 9, 8, 4, 2, 7, 2, 9, 8, 5, 3]
res = []

for item in myList:
    count = 0
    for x in myList:
        if x == item:
            count += 1
    res.append(count)

duplicates = set()
i = 0
while i < len(myList):
    if res[i] != 1:
        duplicates.add(myList[i])
    i += 1

print(duplicates)

'''
task 2
2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

print(f"{'':-^90}")
print('Задание 2')

with open('text_hw3.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
limit = 10
dictionary = {}
res = {}
new_text = text.replace(',', '').replace('.', '').replace('!', '').replace('—', ''). \
                replace('?', '').replace('"', '').lower().strip()
words_list = new_text.split()
for word in words_list:
    counter = words_list.count(word)
    dictionary[word] = counter
sorted_values = sorted(dictionary.values())[::-1]
for i in sorted_values:
    for j in dictionary.keys():
        if dictionary[j] == i:
            res[j] = dictionary[j]
print(list(res.items())[0: limit])

'''
task 3
3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

print(f"{'':-^90}")
print('Задание 3')

backpack = int(input('Введите грузоподъемность рюкзака: '))

things_to_hike = {'Обувь': 1.5,
                    'Вода': 2,
                    'Палатка': 2,
                    'Компас': 0.2,
                    'Одежда': 5,
                    'Горелка': 3,
                    'Аптечка': 0.7,
                    'Топор': 1.2,
                    'Еда': 3,
                    'Спальник': 1}


def sort_list(some_set: set):
    global global_list
    if len(some_set) == 1:
        return some_set
    else:
        for i in some_set:
            new_set = some_set.copy()
            new_set.remove(i)
            global_list.add(tuple(sort_list(new_set)))
    return some_set


things_to_hike = dict(sorted(things_to_hike.items(), key=lambda x: x[1]))
global_list = {tuple(things_to_hike)}
sort_list(set(things_to_hike))

print(f'В рюкзак грузоподъемностью {backpack}кг может влезть:')

for stack in global_list:
    summ_stack = 0
    for i in stack:
        summ_stack += things_to_hike.get(i)
        if summ_stack > backpack:
            break
    else:
        print(*stack, ': весом', summ_stack, 'кг')

def sort_list(some_set: set):
    global global_list
    if len(some_set) == 1:
        return some_set
    else:
        for j in some_set:
            new_set = some_set.copy()
            new_set.remove(j)
            global_list.add(tuple(sort_list(new_set)))
    return some_set
