'''
Реализовать класс и переопределить магические методы базовых математических операции (сложение, вычитание, умножение, деление), добавив туда выводы в консоль текущего действия.

Например: при умножении выводится сообщение, что происходит умножение.
'''
class Test(int):
    '''инициализация'''
    def __init__(self, num):
        super().__init__()
        self.num = num
        
    '''cложение'''
    def __add__(self, num2):
        print('Процесс сложения')
        return self.num + num2
    '''Вычитание'''
    def __sub__(self, num3):
        print('Процесс вычитания')
        return self.num - num3
    '''Умножение'''
    def __mul__(self,num4):
        print('Процесс умножения')
        return self.num * num4
    '''Деление'''
    def __truediv__(self,num5):
        print('Процесс деления')
        return self.num / num5
    
a = Test(10)
b = Test(2)
c = Test(3)
d = Test(2)
f = Test(5)
print(a + b)
print(a - c)
print(a * c)
print(a / d)


