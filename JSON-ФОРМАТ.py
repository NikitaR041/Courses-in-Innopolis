## Json
'''
JSON - это такой тип данных от JAVA.SCRIPT, который используется при передаче данных С сайта В приложение В программу, С программы С приложения В сайт.
К примеру, вводишь пароль и логин в сайт, эти данные должны перейти в Python-программу, а это Python-программа осматривает эту информацию(обрабатывает).
В случае, что если пароль или логин введен не верно, то Python-программа отсылает ответ о том, что пользователь ввел пароль или логин не верно!
Действия : Пароль и логин переделывается в формат JSON и передается его к вам, точно также, когда Вы отправляете из Python-программу в формате JSON!
p.s. метод json уже используют как лет 20 назад, вот так вот!
'''
#json -> Pyrhon-словарь
#Как сохрать из Pyrhon-программу в JSON формат!

'''
В качестве ключа ОБЯЗАТЕЛЬНО СТРОКУ!!!!! А в качестве значения хоть что угодно, даже словарь, списки и тд

import json # Включаем библиотеку
info = { #Создали слловарь
        'ФИО' : 'Колбасевич Колбас Колбасович',
        'Оценки в школе': {'Математика': 5, 'Русский язык' : 2, 'Химия': 5},
        'Хобби' : ['Играть в футбол','Быть вкусным'],
        'Домашние животные':None #если ничего нет, то это отсутсвие, но этот None - тоже важная информация(данные)!
    }
'''
'''
info_json = json.dumps(info) # Переводит его в формат JSON
print(info_json)
'''
#Свехру: Выведит формат JSON, СМ НИЖЕ,как избежать этого!
'''
info_json = json.dumps(info,ensure_ascii = False) #второй параметр переводит его в формат python
print(info_json)
'''
#Сверху: Выведит в формат Python при помощи второго параметра
#Оставляем то, что внизу
'''
info_json = json.dumps(info,ensure_ascii = False, indent = 4) #Третий параметр выведит его в красивый формат json в python
print(info_json)                                              #Насамом деле просто ставит красивые отсупы в зависимости от цифр
'''

#Как сохранить из JSON формата в Python-программу
'''
Создаем файлик в формате JSON
'''
##with open('JSON-файлик.json','w') as file:
##    file.write(info_json)#Внимание создался JSON файлик, а чтобы создался в блокноте надо написать формат txt

#--------------------------------------------    
#Как считать из JSON формат в Python формат:
'''
Метод .loads, который переводит из JSON формат в Python формат, а точнее в словарь, тк мы же создавали словарь

with open('JSON-файлик.json','r') as file:
    info_from_json = json.loads(file.read())
print(info_file_json)
'''
###_ общий вид снизу
'''
import json # Включаем библиотеку
info = { #Создали слловарь
        'ФИО' : 'Колбасевич Колбас Колбасович',
        'Оценки в школе': {'Математика': 5, 'Русский язык' : 2, 'Химия': 5},
        'Хобби' : ['Играть в футбол','Быть вкусным'],
        'Домашние животные':None #если ничего нет, то это отсутсвие, но этот None - тоже важная информация(данные)!
    }
info_json = json.dumps(info,ensure_ascii = False, indent = 4) #Третий параметр выведит его в красивый формат json в python
print(info_json)                                              #Насамом деле просто ставит красивые отсупы в зависимости от цифр

with open('JSON-файлик.json','w+') as file:
    file.write(info_json)#Внимание создался JSON файлик, а чтобы создался в блокноте надо написать формат txt

with open('JSON-файлик.json','r') as file:
    info_from_json = json.loads(file.read())
print(info_from_json)
'''

###Задачка:
'''
доп-задача: Сохранить инфу в json файл от пользователя через input

import json
info = input('что тебе вчера приснилось ')
info_json = json.dumps(info,ensure_ascii=False,indent=3)
with open('file.json','w')as file:
    file.write(info_json)
print(info_json)
'''
