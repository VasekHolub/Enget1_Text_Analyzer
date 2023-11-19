"""
projekt_1.py: první projekt do Engeto Online Python Akademie (Text_analyzer)
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""
import sys
import re

texts = [
    """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]


def user_validation(users: dict, user_name: str, user_password: str) -> None:
    sep = "-" * 40
    if users.get(user_name) == user_password:
        print(
            f"""{sep}\nWelcome to the app {user_name}\nWe have 3 texts to be analyzed.\n{sep}"""
        )
    else:
        print("Unregistered user, terminating the program...")
        sys.exit()


def user_login() -> None:
    users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    user_validation(users, user_name, user_password)


def text_selection(texts: list) -> int:
    text_choice = input("Enter a number btw. 1 and 3 to select: ")
    if not text_choice.isnumeric() or int(text_choice) not in range(1, len(texts) + 1):
        print("Invalid text selection, terminating the program...")
        sys.exit()
    return int(text_choice)


def text_nonalnum_char_strip(text_to_analyse: str) -> list:
    removed_lines = text_to_analyse.replace("\n", " ")
    return re.sub(r"[^a-zA-Z0-9- ]", "", removed_lines)


def text_analysis(striped_text: list) -> list:
    total_words = len(striped_text)
    title_words = 0
    upper_case_words = 0
    lower_case_words = 0
    numerics = list()
    for i in striped_text:
        if i.istitle() and i.isalpha():
            title_words += 1
        elif i.isupper() and i.isalpha():
            upper_case_words += 1
        elif not i.istitle() and not i.isnumeric() and not i.isupper():
            lower_case_words += +1
        elif i.isnumeric():
            numerics.append(int(i))
    numeric_count = sum(numerics)
    return (
        total_words,
        title_words,
        upper_case_words,
        lower_case_words,
        numerics,
        numeric_count,
    )


def sort_word_length(striped_text: list) -> list:
    word_length = list()
    for i in striped_text:
        word_length.append(len(i))
    sorted_word_length = sorted(word_length)
    return sorted_word_length


def analysis_user_output(analysed_text: list) -> None:
    print(
        f"""There are {analysed_text[0]} words in the selected text.\nThere are {analysed_text[1]} titlecase words.\nThere are {analysed_text[2]} uppercase words.\nThere are {analysed_text[3]} lowercase words.\nThere are {len(analysed_text[4])} numeric strings.\nThe sum of all the numbers {analysed_text[5]}"""
    )


def determine_max_symbol_length(sorted_word_length: list) -> int:
    max_symbols = 0
    checked = list()
    for i in sorted_word_length:
        if i not in checked:
            occ_symbols = sorted_word_length.count(i)
            checked.append(i)
        if occ_symbols > max_symbols:
            max_symbols = occ_symbols
    return max_symbols


def graph_printer(sorted_word_length: list) -> None:
    sep = "-" * 40
    max_symbols = determine_max_symbol_length(sorted_word_length)
    print(f"""{sep}\nLEN|  OCCURENCES{(max_symbols - 10) * " "}|NR.\n{sep}""")
    for i in set(sorted_word_length):
        occ_symbols = sorted_word_length.count(i) * "*"
        if i < 10:
            print(
                f'  {i}|{occ_symbols} {(max_symbols - len(occ_symbols)) * " "} |{sorted_word_length.count(i)}'
            )
        else:
            print(
                f' {i}|{occ_symbols} {(max_symbols - len(occ_symbols)) * " "} |{sorted_word_length.count(i)}'
            )


def main():
    user_login()
    striped_text = text_nonalnum_char_strip(texts[text_selection(texts) - 1])
    print(striped_text)
    text_to_analyse = striped_text.split()
    analysed_text = text_analysis(text_to_analyse)
    sorted_word_length = sort_word_length(text_to_analyse)
    analysis_user_output(analysed_text)
    graph_printer(sorted_word_length)


if __name__ == "__main__":
    main()
