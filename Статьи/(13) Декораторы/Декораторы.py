'''
Вспоминаем прошлую тему про генераторы через классы:

class My_generator:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.n = self.n + 1
        if self.n < 10:
            return self.n
        else:
            return StopIteration

generator = My_generator(8)
generator = iter(generator)
print(next(generator))
print(next(generator)) # Выдаст ошибку, так как превышает 10, либо равняется 10
'''
#------------------------------------------------------------------------------
'''
     Декаратор - обёртка функции, которая позволяет расширить возможности функции
     ОН принимает на вход в качестве аргумента саму функцию!

    Чтобы её создать необходимо засунуть её в другую функцию, и создать вторую функцию, которая и является оберткой - wrapper()
'''
#---------------------------------------------------------------------------

'''Пример 1 
def decorator_krasivaya_obertka(some_func):#Передается какая-то функция
    def wrapper():
        #ЗАписывается ваша логика обертки
        x = print('Я в очень красочной обёркте, я крутой продукт!')
        x = input('Какая')
        result = some_func(x)
        return result
    return wrapper #Обязательно без скобок!

@decorator_krasivaya_obertka
def func_konfeta(x):
    return f"Я {x} конфета"

@decorator_krasivaya_obertka
def func_marlmelad(x):
    return f"Я {x} мармеладка"

print(func_konfeta())
print(func_marlmelad())
'''
#Пример2
'''
def decorator_calc(some_func):
    def wrapper():
        x = int(input('Введите число 1 '))
        y = int(input('введите число 2 '))
        return some_func(x,y)
    return wrapper

@decorator_calc
def plus(x,y):
    return x+y

@decorator_calc
def minus(x,y):
    return x-y

print(plus())
print(minus())
'''

'''
Задачки:
1)Создать ещё одну любую функцию и применить к ней декоратор
2)Сделать декоратор, который будет говорить 'Старт функции', потом вызывать функцию, а потом говорить 'Конец'
  Что должна делать сама функция? Все равно, хоть говорить 'Привет колбасевич'
'''
#1)
##def obertka(some_func):
##    def wrapper():
##        print('Я в очень красивой обертке')
##        x = input('Какая?')
##        res = some_func(x)
##        return res
##    return wrapper
##
##@obertka
##def konfeta(x):
##    return f"Я очень {x} конфетка"
##print(konfeta())

#2)
##def obertka(some_func):
##    def wrapper():
##        print('Старт функции!')
##        x = input('Как тебя зовут?')
##        res = some_func(x)
##        print('Конец функции!')
##        return res
##    return wrapper
##
##@obertka
##def hello(x):
##    return f"Привет {x} я колбасевич "
##print(hello())

'''
НАстоящая задачка , которая раскрывает смысл декоратора:
Написать декоратор, который открывает файл.txt
Сама же функция должна записывать туда данные, которые введёт пользователь.
В начале декоратора говорится ФАЙЛ ОТКРЫТ, а в конце ФАЙЛ ЗАКРЫТ
'''
#Как я делал:
'''
def obertka(some_func):
    def wrapper():
        with open('Файл.txt', 'w+') as data:
            print('ФАЙЛ ОТКРЫТ!')
            x = input('Что хотите написать, чтобы функция сама записала, то что вы запишите! ')
            a = data.write(x)
            print('ФАЙЛ ЗАКРЫТ!')
        return a
    return wrapper

@obertka 
def writell(x):
    return f" Вы записали следующие слова в txt файл {x}"
print(writell())
'''
###Как делал учитель: У него получше, так как у меня выводится цифра какая-то
'''
def open_file(some_func):
    def wrapper():
        with open('file.txt', 'w+') as f:
            print('Файл открыт')
            some_func(f)
            print('файл закрыт')
    return wrapper
@open_file
def write_to_file(f):
    line = input('Введите, что ты хочешь добваить.')
    f.write(line)
write_to_file()
#или
def write_to_file(f):
    while True:
        line = input('Введите, что ты хочешь добавить.')
        if line == 'стоп':
            break
        f.write(line + "\n")

write_to_file()
'''

###Бесконечный цикл:
##while True:
##    print('1')


