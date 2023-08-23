"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""
import sys

#Texts
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Variables
users = {
  'bob': '123',
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
word_length = []

#Login
user_name = input('Enter username: ')
user_password = input('Enter password: ')
if users.get(user_name) == user_password:
  print(f'''{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}''')
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
text_list = TEXTS[int(text_choice) - 1].split()

for i in text_list:
  if i.istitle():
    title_words.append(i)
  elif i.isupper():
    upper_case_word.append(i)
  elif not i.istitle() and not i.isnumeric() and not i.isupper():
    lower_case_word.append(i)
  elif i.isnumeric():
    numerics.append(i)

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
  else:
    text_list_alphanum.append(i)

#Sorting word length
for i in text_list_alphanum:
  word_length.append(len(i))
sorted_word_length = sorted(word_length)

#User output
print(f'''There are {words} words in the selected text.
There are {title_words_count} titlecase words.
There are {upper_case_word_count} uppercase words.
There are {lower_case_word_count} lowercase words.
There are {numerics_count} numeric strings.
The sum of all the numbers {numerics_sum}''')

#Graph
max_symbols = 0
for i in (sorted_word_length):
 occ_symbols = sorted_word_length.count(i)
 if occ_symbols > max_symbols:
    max_symbols = occ_symbols

print(f'''{sep}
LEN|  OCCURENCES{(max_symbols - 10) * " "}|NR.
{sep}''')

for i in set(sorted_word_length):
 occ_symbols = sorted_word_length.count(i) * "*"
 if i < 10:
    print(f'  {i}|{occ_symbols} {(max_symbols - len(occ_symbols)) * " "} |{sorted_word_length.count(i)}')
 else:
    print(f' {i}|{occ_symbols} {(max_symbols - len(occ_symbols)) * " "} |{sorted_word_length.count(i)}')
