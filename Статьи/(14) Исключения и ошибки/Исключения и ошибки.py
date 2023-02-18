'''
    Исключения в Python

    1 конструкция try - except
        Здесь except -> ПЕРЕХВАТЫВАЕТ любую ошибку, поэтому нужно быть осторожным с этимъ
        Но после слова except конкретизировать, какая может появится ошибка!

        Можно несколько раз писать except, если хотим более конркретизировать

В статейке показаны примеры ошибок, здесь приведу некоторые из них:

NameError
print(x)

SyntaxError
x=5asas

ModuleNotFoundError или ImportError
import functoolsasda

AttributeError
x = [12,12,3]
x.appendad(10) -> возможно покажет, что вы хотели написать 'append'?

IndentationError
if x == 5:
print('afas')

ZeroDivisionError
print(100/0)

'''
#Пример
##y = 100
##x = 1
##x = x -1
##try:
##    print(y/x)
##except ZeroDivisionError:
##    print('Ошибка')
##x = x - 1


'''
Задачки
1)Открыть файл используюя with open. Проверять через try...except наличие ошибки "Такого файла нет"
2)Обработать добавление в файл только чисел через int(input), отловить для этого какую-то ошибку,
  если пытаемся ввести через int(input) строку, а не число
3)Написать функцию date, принимающую 3 аргумента - день,месяц и год
  Вернуть True, если такая дата есть в нашем календаре, и False иначе.
  При написании использовать исключения.
'''
#1
'''
try:
    f = open('test.txt')
except FileNotFoundError:
    print('Такого файла нет')
'''
#2
'''
try:
    with open('file.txt','w') as f:
        print('Этот файл открылся')
        try:
            number = int(input('введите число '))
            f.write(str(number))
        except ValueError:
            pass #Ничего не делать
except  FileNotFoundError:
    print('Такого файла нет')
'''
#3 Не однозначность
try:
    def date(day,month,year):
        if day in a and mount in a and year in a:
            return "Все впорядке"
        else:
            return 'не впорядке'

    a = ['15','Май','2007']
        
    x,y,z = map(str, input('Введите дату, месяц и год(через пробел) ').split())

    print(date(x,y,z))
except:
    pass