#------------------------------------------------------------------------------------------------------------------
#Продолжение темы:
#Повторение

#Пример 1
'''
def decor_func(some_func):
    def wrapper():
        print('Начало декоратора')
        t = input('Вкус?')
        some_func(t) #Вызываем функцию
        print('Конец декоратора')
    return wrapper

@decor_func
def func_konfeta(taste):
    print(f"Я {taste} конфета")

func_konfeta()


    Бывает порой, что надоедает каждый раз прописывать что-то, как например выше. Тогда мы должны что-то указывать в параметре в wrapper(t)
    А, когда нужно выводить в конце программы функцию, то указываем просто аргументы

#Пример-усовершенствованный 1
def decor_func(some_func):
    def wrapper(t): #Указываем нужные нам аргументы
        print('Начало декоратора')
        #t = input('Вкус?')
        some_func(t) #Вызываем функцию
        print('Конец декоратора')
    return wrapper

@decor_func
def func_konfeta(taste):
    print(f"Я {taste} конфета")

func_konfeta('Сладкая')
'''

#           У Декораторов могут быть КЛАССЫ
'''
class Candy:
    def __init__(self,some_func):
        self.some_func = some_func
        print(f"Это __init__ класса Candy, меня вызвала функция {self.some_func.__name__}")
    def __call__(self):
        print('Это старт декоратора')
        t = input('Вкус?')
        self.some_func(t)
        print('Это конец декоратора')

#Сначала будет выводится __init__ потом последовательно

@Candy
def func_konfeta(taste):
    print(f"Я {taste} конфета")
@Candy
def func_marmelad(taste):
    print(f"Я {taste} мармелад")
func_konfeta()
func_marmelad()
'''
#--------------------------------------------------------------------------------------
'''
    Существют для функция такие параметры как *args и **kwargs
    *args - это передача неименнованных аргументов в заранее неизвестном количестве -> Возвращает кортеж
    *kwargs - это передача именнованных аргументов -> Возвращает словарь -> {ключ:значение}
'''
#Примеры
'''
def func(*args):
    print(args)
func(5,10,'fgljhgf',123,)

def summa(*args):
    some_list = list(args)
    summa = sum(some_list)
    print(summa)
summa(10,20,100)

def func2(*args,**kwargs):
    print(args)
    print(kwargs)

func2(100,200, name = 'Мистер', second_name = 'Колбасевич')
'''

#----------------------------------------------------------------------------------------
# Продолжение темы декораторов

'''
    В декораторах можно добавлять параметры, которые существенно могут влиять на саму функцию(изменять её)
    Пример: @Candy(test_or_not)
    К примеру, это нужно, чтобы проверять время захода пользователя на сайт, обработка и т.д. Ниже пример попроще 
    
    Ниже предоставлен пример того, что будем проверять запуск системы -> программа будет проверять тестовый ли запуск или настоящий, если настоящий, то какие-то появляются плашки(какая-то инфа и тп.тд),
    а если тестовый, то просто показывает, как работает сам код, без каких-либо лишних плашек.

    На самом деле просто к wrapper добавляется новая функиция, то есть происходит наложение одной функции на другой.
'''
#import datetime

##def new_decor(test_or_not):
##    def decor_time(some_func):
##        def wrapper(x):
##            print(f"Это - {test_or_not}")
##            start = datetime.datetime.now()
##            some_func(x)
##            end = datetime.datetime.now()
##            print(f"Время выполнения функции: {end - start}")
##        return wrapper
##    return decor_time
##
##@new_decor('Тест') #Можно поставить "Настоящий запуск работы"
##def make_list(j):
##    some_list = [i for i in range(j)]
##make_list(100000)

#Аналог с классом

##class Class_new_decor:
##    def __init__(self,test_or_not):
##        self.test_or_not = test_or_not
##    def __call__(self,some_func):
##        def wrapper(x):
##            print(f"Это - {self.test_or_not}")
##            start = datetime.datetime.now()
##            some_func(x)
##            end = datetime.datetime.now()
##            print(f"Время выполнения функции: {end - start}")
##        return wrapper
##
##@Class_new_decor('Настоящий запуск работы')
##def make_list(j):
##    some_list = [i for i in range(j)]
##make_list(100000)


