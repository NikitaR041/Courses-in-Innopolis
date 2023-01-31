##Промежуточная аттестация
'''
Реализовать программу, которая принимает на вход числа a, b.
Результатом работы должно быть среднее значение всех чисел от a до b включительно, которые делятся на 3, среднее значение находится, как сумма чисел разделенное на количество.
'''
print('Введите два числа: ')
a,b = map(int,input().split())
m = []
for i in range(a, b + 1):
    if i % 3 == 0:  
        m.append(i)
srd = sum(m)/len(m)
print('Среднее значение: ', srd)
##
a,b = map(int, input().split())
summa = 0
amount = 0
arifmatic = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        summa+=i
        amount+=1
arifmatic = summa / amount
print(arifmatic)
