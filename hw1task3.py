"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

print("Введите число:")
n = input()
print(n + n)
print(n + n + n)
res = (int(n) + int(str(n + n)) + int(str(n + n + n)))
print(f"Сумма чисел: {n} + {n + n} + {n + n + n} = {res}")