#Задача
'''
Доп задание - создать декоратор такой же структуры, необходимо создавать последовательность четных чисел
# от 0 до значения которое будет передано в качестве аргумента после @decor.....(воттут)
# пример - @decor_with_args(5)
# пример вывода 0 2 4
'''
##def obertka(some_func):
##    def wrapper():
##        t,j = map(int,input('Введите сначало маленькое число, а затем максимальное(через пробел) ').split())
##        print('Последовательность четных чисел')
##        for i in range(t,j):
##            if i % 2 == 0:
##                print(i)
##        return some_func(t,j)
##    return wrapper
##
##@obertka
##def chet(x,y):
##    return(f"Последовательность четных чисел из промежутка {x,y}")
##print(chet())
#или
##def obertka(some_func):
##    def wrapper(t,j): #Закинул на прямую
##        #t,j = map(int,input('Введите сначало маленькое число, а затем максимальное(через пробел) ').split())
##        print('Последовательность четных чисел')
##        for i in range(t,j):
##            if i % 2 == 0:
##                print(i)
##        return some_func(t,j)
##    return wrapper
##
##@obertka
##def chet(x,y):
##    return(f"Последовательность четных чисел из промежутка {x,y}")
##print(chet(1,10))

#-----------------------------------------------
'''
    В Python существуют документации -> это можно сделать так ''' ''' или " "
    Вызывается при помощи __doc__
'''
#Пример 1:

def f(x,y):
    #''' Складываем два числа x и y''' 
    print(x+y)
#f(10,100)
print(f.__doc__)

#Пример 2:
'''
import random
print(random.randint.__doc__)
'''

#Пример 3: (В декораторах)
#Надо учитывать, что в функции не будет выводится документация, только в декораторе!

def dec(sme_func):
    '''Документация декораторао dec'''
    def wrapper(x,y):
        '''Вот эта документация, а не документация в func'''
        print('Декоратор')
        some_func(1,100)
        print('Конец')
    return wrapper

@dec
def func(x,y):
    '''Складываем два чсила x и y''' #Это вызыватся не будет!
    print(x+y)

print(func.__doc__)
print(dec.__doc__)
#Пример 4: (В классах)

class Dec:
    '''Документация класса-декоратора'''
    def __init__(self,x):
        self.x = x
    def __call__(self,some_func):
        def wrapper():
            '''Документация враппера-класса'''
            print('Лялялял')
            some_func()
        return wrapper

@Dec
def func(x,y):
    '''Складываем два числа x и y'''
    print(x+y)
print(func.__doc__)

print('--------------------------------------------')
'''
Задачка, где дает реальное понимание что такое декоратор - для сайта

Декораторы можно использовать для проверки состояния перед выполнением функции:
например, зарегистрировался ли пользователь, есть ли у него достаточное количество праф

Нужно создать декоратор, который будет принимать параметр роли пользоватея
Например @dec("user")

На выходе должен быть ответ "вам разрешен доступ к сайту Admin Panel" или наоборот "Вам запрещен доступ..."

permission = ['admin','superadmin','moderator']
'''
##permission = ['admin','superadmin','moderator']
##
##def check_users(per):
##    def obertka(some_func):
##        def wrapper():
##            some_func()
##            if per in permission:
##                print('вам разрешен доступ к сайту Admin Panel')
##            else:
##                print('Вам запрещен доступ...')
##        return wrapper
##    return obertka
##
##@check_users("user") #Здесь мы меняем аргумент/параметр, когда ты регаешся сайт сам решает кто ты будешь
##def f():
##    print('Обработка')
##f()


#---------------------------------------------------------------------------------
'''
    Кеш-памяти
'''
##import datetime
##from functools import lru_cache
##def dec_time(sone_func):
##    def wrapper(n):
##        start = datetime.datetime.now()
##        some_func(n)
##        end = datetime.datetime.now()
##        print(end - start)
##    return wrapper
##
##@dec_time
##@lru_cache(None)
##def make_big_list(n):
##    some_list = [i for i in range(0,n)]
##
##make_big_list(2000000000)
##make_big_list(2000000000)
