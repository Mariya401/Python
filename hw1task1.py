"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

print("Ответьте, пожалуйста, на следующие вопросы:")
name = input("Введите ваше имя:")
password = input("Введите ваш пароль:")
age = int(input("Введите ваш возраст:"))
print(f"Ваше имя: {name}, Ваш пароль: {password}, Вам {age} лет")