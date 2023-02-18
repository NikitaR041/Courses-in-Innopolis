if __name__ == '__main__':
    print('Вы зашли в саму программу, где происходят вычислительные действия')

def add(a, b):
    return a + b

def sub(a, b):
    if a > b:
        return a - b
    elif a == b:
        return a - b
    else:
        return f"У вас отрицательное число {a - b}"


def mul(a, b):
    return a * b


def div(a, b):
    x = input('Для продолжения действия, что вы хотите Целое или Дробное число(для этого выберете Ц или Д): ')
    if x == 'Ц':
        if b == 0:
            return f"Деление на ноль недоступен"
        else:
            return a // b
    else:
        if b == 0:
            return f"Деление на ноль недоступен"
        else:
            return a / b

def numbersys(number,system):
    '''Урезанная функция перевода из 10 в любую другую, кроме как больше 10'''
    result = ''
    while number > 0:
        if system > 10: return f"Простите основание больше 10 пока не доступен"
        result = str(number%system) + result
        number//=system
    return result