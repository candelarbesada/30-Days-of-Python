# Day 11 - Level 3

print("------ IS PRIME ------")
def is_prime(num):
    num_str = str(num)
    sum_dig = 0
    for i in num_str:
        sum_dig += int(i)

    if int(num_str[-1]) % 2 == 0 and num > 2:
        return False
    elif int(num_str[-1]) % 5  == 0 and num > 5:
        return False
    elif sum_dig % 3 == 0 and num > 3:
        return False
    elif num % 7 == 0 and num > 7:
        return False
    elif num % 11 == 0 and num > 11:
        return False
    elif num % 13 == 0 and num > 13:
        return False
    elif num % 17 == 0 and num > 17:
        return False
    else:
        return True
print(is_prime(221))
print(is_prime(257))


print("\n------ UNIQUE ITEMS ------")
def unique_items(lst):
    uniq = set(lst)
    for item in uniq:
        lst.remove(item)
    if lst == []:
        return True
    else:
        return False
print(unique_items([1, 2, 3, 4, 5]))
print(unique_items([1, 2, 3, 4, 5, 1]))


print("\n------ SAME DATA TYPE ------")
def same_data_type(lst):
    t = type(lst[0])
    for item in lst:
        if t == type(item):
            continue
        else:
            return False
    return True
print(same_data_type([1, 2, 3, 4, 5]))
print(same_data_type([1, 2, 3, 'hola', 4, 5]))


print("\n------ VALID PYTHON VARIABLE ------")
def valid_python_variable(var):
    if var[0] == '_' or var[0].isalpha():
        for i in var:
            if not i.isalnum() and i != '_':
                return False
        return True
    else:
        return False
print(valid_python_variable("good_variable"))
print(valid_python_variable("1_bad"))
print(valid_python_variable("also-bad"))


print("\n------ COUNTRIES ------")
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Data.countries_data import countries_data

def most_spoken_languages(num=10):
    count = dict()
    for c in countries_data:
        for l in c['languages']:
            if l in count.keys():
                count[l] += 1
            else:
                count[l] = 1
    languages_dict = sorted(count.items(), key = lambda x: x[1], reverse=True)[:num]
    lang = []
    for d in languages_dict:
        lang.append(d[0])
    return lang
print(most_spoken_languages())

def most_populated_countries(num=10):
    return [c['name'] for c in sorted(countries_data, key= lambda x: x['population'], reverse=True)[:num]]
print(most_populated_countries())