"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""
import task_template as texts

#Variables
registered_users = {'bob': '123',
                    'ann': 'pass123',
                    'mike': 'password123',
                    'liz': 'pass123'}
sep = '-'*40
words = ''
upper_case = []

#Login
user_name = input('Enter username: ')
user_password = input('Enter password: ')
if registered_users.get(user_name) == user_password:
  print(f'{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}')
else:
  print('unregistered user, terminating the program...')

#Text selection
text_choice = input('Enter a number btw. 1 and 3 to select: ')
print(sep)
if not text_choice.isnumeric() or int(text_choice) - 1 not in range(0,3):
  print('Invalid text selection, terminating the program...')

#Text analysis
text_list = texts.TEXTS[int(text_choice) - 1].split()
words = len(text_list)
for i in text_list:
  if i[0].isupper():
    upper_case.append(i)
  else:
    continue
print(upper_case)