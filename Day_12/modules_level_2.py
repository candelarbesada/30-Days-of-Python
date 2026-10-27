# Day 12 - Level 2

import string
import random

def list_of_hexa_colors(num):
    characters = string.digits + 'abcdef'
    lst = []
    for i in range(num):
        hexa = '#'
        for j in range(6):
            hexa += random.choice(characters)
        lst.append(hexa)
    return lst
print(f"List of random hexadecimal colors: {list_of_hexa_colors(6)}")


def list_of_rgb_colors(num):
    lst = []
    for i in range(num):
        rgb = 'rgb('
        for j in range(3):
            rgb += str(random.randint(0, 255))
            if j < 2:
                rgb += ', '
        rgb += ')'
        lst.append(rgb)
    return lst
print(f"List of random rgb colors: {list_of_rgb_colors(4)}")


def generate_colors(type, num):
    if type == "hexa":
        return list_of_hexa_colors(num)
    elif type == "rgb":
        return list_of_rgb_colors(num)
    else:
        return 'Wrong type'
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
