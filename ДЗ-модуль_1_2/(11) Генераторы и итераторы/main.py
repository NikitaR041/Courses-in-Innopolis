'''
Данные об email-адресах учеников хранятся в словаре:

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],

              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],

              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],

              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],

      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],

      	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}



Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.

При решении использовать генератор словарей.
'''

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],

              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],

              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],

              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],

      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],

      	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

#print(*sorted(['{a}@{b}'. format(a = username, b = adres[0]) for adres in emails.items() for username in adres[1]]), sep='\n')

#print(emails.items())#Создается двумерный массив

some_gen = (name+'@'+domen for domen, names in emails.items() for name in names)
print(list(sorted(some_gen)))
#эквивалентно что и
