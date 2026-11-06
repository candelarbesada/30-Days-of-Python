# Day 20

import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

romeo_and_juliet = "https://www.gutenberg.org/files/1112/1112-0.txt"
romeo_and_juliet_response = requests.get(romeo_and_juliet)
romeo_and_juliet_text = romeo_and_juliet_response.text

words = romeo_and_juliet_text.split()
words_dict = dict()
for w in words:
    if w in words_dict.keys():
        words_dict[w] += 1
    else:
        words_dict[w] = 1
print([x[0] for x in sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:10]])

cats_api = "https://api.thecatapi.com/v1/breeds"
load_dotenv()
headers = {'x-api-key': os.environ.get('API_KEY_CATS')}
cats_response = requests.get(cats_api, headers=headers)
cats = cats_response.json()

weights = []

import re
import statistics 

for cat in cats:
    weight = cat['weight']['metric']

    if re.match(r'^\d+(\.\d+)?\s*-\s*\d+(\.\d+)?$', weight):
        min_w, max_w = map(float, weight.split('-'))
        weights.append((min_w + max_w) / 2)

print('\n------ WEIGHT ------')
print('Min:', min(weights))
print('Max:', max(weights))
print('Mean:', statistics.mean(weights))
print('Median:', statistics.median(weights))
print('Standard deviation:', statistics.stdev(weights))


lifespans = []

for cat in cats:
    lifespan = cat['life_span']

    if re.match(r'^\d+(\.\d+)?\s*-\s*\d+(\.\d+)?$', lifespan):
        min_life, max_life = map(float, lifespan.split('-'))
        lifespans.append((min_life + max_life) / 2)

print('\n------ LIFESPAN ------')
print('Min:', min(lifespans))
print('Max:', max(lifespans))
print('Mean:', statistics.mean(lifespans))
print('Median:', statistics.median(lifespans))
print('Standard deviation:', statistics.stdev(lifespans))


print("\n------ FREQ BY COUNTRY ------")
country_breeds = {}
for cat in cats:
    country = cat['origin']
    if country in country_breeds:
        country_breeds[country] += 1
    else:
        country_breeds[country] = 1
country_breeds = sorted(
    country_breeds.items(),
    key=lambda x: x[1],
    reverse=True
)
for country, count in country_breeds:
    print(f'{country}: {count}')



# skipped the countries exercise as being practically the same


from bs4 import BeautifulSoup
url = "https://archive.ics.uci.edu/datasets"
uci_response = requests.get(url)
soup = BeautifulSoup(uci_response.text, 'html.parser')
print("\n------ BEAUTIFUL SOUP ------")
print(soup.title.text)
