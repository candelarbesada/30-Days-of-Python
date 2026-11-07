# Day 22

import requests
from bs4 import BeautifulSoup
import json

url1 = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url1)
soup = BeautifulSoup(response.text, 'html.parser')

data = {}
content = soup.find('main')
data['title'] = soup.title.get_text()
for element in content.find_all(['h2', 'h3', 'p', 'li']):
    text = element.get_text(strip=True)
    if text:
        data.setdefault('content', []).append(text)

with open('bu_facts_stats.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)



url2 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url2, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='wikitable')
headers = [th.get_text(' ', strip=True) for th in table.find_all('th')]
data = []

for row in table.find_all('tr'):
    cells = row.find_all('td', recursive=False)
    if len(cells) < 5:
        continue
    row_data = {}
    for i, cell in enumerate(cells):
        if i < len(headers):
            row_data[headers[i]] = cell.get_text(' ', strip=True)
    if row_data:
        data.append(row_data)

with open('presidents.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
