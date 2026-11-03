# Day 18 - Level 3

import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    return re.sub(r'[^a-zA-Z ]', '', sentence)
print(clean_text(sentence))

def most_frequent_words(sentence, num):
    words = set(sentence.split(' '))
    dict_words = dict()
    for w in words:
        dict_words[w] = len(re.findall(r'\b'+ w + r'\b', sentence, re.I))
    return [word for word in sorted(dict_words.items(), key=lambda x: x[1], reverse=True)][:num]
print(most_frequent_words(clean_text(sentence), 3))