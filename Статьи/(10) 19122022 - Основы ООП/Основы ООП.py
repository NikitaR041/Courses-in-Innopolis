#                                   Предисловие.Курс 1
'''
    python - обектно-ориентированный язык,а соотвественно все, что мы НЕ выдим является
    объектом какого-либо класса.
    Узнать тип объекта нам поможет функция TYPE()
'''
#Пример :
##def func():
##    pass   #Ничего не делание
##
##class Test:
##    pass
##
##print(type(5))
##print(type(True))
##print(type(5.0))
##print(type('T'))
##print(type({'3': 2}))
#----------

'''----------
    Класс можно представить, как некий шаблон описывающий общие свойства и возможныедействия.
    Например, в любой игре огромное количество персонажей и писать под каждогоиз них отдельный код, было бы очень накладно и ресурсоемко.
    Все персонажи имеют какието общие характеристики(переменные), такие как например жизни, имя и т.п, а также наборкаких то методов, например ходить, говорить, стрелять.

    Метод - та же функция, но написанная внутри класса.Объект же, если брать в пример игру, то это собранный на основе класса персонаж.Для создания класса используется ключевое слово class.

    (1)Давайте создадим простой класснекого персонажа.
    (2)Создадим экземпляр класса и попробуем выведем его имя и вызовем метод say() 

#(1)
class Person:
    name = 'Иван'
    surname = 'Иванов'
    #Ниже написана функция, но это как раз таки метод персонажа, т.е грубо говоря, он умеет говорить
    def say():
        print('Hello')
#(2)
person1 = Person #Создан экземпляр класс (на самом деле это нафиг не нужно)
print(person1.name)
person1.say()    #Хотя без экземпляра невозможно было бы вывести метод(функцию) класса
-------------'''

#####     ВАЖНО
'''           ТАКЖЕ
    В метод __init__ мы можем передать необходимые значения и сохранить их в локальные переменные,
    значения которых будут разные для разных объектов.

    Теперь у каждого объекта свое имя и свой возраст.
    Помочь программе, понять какое значение принадлежит объекту, позволяет self, которые ссылается именно на объект,который обратился к данному свойству.

    Метод init, называют конструктором класса или же методом инициализации.

class Person:
    def __init__(self, name, age): #Можно менять self в любую переменную
        self.name = name
        self.age = age

person1 = Person('Иван', 15)
person2 = Person('Петр', 14)
print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
'''

###------ Курс 2
'''
    Предположим,нам необходимо создать класс транспорта,но видов транспорта может быть больше количество : легковыемашины,грузовые,общественныйтранспортит.
    Эти видыимеют как общие,так и строго индивидуальные характеристики

    (1)Создали родительский класс и указали, что у транспорта есть скорость, цвет и возможность
    говорить бип
'''
#Родительский класс(1)
##class Transport:
##    def __init__(self,speed,color):
##        self.speed = speed
##        self.color = color
##    
##    def beep(self):
##        print('Beep')

'''(2)
Теперь необходимо создать дочерние классы. Для указания, что класс является дочерним,
необходимо при указании названия класса, в скобках указать класс от которого мы
наследуемся

В классе Car мы указали, что он наследуется от класса Transport, а также в методе
инициализации указали вызов super(), в котором сослались на метод инициализации
родительского класса, т.е простыми словами, мы сказали что нам необходимо вызвать метод
init родительского класса. Теперь укажем для класса пару переменных и какой нибудь метод
выведем в консоль
'''         #(2)
##class Car(Transport):
##    def __init__(self, speed, color, owner):
##        super().__init__(speed, color)
##        self.owner = owner
##
##    def say_owner(self):
##        print(f"Владелец {self.owner}")
##
##car1 = Car(100,'Blue','Вася')
##print(car1.color)
##print(car1.speed)
##print(car1.owner)
##car1.beep()
##car1.say_owner()

