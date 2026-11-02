# Day 14 - Level 3

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Data.countries_data import countries_data

def sort_countries(key_order):
    return [c['name'] for c in sorted(countries_data, key=lambda c: c[key_order])]
print("Sorted by name: ", sort_countries('name'))
print("Sorted by capital: ", sort_countries('capital'))
print("Sorted by population: ", sort_countries('population'))


def most_spoken_languages(num):
    languages = dict()
    for c in countries_data:
        for l in c['languages']:
            if l in languages.keys():
                languages[l] += 1
            else:
                languages[l] = 1
    return [lang[0] for lang in sorted(languages.items(), key=lambda l: l[1], reverse=True)][:num]
print(most_spoken_languages(10))


def most_populated_countries(num):
    return [c['name'] for c in sorted(countries_data, key=lambda x: x['population'], reverse=True)][:num]
print(most_populated_countries(10))