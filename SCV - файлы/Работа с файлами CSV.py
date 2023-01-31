### тип данных CSV - табличный формат, ею пользуется google tzble, excel

'''
К примеру набираем овощи в корзинку, где сначала в списке пишем вес и цена

import csv
#Закидываем в csv-файл из пайтон программы
shop = {'Картошка':[2,100],'Яблоки':[3,250], 'Морковь':[1,35]} #В качестве ключа строка, а значение список, в котором говорим вес и цену
with open('file.csv','w',newline='') as file:#Открываем файл
                        #newline='' избавляет от лишней строки, попробуй посмотреть без этой команды
    a = csv.writer(file) # Создали переменную a - для записи в файл
    a.writerow(['Наименование','вес','цена за кг']) # записываем в одну строку, ОБЯЗАТЕЛЬНО В СПСИКЕ
    #Далее нужно записать shop в файл, см ниже
    shop = shop.items() # Превращает словарь в список, обязательно так делать
    #print(shop)
    for x,y in shop: # чтобы перебрать два элемента ключ и значение
        a.writerow([x,*y])#Все записывается в csv-файл
        
#Чтение в пайтон пррограмму из csv-файла
rows = []
with open('file.csv','r') as file:
    rdr = csv.reader(file) # Создаем объект для чтения!
    rows = list(rdr) # Приверащаем полученнные данные в список
print(rows)
'''

#Обычный вид

import csv

#Закидываем в csv-файд из Python-программу
shop = {'Картошка':[2,100],'Яблоки':[3,250], 'Морковь':[1,35]}
with open('file.csv','w',newline='') as file:
    a = csv.writer(file)
    a.writerow(['Наименование','вес','цена за кг']) 
    shop = shop.items()
    
    for x,y in shop:
        a.writerow([x,*y])
#Чтение в Python-пррограмму из csv-файла
rows = []
with open('file.csv','r') as file:
    rdr = csv.reader(file)
    rows = list(rdr) 
print(rows)

'''
Доп-задачка: Добавьте что-то свое в таблицу

shop = {'Картошка':[2,100],'Яблоки':[3,250], 'Морковь':[1,35]}
with open('file.csv','w',newline='') as file:
    a = csv.writer(file)
    a.writerow(['Наименование','вес','цена за кг']) 
    shop = shop.items()
    
    for x,y in shop:
        a.writerow([x,*y])

    a.writerow(['колбаса',3,250]]) #Добавить что-то свое, обязатеьно в функцию with

#Чтение в Python-пррограмму из csv-файла
rows = []
with open('file.csv','r') as file:
    rdr = csv.reader(file)
    rows = list(rdr) 
print(rows)
'''
#Домашка
'''
Написать программу - список дел. Нужно спросить у пользователя, скольких дел ты хочешь добавить?
Допустим, он ответил 5
Вы 5 раз должны спросить "введи дело" и сохранить в список
Затем Вы создаете текстовый файл и добавляете туда эти дела, но не все, а пропускаете каждое второе слова,
т.е. добавляете в файл только 1,3 и 5 дело в ОДНУ СТРОКУ

#проснуться
#улыбнуться
#покушать
#посмотреть сериал
#поспать

#проснутьсяпокушатьпоспать
'''