#НЕ пугайся, это просто такой пример, чтобы ты легко разобрался! Если, что ты можешь прочитать этот мануал в файле.)

'''------------------------------------------------------------------------------
В данном примере мы создали класс,который наследуется от двух предыдущих классов.
Несмотря на то что класс SportCar пустой, он наследует все методы и атрибуты от
родительских классов.

class Transport:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
    
    def beep(self):
        print('Beep')
class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner

    def say_owner(self):
        print(f"Владелец {self.owner}")

class SportCar(Car, Transport): #вот он класс, который берет из двух других классов!
    pass

car1 = Car(100,'Blue','Вася')
print(car1.color)
print(car1.speed)
print(car1.owner)
car1.beep()
car1.say_owner()
'''

'''
Если же у нас в классе Car будет метод, с таким же названием как у другого родительского
класса, то метод будет переопределен и вызовется метод из класса Car - можно исправить принципом полиморфизма
'''
##class Transport:
##    def __init__(self,speed,color):
##        self.speed = speed
##        self.color = color
##    
##    def beep(self):
##        print('Beep')
##class Car(Transport):
##    def __init__(self, speed, color, owner):
##        super().__init__(speed, color)
##        self.owner = owner
##
##    def say_owner(self):
##        print(f"Владелец {self.owner}")
##
##    def beep(self):     #Теперь при вызове beep, команда будет вызыватся из класса CAR !!!! НЕ ИЗ РОДИТЕЛЬСКОГО КЛАССА
##        print('Hello')
##class SportCar(Car, Transport): #вот он класс, который берет из двух других классов!
##    pass
##
##car1 = Car(100,'Blue','Вася')
##print(car1.color)
##print(car1.speed)
##print(car1.owner)
##car1.beep()
##car1.say_owner()


#-----------------------------------------------------------------------------------------------------------------
                                            # 3 КУРС по основам изучения ООП
'''
    Может быть, что какие-то аргументы могут быть не обязательными, к примеру, иметь по умолчанию какое-то значение

    Например если пользователь не указал при создании объекта цвет, то мы можем указать,
    чтобы он брался из значения по умолчанию

    Важно:
    если вы начали указывать для какого-то аргумента значение по умолчанию, то все остальные
    аргументы после него должны тоже иметь значения по умолчанию, иначе возникнет ошибка

#Пример для функций :
def get_name( name = 'Иван'): # по умолчанию будет выводится имя Иван
    print(name)

get_name()       # По умолчанию будет выводится Иван
get_name('Петр') # Вывод будет Петр

#Пример для класса
class Car:
    def __init__(self, speed, color = 'Yellow'): # По умолчанию третий параметр будет выводить Желтый цвет
        self.speed = speed
        self.color = color

car1 = Car(100)         #Присвоили переменную класс Car
car2 = Car(100,'Синий') #Присвоили переменную класс Car

print(f"{car1.color}") #Просто выведит Yellow
print(f"{car2.color=}") #Выведит car2.color=Синий 

#2 пример для класса
class Animal:
    # Если вы указали значение по-умолчанию, то у всех слудющих аргументов его ТОЖЕ нужно указать, иначе ошибка
    def __init__(self, name, fav_food = 'Пицца', color = None):
        self.name = name
        self.fav_food = fav_food
        self.color = color
    def eat(self):
        print(f"Моя любимая еда - {self.fav_food}")
        print(f"Мой цвет - {self.color}")

shlepa = Animal(name = 'Шлепа', fav_food = 'Морковка', color = 'Белый') # Можно так делтаь , чтобы не запутаться кому были присвоены аргументы параметрам
shlepa.eat()
'''

