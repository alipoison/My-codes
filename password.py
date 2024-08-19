import random
import string


def index_choose(harchi):
    return random.randint(0, len(harchi)-1)


def index_choose_integers(harchi):
    integers = [x for x in harchi if isinstance(x, int)]
    return random.choice(integers)


def find_position_of_number(num, lst):
    position = lst.index(num)
    return position + 1


def uppercase(harchi, harchi_Adad):
    return harchi(harchi_Adad).upper()


def turn_to_int(harchi, harchi2):
    for item in harchi:
        try:
            harchi2.append(int(item))
        except ValueError:
            harchi2.append(item)

def replace_number_with_character(lst, lst2, character, new_number):
    index = lst.index(character)
    lst2[index] = new_number
    return lst2


password = "a.ali.a03"

list_password = list(password)

password_2 = list_password

list_integers_password = []

turn_to_int(password_2, list_integers_password)

choosen_integers = index_choose_integers(list_integers_password)

choosen_index = index_choose(list_integers_password)

index_teller = []

index_teller.append(find_position_of_number(choosen_integers, list_integers_password))

password_2.append(replace_number_with_character(list_integers_password, password_2, choosen_index, index_teller))

print(list_integers_password)


