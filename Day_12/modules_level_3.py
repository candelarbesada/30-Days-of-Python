# Day 12 - Level 3

import random

def shuffle_list(lst):
    len_list = len(lst)
    used = []
    new_list = lst.copy()
    i = 0
    while i < len_list-1:
        pos = random.choice(range(len_list-1))
        if pos not in used:
            new_list[pos] = lst[i]
            used.append(pos)
            i += 1
        else:
            continue
    return new_list
print(f"Shuffle list: {shuffle_list([1, 2, 3, 4, 5, 6])}")


def seven_random_numbers():
    lst = []
    i = 0
    while i < 7:
        num = random.randint(0, 9)
        if num not in lst:
            lst.append(num)
            i+=1
        else:
            continue
    return lst
print(f"Seven random numbers: {seven_random_numbers()}")
