'''
Реализовать родительский класс человека, а также дочерние классы директора, преподавателя и ученика.
Описать для каждого класса необходимые свойства и методы.

Важно: директор помимо своих обязанностей может также и преподавать (множественное наследование).
'''
class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    def say_Person(self):
        print('Привет, Я человек!')

class Students(Person):
    def __init__(self, height, weight, klass, name):
        super().__init__(height, weight)
        self.klass = klass
        self.name = name

    def say_Students(self):
        print(f"Привет! Я ученик {self.klass} класса, меня зовут {self.name}")

class Teacher(Person):
    def __init__(self, height, weight, lesson, name):
        super().__init__(height, weight)
        self.lesson = lesson
        self.name = name

    def say_Teacher(self):
        print(f"Здравствуйте, я учитель такого предмета, как {self.lesson}. Меня зовут {self.name}, будем знакомы!")

class Director(Teacher,Person):
    def __init__(self, height, weight, lesson,  name, status):
        super().__init__(height, weight, lesson, name)
        self.lesson = lesson
        self.status = status
        self.name = name
        
    def say_Director(self):
        print(f"Здравствуйте, я директор этой школы! Меня зовут {self.name}")
        print(f"Иногда я перподаю такой урок, как {self.lesson}")

person1 = Person(100,120)
person1.say_Person()

student1 = Students(180,80,10,'Максим')
student1.say_Students()

teacher1 = Teacher(180,70,'Физкультура','Василий')
teacher1.say_Teacher()

director1 = Director(160,80,'Математика','Директор школы', 'Борис')
director1.say_Director()

    
        
