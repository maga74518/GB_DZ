'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
return sum(a, b) + 1 - такое использовать нельзя'''

def sum_1(x, y):
    return x if y == 0 else sum_1(x+1, y-1)

print(sum_1(int(input()), int(input())))