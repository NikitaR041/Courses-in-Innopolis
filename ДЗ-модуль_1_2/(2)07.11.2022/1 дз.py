'''
Найдите сумму и произведение элементов списка. Результаты вывести в консоль.
'''
a = [1,2,6,8,9]

#Сумму элементов списка (простой способ):
print(sum(a))

#Другой способ суммы элементов списка:
sm = 0
for i in a:
  sm += i
print(sm)

#Нахождение произведения элементов списка:
d = 1 # ставим 1 так как всегда будет умножаться на 0, в консоли будет ответ 0
for i in a:
    d *= i
print(d)
