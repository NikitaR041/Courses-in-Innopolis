'''
Написать программу, которая проверяет является ли число палиндромом. Палиндром - строка или число, которая читается одинаково, как слева направо, так и наоборот.

Например число 77
'''
print('Ввидете любое число, чтобы проверить является ли он полиндромом:')
a = input()
for i in range(len(a)):
    y = (i+1) #Так как, индексы начинаются с нуля,если считать слева направо
                #А, если считать справа на лево, то начинается -1, поэтому прибавляем +1 значение 
    if a[i] == a[-y]: # Индексы равны с началом и с концом(и последующие), если так, то проходит в блок 1, иначе во второй блок 
        print('Индекс:',i,'Yes')
    else:
        print('Индекс:',i,'No')

if a[:] == a[::-1]:
    print('ДА')
else:
    print('Дурак')
    
if a == a[::-1]:
    print('Da')
else:
    print('No')
