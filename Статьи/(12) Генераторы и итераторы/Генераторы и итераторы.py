'''
                            ГЕНЕРАТОРЫЫЫЫЫЫЫ (и итераторы)
    Обобщение:
    Короче, то что ты перебирал какие-либо элементы и добавлял в СПИСОК; код получался громозким
    И в общем генераторы(списочные выражения) заменяют несколько строчек кода в одну строку

    Как выглядит:
    [выражение for переменная in последовательность]

    Важно!
    Не забывать, что краткость - хорошо, но читаемость должна быть на ПЕРВОМ месте!

    Что должны понимать:
    Если использовать if без else, то нужно его закинуть в конец (после цикла for)

    Если использовать if с else, то нужно его закидывать до цикла for -> в основном это в словарях 
'''

#Пример 1
'''
перебрать просто числа от 0 до 10 вкл, двумя способами:

#1 способ
x = []
for i in range(0,11):
    x.append(i)
print(x)
### списковое включение
#2 способ
a = [i for i in range(0,11)] # [выражение for переменная in последовательность]
print(a)
'''
## !С выражением можно хоть что сотворить ( прибавитьБ умножитьБ перевести в str и тд) 
'''
b = [i*2 for i in range(0,11)]
print(b)
c = [str(i) for i in range(0,11)]
print(c)
'''
## !Мы можем перебрать другой список в список и что-то от себя добавить
'''
x = ['машина', 'Ауди', 'БМВ']
y = [i+'!' for i in x]
print(y)
'''

#Вспомни split() - он переводит вашу строку(str), с соответсвием тем, что вы указали в скобках
'''
Пример:
Ввести числа через пробел, а затем это закинуть в список, но так, чтобы это были числа
Пояснение:
так как по стандарту когда мы пишем в инпуте у нас переменные присваиваются типу str, поэтому надо переводить в int


some_list = [int(i) for i in input('Введи числа через пробелы').split(' ')]
print(some_list)
#Она равносильна, если писать в несколько строк:
s = []
a = input('Введи числа через пробел').split(' ')
#print(a) # Предпросмотр, то что в списке a
for i in range(len(a)):
    s.append(int(a[i])) #Здесь нужно переводить из str в int
print(s)
'''

## Можем перебрать СТАРЫЙ список и закинуть в НОВЫЙ список
'''
new_zoo = [i for i in ['Бегемот', 'Собака', 'Ежик', 'Енот', 'Медведб'] if len(i) > 5]
print(new_zoo)
'''


#Задачки:
'''
# # 1 доп создать список с ЧЕТНЫМИ элементами от 0 до 15 
# # 2 доп создать список с элементами от 0 до 150 которые делятся на 3 и на 5 без остатка
# # 3 доп добавить в список слова из последовательности(вводиой с клавиатуры), 
# но только те, длина которых больше 5
# # 4 доп создавть два цикла (да, так можно, догадайтесь как) чтобы добавить элемент i*j
# по типу как ниже, но естественно использяу СПИСКОВОЕ ВКЛЮЧЕНИЕ В ОДНУ СТРОКУ
list = []
for i in range(0,10):
    for k in range(0,10):
        list.append(i*k)

#1
x = [i for i in range(0, 16) if i % 2 == 0]
print(x)
#2
c = [i for i in range(0,150) if i % 3 == 0 and i % 5 == 0]
print(c)
#3
x = [i for i in input('Введите слова через пробел').split(' ') if len(i) > 5]
print(x)
#4
l = []
for i in range(0,10):
    for k in range(0,10):
        l.append(i*k)
print(l)
#Ниже предствален пример
m = [i*k for i in range(0,5) for k in range(0,5)]
print(m)
'''


#Можно работаь и словарем!
'''
d = {i:i**2 for i in range(0,10) if i != 5}
print(d)
'''

'''
    Как работает если нам нужно использовать if else ?
    If else заносится в перед перед for

dict1 = {x: 'Есть' if x in ['Зебра','Собака', 'Колбаса'] else '0' for x in ['Зебра','Енот','Медведь','Собака','Колбаса']}
print(dict1)
d1 = {x: y for x, y in [['А', 0], ['В', 1], ['С',2]]}
print(d1)
'''

'''
#Работа со словарем!
dict1 ={x: y for x in 'ABC' for y in 'ZXC'}
print(dict1)
#Способ2
dic1 = {x : 'z' for x in 'abc'}
print(dic1)
#Эквивалентно что и снизу и сверху
di1 = {}.fromkeys('ABC', 'z')
print(di1)
#Способ 3
d1 = {x:y for x, y in [('A',0),('B',1),('C',2)]}
print(d1)
'''

