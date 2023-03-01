'''
Создать декоратор, измеряющий время выполнения функции.
Для расчета времени ознакомьтесь с модулем datetime.
'''
import datetime
##print(datetime.datetime.now())
def decorator(some_func):
    def wrapper():
        start = (datetime.datetime.now())
        some_func()
        end = (datetime.datetime.now())
        print(end - start)
    return wrapper

@decorator
def printt():
    print('Куча мала')

@decorator
def gen_list():
    y = [i for i in range(1,1000)]
printt()
gen_list()
