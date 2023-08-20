"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""
import sys
import task_template as texts

#Variables
users = {'bob': '123',
          'ann': 'pass123',
          'mike': 'password123',
          'liz': 'pass123'}
sep = '-' * 40
title_words = []
upper_case_word = []
lower_case_word = []
numerics = []
int_numerics = []

#Login
user_name = input('Enter username: ')
user_password = input('Enter password: ')
if users.get(user_name) == user_password:
  print(f'{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}')
else:
  print('unregistered user, terminating the program...')
  sys.exit()

#Text selection
text_choice = input('Enter a number btw. 1 and 3 to select: ')
print(sep)
if not text_choice.isnumeric() or int(text_choice) - 1 not in range(0,3):
  print('Invalid text selection, terminating the program...')
  sys.exit()

#Text analysis
text_list = texts.TEXTS[int(text_choice) - 1].split()
words = len(text_list)
for i in text_list:
  if i.istitle():
    title_words.append(i)
  elif i.isupper():
    upper_case_word.append(i)
  elif not i.istitle() and not i.isnumeric() and not i.isupper():
    lower_case_word.append(i)
  elif i.isnumeric():
    numerics.append(i)
  else:
    continue

for i in numerics:
  int_numerics.append(int(i))

#Counts of occurrences
title_words_count = len(title_words)
upper_case_word_count = len(upper_case_word)
lower_case_word_count = len(lower_case_word)
numerics_count = len(numerics)
numerics_sum = sum((int_numerics))


print(title_words_count)
print(upper_case_word_count)
print(lower_case_word_count)
print(numerics_count)
print(numerics_sum)