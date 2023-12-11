import os
from helper import *
from enum import Enum


class Actions(Enum):
    PRINT = 1
    ADD = 2
    DELETE = 3
    SEARCH = 4
    EXIT = 5


animals = []
my_data_file = "list.json"


def menu():
  print("==Zoo Menu==")
  for x in Actions:
    print(f'{x.name} - {x.value}')
  return input("Enter your selection: ")


def main():
    os.system('cls')
    global animals
    # calls the function to read the animals list from file (in helper.py)
    animals = read_animals(my_data_file)

    while (True):
        userSelection = menu()
        # menu logic with calls to functions from helper.py
        if Actions(int(userSelection)) == Actions.EXIT: exit_func(animals, my_data_file)
        elif Actions(int(userSelection)) == Actions.PRINT: print_func(animals)
        elif Actions(int(userSelection)) == Actions.ADD: add_func(animals)
        elif Actions(int(userSelection)) == Actions.DELETE: del_func(animals)
        elif Actions(int(userSelection)) == Actions.SEARCH: search_func(animals)


if __name__ == '__main__':
    main()
