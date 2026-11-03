# Day 19 - Level 1

def count_lines_words(text):
    lines = len(text.splitlines())
    words = 0
    for line in text.splitlines():
        words += len(line.split(' '))
    print(f"The text has {lines} lines and {words} words")



with open('./files/obama_speech.txt') as f1:
    obama_text = f1.read()
    count_lines_words(obama_text)


with open('./files/michelle_obama_speech.txt') as f2:
    michelle_obama_text = f2.read()
    count_lines_words(michelle_obama_text)


with open('./files/donald_speech.txt') as f3:
    donald_text = f3.read()
    count_lines_words(donald_text)


with open('./files/melania_trump_speech.txt') as f4:
    melania_trump_text = f4.read()
    count_lines_words(melania_trump_text)


import json
def most_spoken_languages(filename, num):
    with open(filename, encoding='utf-8') as f:
        countries_data = json.load(f)
        languages_count = dict()
        for country in countries_data:
            for language in country['languages']:
                if language in languages_count.keys():
                    languages_count[language] += 1
                else:
                    languages_count[language] = 1
        return [(count, language) for language, count in sorted(languages_count.items(), key=lambda x: x[1], reverse=True)[:num]]

print(most_spoken_languages('../Data/countries_data_json.json', 10))
print(most_spoken_languages('../Data/countries_data_json.json', 3))



def most_populated_countries(file, num):
    with open(file, encoding='utf-8') as f:
        countries_data = json.load(f)
        return [{'country': c['name'], 'population': c['population']} for c in sorted(countries_data, key=lambda x: x['population'], reverse=True)[:num]]
print(most_populated_countries('../Data/countries_data_json.json', 10))
print(most_populated_countries('../Data/countries_data_json.json', 3))