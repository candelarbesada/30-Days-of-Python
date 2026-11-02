# Day 14 - Level 2

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


new_lst = list(map(lambda x: x.upper(), countries))
print(new_lst)

new_lst_2 = list(map(lambda x: x**2, numbers))
print(new_lst_2)

new_lst_3 = list(map(lambda x: x.upper(), names))
print(new_lst_3)


print(list(filter(lambda x: 'land' in x, countries)))
print(list(filter(lambda x: len(x) == 6, countries)))
print(list(filter(lambda x: len(x) >= 6, countries)))
print(list(filter(lambda x: x[0] == 'E', countries)))
print(list(map(str.upper, filter(lambda country: len(country) > 6, countries))))


def get_string_lists(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, str):
            new_lst.append(i)
    return new_lst
print(get_string_lists(['hola', 1, [2, 3], 'adios']))


from functools import reduce
print(reduce(lambda res, current: res + ", " + current, countries[:-1]) + f' and {countries[-1]} are north European countries')


import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Data.countries_list import countries as countries_list


def categorize_countries(pattern):
    res = []
    for i in countries_list:
        if pattern.lower() in i.lower():
            res.append(i)
    return res
print(categorize_countries('island'))


import string
def dictionary_function():
    dictionary = dict()
    letters = string.ascii_uppercase
    for l in letters:
        for c in countries_list:
            if c[0] == l:
                if l in dictionary.keys():
                    dictionary[l] += 1
                else:
                    dictionary[l] = 1
    return dictionary
print(dictionary_function())


def get_first_ten_countries():
    return countries_list[:10]
print(get_first_ten_countries())


def get_last_ten_countries():
    return countries_list[-10:]
print(get_last_ten_countries())

