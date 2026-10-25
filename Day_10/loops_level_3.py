# Day 10 - Level 3

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Data.countries_list import countries

print("------ COUNTRIES WITH 'LAND' ------")
for c in countries:
    if 'land' in c:
        print(c)


print("\n------ FRUIT LIST REVERSED ------")
lst = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(lst)-1, -1, -1):
    print(lst[i])


from Data.countries_data import countries_data

print("\n------ LANGUAGES ------")
languages = list()
for d in countries_data:
    for key, value in d.items():
        if key == 'languages':
            for i in value:
                languages.append(i)
        continue
print(set(languages))
print(f"Number of unique languages: {len(set(languages))}")


freq = dict()
for l in languages:
    if l in freq.keys():
        freq[l] += 1
    else:
        freq[l] = 1
print(f"MOST SPOKEN LANGUAGES: {sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]}")
print(f"MOST POPULATED COUNTRIES: {[c['name'] for c in sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]]}")




