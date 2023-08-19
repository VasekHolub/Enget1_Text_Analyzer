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
while True:
  user_name = input('Enter username: ')
  user_password = input('Enter password: ')
  login = {user_name: user_password}
  if registered_users.get(user_name) == user_password:
    print(f'{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}')
  else:
    print('unregistered user, terminating the program...')
    break