'''
    В примере ниже в методе say_owner проверяем если есть какое то значение, то вывести
    нам его, иначе вывести сообщение о отсутствии владельца 

class Car:
    def __init__(self, speed, color = 'Желтый', owner = None) -> None:
        self.speed = speed
        self.color = color
        self.owner = owner

    def say_owner(self):
        if self.owner:
            print(f"Владелец {self.owner}")
        else:
            print(f"У данного автомобиля нет владельца")
car1 = Car(100,'Зеленый', 'Ваня')
car2 = Car(350,'Синий')
car1.say_owner()
car2.say_owner()
'''
### ----------------------------------------------------------------------------------------
#                                       ПАРОЛИ
'''
    Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным). или возможность изменить зону видимости переменных и методов
    Инкапсуляция делает некоторые из компонент доступными только внутри класса.

    НО ВАЖНО! ИНКАПСУЛЯЦИЯ В pyhton условна и является соглашением на уровне разработчиков,
    так как нет конкретных модификаторов доступа, запрещающих изменение значений внутри класса,
    но по крайней мере усложняет данное действие
'''
#Простой способ защиты
'''
Нижнее подчеркивание можно применять не только к атрибутам, но и к методам. "_" показзывает, что то или иное  переменная не предназзначен для использование вне класса 

class Person:
    _age = 15 # Нижнее подчеркивание означает, что её запрещено изменять

pers1 = Person
print(pers1._age)
pers2._age = 14
print(pers2._age)
'''
#Средний уровень
'''
 2Х нижнее подчеркивание запрещает вызывать какой-либо МЕТОД, ПРЕМЕННУЮ.
 Вывод ошибки: AttributeError: type object 'Person' has no attribute '__say_hello,
 означает, что данного атрибута(метода) у класса нет

class Person:
    _age = 15
    def __say_hello():
        print('Hello') #ЗАпрешенное слово
##        print(self.__age)

per1 = Person
print(per1._age)
#per1.__say_hello() #Нижнее подчеркивание не дает вызвать метод!

### НО можно обойти эту защиту
#Для этого нам всего лишь необходимо указать после объекта название класса с нижним подчеркиванием, а сразу после него название метода
per1._Person__say_hello()
'''
#Пример
# _ - слабая инкапсуляция (рекомендация того, что не стоит выводить её вне класса)
# _ - сильная инкапсуляция, прячет метод (нельзя ее выводить припомощи принта, разве что внутри класса)
'''
пример 1
class Ded_Moroz:
    def __init__(self, age):
        self.__age = age
    #Функция снизу, которая позволяет обойти препятсвие
    def age(self):
        return self.__age

ded = Ded_Moroz(199)
print(ded.age) # Не видит (вызывает переменную ded и его значение age)
print(ded.age()) # Видит, т.к. обошли при помощи функции

пример 2

class Ded_Moroz:
    def __init__(self, age):
        self.__age = age
    #Функция снизу, которая позволяет обойти препятсвие
    @property # позволяет вызывать функцию без использование (), простое представление, что property - обертка функции
    def age(self):
        return self.__age
    # Функция сниху, которая позволяет изменять аргумент
    @age.setter #Позволяет изменять значение ! Обязательно первым указываем переменную, которую хотим изменить
    def age(self, new_age):
        self.__age = new_age
        
ded = Ded_Moroz(199)
print(ded.age) #(1) Не видит (вызывает переменную ded и его значение age)

#print(ded.age()) #(2) Видит, т.к. обошли при помощи функции

ded.age = 200 # типо присвоили переменную другое значение (x = 1 типо такого)
print(ded.age)  #(2.1) Видите, что вызываем функцию без оббертки!

print()
'''
#---------------------------------------------------------------------------------------------
##                                      Декораторы и сеттеры - поверхностное изучение
#продолжение темы "Пароли" - можем использовать специальные декораторы для написания более защищенного приложения
'''
    @property
    Декораторы - это функция обёртка. Для более углубленного изучение нужно ждать продолжение данной темы
    1) С помощью нею позволяет обращаться к какому-то методу без вызова, а точнее, как к обычной пременной.

    @a.setter, где a - имя метода, setter - непосредственно сама команда
    Сеттеры - это метд, который используется для установки значение свойства.
    В основном используется для изменение ЗНАЧЕНИЯ в методе (см. примеры)
'''
#Пример
'''
    (1) Так как мы ‘спрятали’ наше имя и пользователь не знает о данном поле, мы с вами создадим
        метод, который будет выводит наше имя пользователю
    (2) Декорируем данный метод специальным декоратором,который позволит обращаться к
        данному методу без вызова. Как к обычной переменной
    (3) Теперь мы можем обращаться к методу, как к обычной переменной
    (4) Если же нам необходимо позволить пользователю изменять имя мы создадим метод,
        который будет принимать новое значение имени и заменять старое значение
'''
#Пример для (1) - (3) пунктов
##class MyClass:
##    def __init__(self, name):
##        self._name = name # (1) Написали нижнее подчеркивание, дабы его спрятать(к примеру)
##    @property             # (2) Создали обертку для функции, чтобы позволяла выводить спрятанную переменную
##    def name(self):
##        return self._name
##a = MyClass('Ваня')       # (3) Можем спокойно выводить имя, без вызова функции, а как переменную
##print(a.name)
##
###Пример для (4)
##class MyClass:
##    def __init__(self, name):
##        self._name = name 
##    @property             
##    def name(self):
##        return self._name
##    @name.setter            # (4) Создали для изменения имени
##    def name(self, value):
##        self._name = value
##
##a = MyClass('Ваня')       
##a.name = 'Сергей' #Поменяли имя
##print(a.name)

