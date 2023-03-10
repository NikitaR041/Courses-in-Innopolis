'''
Перед тем как изучать модули нужно помнить классы
'''
#Вспоминаем
# наследование
# полиморфизм
# инкапсуляция
'''
class Animal:
    def __init__(self,name): # Инициализация
        self.__name = name # Инкапсуляция
    def say_about_me(self): # Полиморфизм
        print("Я объект класса Animal")

class Dog(Animal):
    def bark(self):
        print("Гав Гав ГАв")
    def say_about_me(self): #Переопределение - полиморфизм
        print("Я собака!")
sharick = Dog("Шарик")
print(sharick.__name)#Инкапсуляция
sharick.bark()
sharick.say_about_me()
'''
#Вспоминаем перегрузки - можем их переопределять
'''
class MyInt(int):
    def __add__(self, other):
        return f"сложение {self} + {other} = {int(self)+other}"
    def __sub__(self, other):
        return f"вычитание {self} - {other} = {int(self)-other}"
    def __mul__(self, other):
        return f"Умножение {self} * {other} = {int(self)*other}"
    def __truediv__(self, other):
        return f"деление {self} / {other} = {int(self)/other}"

a = MyInt(10)
print(a+20)
print(a-5)
print(a*5)
print(a/5)
'''

#----------------------------------------------------------------------------
# Модули
'''
Что это? 
Модуль - файл, в котором расписаны различные команды (в частности там встроенные классы с методами или расписаны различные функции), после его импортирования, 
мы можем спокойно его включать и применять

Помните, что вы (или другие люди) будут импортировать ваш модуль и использовать в
качестве переменной. Модуль нельзя именовать также, как и ключевое слово. Также имена
модулей нельзя начинать с цифры. И не стоит называть модуль также, как какую-либо из
встроенных функций. То есть, конечно, можно, но это создаст большие неудобства при его
последующем использовании
'''

'''
zoo = ['Бегемот', 'Собака', 'Мышь','Кошка','Ворона','Попугай']
#1 способ
import random #Модуль создание ЦЕЛЫХ чисел 
x = random.randint(0,10) # от 0  до 10 включительно
print(x)
print(random.choice(zoo))

#2 способ 
import random as r
x = r.randint(0,10)
print(x)
print(r.choice(zoo))

#3 способ - делаем конкретику, но он плох, тем что нам потом трудно догадаться откуда был применен модуль
from random import randint, choice
x = randint(55,100)
print(x)
print(choice(zoo))
'''
#Задачки
'''
Доп задание - сделать мини игру - угадай число.
Создаем случайное число от 0 до 10 и даем игроку 3 попытки на то, чтобы он угадал число.

import random as r
x = r.randint(0,3)
c = 3
while c > 0:
    i = int(input(f"Привет это мини-игра, угадай число на промежутке от 0 до 3, у тебя всего лишь 3 попытки! "))
    if i == x :
        print(f"Твоя победа")
        break
    elif i > x:
        print(f"Не то число! -1 шанс")
        c-=1
    elif i < x:
        print(f"Не то число! -1 шанс")
        c-=1
'''        
''' Анита
from random import randint
x = randint(0,10)
print('Давай сыграем в "угадай число"! у тебя 3 попытки')
for i in range(3):
    y = int(input('введи число '))
    if y == x:
        print('ты выиграл!')
        break
    else:
        print('ты не угадал :(')
print('а вот загаданное число-',"'",x,"'")
'''
#Создание калькулятора!
'''
#Создаем свой модуль - для этого создаем новый файл.py, я его назвал calc.py
import calc as c

class Calculator:
    def __init__(self): #Правило хорошего тона
        self.main()
    def main(self):
        while True:#Бесконечный цикл
            n1 = int(input('Введи первое число '))
            n2 = int(input('Введи второе число '))
            znak = input("Введи знак суммы, вычитания, деления, умножения или стоп")
            if znak == '+':
                print(c.summa(n1,n2))
            elif znak == '-':
                print(c.sub(n1,n2))
            elif znak == '//':
                print(c.delenie(n1,n2))
            else:
                print('Выход из работы')
                break
a = Calculator()
'''
#-----------------------------------------------------------------------------
# Продолжение темы модулей 19.01.2023
'''
Существует слово __name__, который при выводе покажет слово __main__, это значит,
что вы запустили этот файл как обычно, самостоятельно - главный файл
'''
#print(__name__)

'''
Если мы будем импортировать("модулировать"), то при том же записи на другом файл
он будет выводить, что он не главный
'''
#import Test
#print('Файл main', __name__)

### Смотри другой файл Test !!! там важная инфа

#---------------------------------
'''
    Ниже представлены некоторые команды, при помощи которых можно узнать о модули конкретно
'''
##import random
##
##print(random.__name__) #Покажетт имя модуля
##print(random.__package__)   #Покажет имя пакета(папки)
##print(random.__doc__)   #Покажет документацию модуля, если есть такого

#---------------------------------

'''
    При создании пакета ты должен обязательно создать файл __init__ , он является основой из всех основ!
    Смотри ниже пример, сейчас мы создали папку(пакет) по имени Test_Directory, в котором обязательно нужно создать файл __init__, является главной
    Кроме этого,можно создавать и другие файлы.py и пользоваться ими из пакета Test_Directory
    Пример ниже:
    1)Указывается пакет после него указывается конкретный модуль:
      1.1)Примечание:Если в этом пакете существует файл __init__ и в ней есть функция print, то он будет его выводить! 
    2) Если нужно использовать конкретный модуль, то в импорте нужно через точку написать конкректный модуль
    3) Как и в двух вышеперечисленных пунктов нужно указывать огромный путь 
        Вид: [пакет].[модуль] ((и пожеланию указать функцию).[функция])
'''
#---(1)
#import Test_Directory #Если в этой папке есть __init__ и функция print -> будет (в любом случае) её выводить!
#print(Test_Directory.name)

#---(2)
#import Test_Directory.calc as c #Из-за импрота, в консоли будет выводится ранее прописанная функция print(из основного файла __init__)!
#print(c.add(10,5))

#---(3)
#import Test_Directory.greet
#print(Test_Directory.greet.hello_new_pl())
