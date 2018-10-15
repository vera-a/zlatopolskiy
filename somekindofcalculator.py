from math import *
num1 = input("Первое число: ")
num2 = input("Второе число: ")
operation = input('Выберите операцию – умножение, деление, возведение в степень, целочисленное деление или вычитание: ')
if operation == 'умножение':
    print(float(num1) * float(num2))
elif operation == 'деление':
    print(float(num1) / float(num2))
elif operation == 'возведение в степень':
    print(pow(float(num1), float(num2)))
elif operation == 'сложение':
    print(float(num1) + float(num2))
elif operation == 'вычитание':
    print(float(num1) - float(num2))
elif operation == 'целочисленное деление':
    print(float(num1) % float(num2))
elif operation == 'квадратный корень':
    print(sqrt(float(num1)))