#-------------------------------------------------------------------------------------------------------------------------------------
#                                           Основы ООП 4 курс
'''
    Представим ситуацию, что у нас есть родительский и дочерние классы, а в каждом из них
    есть метод с одинаковым названием. Какой метод вызовется при обращении через
    экземпляр дочернего класса? Правильный ответ - метод из дочернего класса. Это и есть так
    называемое переопределение методов. Когда мы наследуемся от какого то класса и
    изменяем поведение метода так, как на требуется
'''

##class Parent:
##    def say_hello():
##        print('Привет Я метод родительского класса')
##class Children(Parent):
##    def say_hello():
##        print('Привет Я метод дочернего класса')
##
##child = Children
##child.say_hello() # Вызовится из дочернего класса

#-------------------------------------------------------------------------------------------------------------------------------------
#                                       Полиморфизм и Перегрузка операторов
'''
    Перегрузка операторов — один из способов реализации полиморфизма, когда мы можем         возможность одного и того же метода действовать по-разному в разных ситуациях
    задать свою реализацию какого-либо метода в своём классе.

    Полиморфизм – это способность одного и того же объекта вести себя по-разному в
    зависимости от того, в контексте какого класса он используется.
'''
#Пример:
'''
class Animal:
    def __init__(self, name): #Создали (индивидуальное) инициализацию для объекта Animal
        self.__name = name
        print('Объект создан') #Смотрим, что объект создан
        print(self.__name) # Так как мы применили принцип инкапсуляции,то мы не можем её вызвать вне класса, но можем посмотреть, что было в этой переменной, если засунем print в тот класс, который нам нужен

    def get_name(self):
        return self.__name # Так как мы применили принцип инкапсуляции, то не можем её применить в ДОЧЕРНЕМ КЛАССЕ. Однако, тогда можно создать функцию, благодаря которой мы проходим через препятсвие

    def say(self):
        print(f"{self.__name} говорит") #Сейчас пойдет пример принципа ПОЛИМОРФИЗМА

class Dog(Animal):
    def __init__(self, name): #Создали (индивидуальное) инициализацию для объекта Dog - пожеланию её можно было не писать
        super().__init__(name) #Создали SUPER, чтобы он связывался с РОДИТЕЛЬСКИМ КЛАССОМ (преемственность)
        print('Собака создана') #Смотрим, что объект создан
    def say(self):
        print(f"{self.get_name()} говорит ГАВ ГАВ ГАВ")

kot_boris = Animal('Борис') #т.е. создали переменную и присвоили ей РОДКласс, передавая аргумент параметра (Тоже самое, что и  a = Animal('Борис')) \\ -> Вызывается print, который был применен в классе 
Jorik = Dog('Жорик') #   \\ -> Вызывается print, который был применен в классе
kot_boris.say() #Вспомни, как вызываются функции. А они вызываются через точку и название переменной со скобками
Jorik.say()
'''

