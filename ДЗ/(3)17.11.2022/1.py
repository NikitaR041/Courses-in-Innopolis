'''
Напишите программу,  которая спрашивает у пользователя ввести число и выводит факториал данного числа.

Пример факториал числа 5! = 1 х 2 х 3 х 4 х 5
'''
print('Введите число: ')
x = int(input())
s = 1
if x > 0 :
    for i in range(1,x+1):
        s = s * i
print('Ваш факториал числа ',x, 'равно ', s)
