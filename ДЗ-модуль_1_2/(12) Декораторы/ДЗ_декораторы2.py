'''
Реализовать программу, которая рассчитывает площадь и периметр прямоугольника и обработать все возможное ошибки с помощью try..except.
'''
try:
    x,y = map(int,input('Введите два значения, чтобы найти площадь и периметр прямоугольника(через пробел): ').split())
    if x <= 0 or y <= 0:
        raise ValueError('Не могут быть значения меньше нуля!')
except ArithmeticError:
    print('ArithrmeticError')
except ValueError:
    print('ValueError')
else:
    print(f"Площадь прямоугольника: {x*y}, периметр: {2*x + 2*y}")
finally:
    print('Конец работы')
