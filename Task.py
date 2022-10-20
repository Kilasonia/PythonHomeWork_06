# Формат: Объясняет преподаватель

# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента






# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from itertools import accumulate
import operator

n = int(input('Enter a number : '))


def get_prods(N):
    return list(accumulate([x for x in range(1, n + 1)], operator.mul))


print(get_prods(n))






# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('Enter a number: '))


# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range(1, n + 1)]


# numbers = get_squerence(n)
# print(numbers)
# print(round(sum(numbers), 5))