'''
    Словари, в котором значения имеют генераторы см ниже

dict1 = {x: [y for y in range(x, x + 3)] for x in range(4)}
print(dict1) #{0: [0, 1, 2], 1: [1, 2, 3], 2: [2, 3, 4], 3: [3, 4, 5]}

dict1 = {x: [y % 2 for y in range(10)] for x in 'ABC'}
print(dict1) #{'A': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 'B': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 'C': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}

dict1 = {'ABCDE'[i]: [i % 2]*5 for i in range(5)}
print(dict1)

dict1 = {x: {y: 0 for y in 'XYZ'} for x in 'ABC'}
print(dict1)
#Супер сложный вид
dict1 = {x: {y: [z for z in range(z, z+ 2)] for y in 'XYZ'} for x, z in zip('ABC', range(3))}
print(dict1)
'''

##dict1 = {x: 1 if x in 'ACE' else 0 for x in 'ABCDEF'}
##print(dict1)

#Задачки
'''
1)Попробовать создать множество используя 'включение' (в одну строку)
2)Попробовать создать кортеж тоже используя включение (и монжо функцию tuple)

#1 set = {}
s = {i for i in range(1,8) if i % 2 == 0}
print(s)
# Кортеж = tuple
t = tuple([i for i in range(0,5)])
print(t)
'''
#Пример :
##list1 = [i * j for i in range(1,6) for j in [1,2,3]]
##print(list1)

##set1 = {i for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if 'a' not in i}
##print(set1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    повторение
    
some_list = [i if i%2 == 0 else 'Нечетное' for i in range(0,10)]
print(some_list)

some_dict = {i:i**2 for i in range(0,10)}
print(some_dict)

some_set = {i for i in range(0,10)}
print(some_set)

x = (1,2,3)
some_tuple = tuple([i for i in range(0,10)])
print(some_tuple)
'''
#------------------------------------------------------------------------------
'''
                                Генераторы
    - генерируют(создают) значения
    () - круглые скобки

    Особенности:
    Отличается тем, что он хранит у себя в памяти ,нужно иначе его выводить

    ТАкже особенность генераторы, она кончаемая, она как корзинка, если мы просим вывести 0 значение, то он выведит, но не сохранит у себя
    Пример с пакет чипсами - едим до конца

    ГЕнераторы способны увеличить производительность программы и уменшить расход памяти
    (Пример если у тебя много номеров)

    Собвстенно они создаются, как списочное включение, функциями или класс
'''
##some_gen = (i for i in range(0,10))
##print(some_gen) # ничего не выведит
'''
Способ 1
next до тех пор пока не дойдет до 10,
после того как мы переходим 10, выведит ошибку (можешь проверить(много поставить принт))

Чтобы не было ошибки, то вторым аргументом наишем слово 'Пусто'
print(next(some_gen, 'Пусто'))
'''

##some_gen = (i for i in range(0,2)) 
##print(next(some_gen,'пусто')) #Ответ 0, второй аргумент записыывем чтобы предстречтся вдруг будет ошибка
##print(next(some_gen,'пусто')) #Ответ 1
##print(next(some_gen,'пусто')) #Ответ ПУСТО, так как мы перешагнули порог двойки
'''
Способ 2
В список кинуть
'''
##some_gen = (i for i in range(0,10))
##print(list(some_gen))
'''
Способ 3
Через цикл for
'''
##some_gen = (i for i in range(0,10))
##for i in some_gen:
##    print(i)

############################
'''
    Могут быть генераторы в функциях см ниже

    Лучше использовать yield - так как он возвращает одно значение и НЕЗАВЕРШАЕТ, а останавливается - чекпоинт
    и с этого момента он продолжает, что было после yield, снизу показано, что после него будет print

def f(number):
    for i in range(0,number):
        #return # Return - воозвращает значение и ЗАВЕРШАЕТ ФУНКЦИЮ!
        yield i # yield - Возвращает значение и приостанавливает и ждвет пока снова не
                # не вызовем его  с помощью next(или другим способом(раннее изучимым))
        print('Это выполнится уже после заморозки')

res = f(10)
print(next(res))
print(next(res))
'''

'''
Задачки
Создать генератор, но вместо range использовать список с животными

zoo = (i for i in ['Макака','Собака','Орел','Птичка','Гриб'])
for i in zoo:
    print(i)
