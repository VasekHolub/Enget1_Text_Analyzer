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

#Main loop

while True:
  user_name = input('Enter username: ')
  user_password = input('Enter password: ')
  login = {user_name: user_password}
  if registered_users.get(user_name) == user_password:
    print(f'{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}')
  else:
    print('unregistered user, terminating the program...')
    break
  text_choice = input('Enter a number btw. 1 and 3 to select: ')
  print(sep)
  if not text_choice.isnumeric() or int(text_choice) - 1 not in range(0,3):
    print('Invalid text selection, terminating the program...')
    break
  else:
    print(texts.TEXTS[int(text_choice) - 1])
    break
  