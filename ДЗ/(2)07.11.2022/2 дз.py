'''
Напишите программу, которая выводит чётные числа из заданного списка и останавливается,
если встречает число 237.
'''
a = [1,3,5,7,9,0,13,2,4,6,8,1,12,14,18,20,10,237,2,3,5]
for i in a:
    if i % 2 == 0 and i != 237:
        print(i)