#------------------------------------------------------------------

1Реализовать генерациб бесконечного количества чисел от 0 до бесконечности пока не завершим программу

2Создать функ-ген для генерации чисел фибоначчи 

#1
def f():
    i = 0
    while True:
        i+=1
        yield i
        b = input('Стоп напиши если хочешь остановить')
        if 'стоп' == b:
            return 

for i in f():
    print(i)

#2
def fib(n):
    num1 ,num2 = 0, 1 # так будет всегда что мы начинаем с 0 и 1
    for i in range(n):
        yield num1
        num1, num2 = num2, num1+num2
print(list(fib(10)))
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    Задача:
    Что, если мы хотим использовать генератор, который ранее создали, использовать во второй раз?
    Для этого нужно использовать ООП, т.е. использовать класс, в котором используем перезагрузку __iter__ - метод, который перезагружает(пересоздаёт) генератор.
    __iter__ отвечает за :
        Он отвечает за генератора, если его не написать, соответсвенно,это уже не генератор!
        Он отвечает за повторный запуск генератора!(типо переоживляем его)
'''

# НЕудачный пример
'''Так как он здесь создает второй новый генератор, это можно увидеть в выводах print!
То есть он использует генератор и все, он опустеет, но так как мы требуем ещё, он создает второй генератор
Но из-за этого память переполняется на компьютере!'''
##def gen():
##    for i in range(0,10):
##        yield i
##print('Первый запуск')
##res = gen()
##print(res)
##
##for i in res:
##    print(i)
##print('Второй запуск')
##print(res)
##
##for i in res:
##    print(i)

#Удачный пример:
'''
class MyGeneretor:
    def __init__(self,start): #Обязательно пишем, без него никак
        self.start = start
    def __iter__(self):
        for i in range(self.start):
            yield i

my_gen = MyGeneretor(5)
print(my_gen)
for i in iter(my_gen):
    print(i)
print()
#Так как мы перегрузили генератор, то он выдает такое же значение как и впервый раз
for i in iter(my_gen):
    print(i)
'''

'''
Задача:
Реализовать класс генератор, который генерирует случайные числа,диапазон и количество задается пользователем
Например, он ввёл числа: 0,3,5
Возможные случайные числа на выходе: 0 1 0 2 0

Подсказка: random.randint(0,3) - создает случайное число от 0 до 3

import random as r
class MyRandomGen:
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
    def __iter__(self): #Генератор, а соответсвенно вспомни как выводить генераторы на экран, см выше
        for i in range(self.count):
            yield r.randint(self.start,self.end)
my_randomm = MyRandomGen(0,3,10)
print(list(iter(my_randomm)))
'''

'''
Задача
Написать функцию генератор(выражение генератор), генерирующий числа от 0 до 10, которые кратны 3

def gen(x):
    for x in range(x):
        if x % 3 == 0:
            yield x
print(list(gen(6)))
# or
s = (i for i in range(0,10) if i%3 == 0)
'''

'''
Задача:
Дан набор слов, допустим ['as_as__asd','asda','as']. Замените _ на пустоту (или на пробел).
Задачу нужно решить в одну строку генератором

a = (i.replace('_',' ') for i in ['sfa__as','asd__as','aas__aas'] )
for i in a:
    print(i)
'''

'''
Задача
Есть набор слов, допусти s = ['asdyy','yyy','aassyyt', 'syka', 'sychka']
Создать новый список в одну строку из тех слов, где встречается ДВЕ буквы y(латинская буква)

s = ['asdyy','yyy','aassyyt', 'syka', 'sychka']
#a = [i for i in s if 'yy' in i] #Неправильно так как, в слове yyy всего три 'y', а по условию нужно ДВЕ 'y'
b = [i for i in s if i.count('y') == 2]

print(b)
'''


#ВАЖНАя ЗАДАЧА ПО ЭКОНОМИЮ ПАМЯТИ !
'''
    Задача состоит в том, что у тебя очень много номеров в файле и тебе нужно перебрать их, где только должны остаться
    российские номера, т.е. удалить иностранные и всякие не понятные номера

def func_gen(name_of_file):
    with open(name_of_file) as f:  # открываем файл
        num_lists = f.readlines() # считываем весь файл в список
        # очистить список от мусора (\n)
        num_lists = [i.replace("\n","") for i in num_lists]
        for i in num_lists:
            if (i.startswith("+7") and len(i) == 12)  or (i.startswith("8") and len(i) == 11):
                yield i

