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
text_list_alphanum = []

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
words = len(text_list)
title_words_count = len(title_words)
upper_case_word_count = len(upper_case_word)
lower_case_word_count = len(lower_case_word)
numerics_count = len(numerics)
numerics_sum = sum((int_numerics))

# Determining word length
  # Striping non alnum characters from the word list
for i in text_list:
  if not i.isalnum():
    for x in i:
      if not x.isalnum():
        text_list_alphanum.append(i.replace(x,'')) 
        continue
  else:
    text_list_alphanum.append(i)

  #Sorting word length
word_lengt = []
for i in text_list_alphanum:
  word_lengt.append(len(i))
sorted_word_length = sorted(word_lengt)

#User output
print(f'''There are {words} words in the selected text.
There are {title_words_count} titlecase words.
There are {upper_case_word_count} uppercase words.
There are {lower_case_word_count} lowercase words.
There are {numerics_count} numeric strings.
The sum of all the numbers {numerics_sum}
{sep}
LEN|  OCCURENCES  |NR.
{sep}''')

#Graph construction
for i in sorted_word_length:
 print(f'{i}|{sorted_word_length.count(i) * "*"} {sorted_word_length.count(i)}')
