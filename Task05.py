# Задача:
# Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите число: '))

numbers = []
for i in range(n):
    numbers.append(random.randint(-n, n))
print(numbers)

def mixing(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = random.randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(mixing(numbers))