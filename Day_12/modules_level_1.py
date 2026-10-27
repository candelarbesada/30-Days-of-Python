# Day 12 - Level 1

import random
import string

def random_user_id():
    char = string.ascii_letters + string.digits
    id = ''
    for i in range(6):
        id+= random.choice(char)
    return id
print(f"Random user id: {random_user_id()}")


def user_id_gen_by_user():
    char = int(input("How many characters? "))
    num = int(input("How many IDs to be generated? "))
    alpha_num = string.ascii_letters + string.digits
    ids = []
    for i in range(num):
        id = ''
        for j in range(char):
            id += random.choice(alpha_num)
        ids.append(id)
    return ids
print(f"\nRandom user ids with input: {user_id_gen_by_user()}")


def rgb_color_gen():
    string = 'rgb('
    for i in range(3):
        string += str(random.randint(0, 255))
        if i < 2:
            string += ', '
    string += ')'
    return string
print(f"\nRgb color: {rgb_color_gen()}")
