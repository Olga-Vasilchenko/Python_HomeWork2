# Задача:
# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите количество чисел в списке: '))

def numb(n):
    sum = 0
    
    for i in range(n):
        a = int(input(f'Введите число {i + 1}) '))
        a = (1 + 1/a) ** a
        sum = a + sum
        i += 1
    return sum

print('Сумма чисел равна =', round((numb(n)), 2))