# Day 19 - Level 2
import re

mails = []

with open('./files/email_exchanges_big.txt') as f:
    lines = f.read().splitlines()
    for l in lines:
        words = l.split(' ')
        for w in words:
            if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', w):
                mails.append(w)

print(f"First 10 mails: {mails[:10]}")


def find_most_common_words(file, num):
    dict_words = dict()
    with open(f'./files/{file}') as f:
        lines = f.read().lower().splitlines()
        for l in lines:
            words = l.split()
            for w in words:
                if w in dict_words.keys():
                    dict_words[w] += 1
                else:
                    dict_words[w] = 1
    return [(x[1], x[0]) for x in sorted(dict_words.items(), key=lambda x: x[1], reverse=True)[:num]]
print(f"Most common words in sample.txt: {find_most_common_words('sample.txt', 5)}")
print(f"Most common words in Obama's speech: {find_most_common_words('obama_speech.txt', 5)}")
print(f"Most common words in Michelle's speech: {find_most_common_words('michelle_obama_speech.txt', 5)}")
print(f"Most common words in Trump's speech: {find_most_common_words('donald_speech.txt', 5)}")
print(f"Most common words in Melania's speech: {find_most_common_words('melania_trump_speech.txt', 5)}")


import re
from files.stop_words import stop_words

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split(' ')

def remove_support_words(words):
    return [word for word in words if word not in stop_words]


def check_similarity(text1, text2):
    words1 = remove_support_words(clean_text(text1))
    words2 = remove_support_words(clean_text(text2))
    common_words = set(words1) & set(words2)
    sim = len(common_words)/len(words1) * 100
    return sim

with open('./files/michelle_obama_speech.txt') as f:
    with open('./files/melania_trump_speech.txt') as f2:
        text1 = f.read()
        text2 = f2.read()
        print(f"Similarity between Melania's speech and Michelle's speech: {check_similarity(text1, text2)}")


print(f"10 most common words in Romeo and Juliet: {find_most_common_words('romeo_and_juliet.txt', 10)}")


import csv
with open('./files/hacker_news.csv') as f3:
    lines = f3.read().lower().splitlines()
    num_lines_dict = dict()
    for l in lines:
        if 'python' in l:
            if 'python' in num_lines_dict.keys():
                num_lines_dict['python'] += 1
            else:
                num_lines_dict['python'] = 1
        if 'javascript' in l:
                    if 'javascript' in num_lines_dict.keys():
                        num_lines_dict['javascript'] += 1
                    else:
                        num_lines_dict['javascript'] = 1
        if 'java' in l and 'javascript' not in l:
                    if 'java' in num_lines_dict.keys():
                        num_lines_dict['java'] += 1
                    else:
                        num_lines_dict['java'] = 1
    print(num_lines_dict)