#   СМОТРИ В ЭЛЕКТРОННОМ ФОРМАТЕ МЕТОДЫ И КОМАНДЫ :)

'''
    Давайте попробуем заставить СЛОЖЕНИЕ например УМНОЖАТЬ - это перегрузка
'''

##class Test(int):
##    def __init__(self, num) -> None: # Стрелка - это указатель возврата функции
##        super().__init__()
##        self.num = num
##    def __add__(self, num2):
##        return self.num * num2
##a = Test(5)
##print(a + 10)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                       перегрузка и полиморфизм
#Пример полиморфизма (еще один)
##a = [1,2,3]
##a.append(10)
##print(a)

'''
#Создали правило,где нельзя добавлять в список!
'''
'''
class List(list):#наследуемся от list
    #не пишем init - то стандартно используется init родителя
    def append(self, n):
        return f"НЕльзя добавлять элемент {n} в список"
    def remove(self,number):
        for i in range(len(x)):
            x[i] = x[i] ** 2
            
x = List([1,2,3,5])
print(x.append(100))
#Можем удалить из списка
x.remove(3) #Удалет похожий элемент (не удаляет по ИНДЕКСУ)
print(x)
'''

''' методы с помощью которых происходит математические действия! их можно переделать под себя
# __add__(self,other) - сложение (x + y)
# __sub__(self, other) - вычитание (x - y).
# __mul__(self, other) - умножение (x * y).
# __truediv__(self, other) - деление (x / y).
# __floordiv__(self, other) - целочисленное деление (x // y).
# __mod__(self, other) - остаток от деления (x % y).
# __divmod__(self, other) - частное и остаток (divmod(x, y)).
# __pow__(self, other[, modulo]) - возведение в степень (x ** y, pow(x, y[, modulo])).
# # __add__(self, other) - сложение. x + y.
# # __sub__(self, other) - вычитание (x - y).
# # __mul__(self, other) - умножение (x * y).
# # __truediv__(self, other) - деление (x / y).
# # __floordiv__(self, other) - целочисленное деление (x // y).
# # __mod__(self, other) - остаток от деления (x % y).
# # __lt__(self, other) - x < y .
# # __le__(self, other) - x ≤ y.
# # __eq__(self, other) - x == y.
# # __ne__(self, other) - x != y
# # __gt__(self, other) - x > y.
# # __ge__(self, other) - x >= y.
# # __len__(self) - длина объекта.
'''

#Пример перегрузки

##class MyInt(int):
##    # Если def __ini__ не пишем, то применяется __init__ родителя
##    def __add__(self, other):#оператор +
##        return f"Сложение наоборот: {self - other}"
##    def __gt__(self, other): #оператор > self - является переменной x
##        if int(self) > other:
##            return f"{self} больше чем {other}"
##        elif int(self) < other:
##            return f"{self} меньше чем {other}"
##        else:
##            return "Они равны"
##    def __len__(self, other):
##        
##        
##    
##x = MyInt(100)
##print(x + 400)
##print(x > 1000)
##print(x > 100)
##print(x > 10)
'''
Задачка
доп задание Переопределить функцию len для нахождения длины списка/строки, чтобы он выводил всегда число 25
__len__ ....
'''
##class Test(str):
##    def __len__(self):
##        return 25
##x = Test('Колбаса')
##print(len(x))