result = func_gen("numbers.txt")
print(list(result))
'''

#-------------------------------------------------------------------------------------------------------------
#27/01/2023                     Метод __iter__ ИТЕРАТОООООООООООООООООООООРРРРРРРРРРРР

'''
iter - способ, который дает возможность из словаря, списка(любой коллекции) превратить в генератор

Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз.
С точки зрения Python - это любой объект(экземпляр класса), у которого есть метод __next__.
Этот метод возвращает следующий элемент, если он есть, или возвращает исключение
StopIteration, когда элементы закончились. Кроме того, итератор запоминает, на каком
объекте он остановился в последнюю итерацию.


Коллекции, строки — это все итерируемые объекты!

Читать статейку!!
'''


'''
class MyGeneretor:
    def __init__(self,start): #Обязательно пишем, без него никак
        self.start = start
    def __iter__(self):
        for i in range(self.start):
            yield i

my_gen = MyGeneretor(5)
print(my_gen) # Пока что он часть класса
gen = iter(my_gen)
print(gen)    #Стал генератором
print(next(gen)) #Вот он генератор
print(next(gen))
'''

'''
#iter - позволяет также и со строками пользоватся!

x = 'Колбасевич'
x = iter(x)
#x = reversed(x) # создает итератор 
print(next(x))
'''

#   ЛОГИКА next - его можно переопределить при помощи класса, то есть к примеру, он не выводил по частям, а еще и что-то другое
'''
class MyGeneretor:
    def __init__(self,n): #Обязательно пишем, без него никак
        self.n = n

    def __iter__(self): #обязательное условие, чтобы переопределить next
        print('выполняется метод ITER')
        return self # В итер мы обязаны вернуть СЕБЯ (self)

    def __next__(self):
        self.n = self.n*2 # Выводим кол-во колбасевичей
        return f"В холодильние {self.n} колбасевичей"
    
my_gen = MyGeneretor(5)
gen = iter(my_gen)
print(next(gen)) 
print(next(gen))
'''

#ЗАдачки
'''
# 1 доп задаание Создайте генератор в одну строку, который выдаст вам числа от -15 до 30, которые не делятся на 3 без остатка

# 2 доп задание Создайте арифм. прогрессию, где пользователь сам задает количество чисел, с какого начать и какой промежуток
# пример ввода 1,5,4
# пример вывода
# 1
# 6
# 11
# 16

3 доп задача
дан словарь с числовым значениями. Необходимо их все перемножить и вывести на экран
4 доп задача
Создать словарь из строки 'python' следующим образом: в  качестве ключей возьмите буквы строки, а значениями пусть будут числа,
соответсвующие количетсву вхождений данной буквы в строку.
'''

#1
##s = (i for i in range(-15,31) if i % 3 != 0)
##for i in s:
##    print(i)

###2
##def arif_progerss(start,diap,size):
##    for i in range(size):
##        yield start
##        start = start + diap
##
##print(list(arif_progerss(1,3,12)))

#3
##some_dict = {i:i*i for i in range(0,10)}
##print(some_dict)

#4
##st = 'pyrhhhhonnnn'
##some_dict = {i:st.count(i) for i in st}
##print(some_dict)


#-------- - - -- - - -    - -      - - - - - - - - -  - --  - -- - - - -
'''
    Как мы  можем запрещать кому чтото такое делать , выброс запрещенки!

    Это помогает увидеть где нужно потом доработать программу! Иногда полезно,а иногда нет, т.к. может запутать вас
    Но это можно избежать просто напросто создать свой класс ошибок
'''
##class MyGeneretor:
##    def __init__(self,n): #Обязательно пишем, без него никак
##        self.n = n
##
##    def __iter__(self): #обязательное условие, чтобы переопределить next
##        print('выполняется метод ITER')
##        return self # В итер мы обязаны вернуть СЕБЯ (self)
##
##    def __next__(self):
##        self.n = self.n*2 # Выводим кол-во колбасевичей
##        if self.n <= 50:
##            return f"В холодильнике {self.n} колбасевичей"
##        else:
##            return StopIteration #Выводит ошибку, т.к. идет переполнение больше 50 при заданой 15
##        
##my_gen = MyGeneretor(15) 
##gen = iter(my_gen)
##print(next(gen)) 
##print(next(gen))


#Домашка
'''
Написать выражение-генератор, возводящее в куб числа от 1 до 10 включительно
Вывести все значение в виде списка
'''
s = (i**3 for i in range(1,11))
print(list(s))
