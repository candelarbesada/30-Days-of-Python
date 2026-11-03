# Day 18 - Level 1

import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.split(' ')
dict_words = dict()
for w in words:
    if w not in dict_words.keys():
        dict_words[w] = len(re.findall(w, paragraph))
mode = [word[0] for word in sorted(dict_words.items(), key=lambda x: x[1], reverse=True)][0]
print(f"Most frequent word in the paragraph: {mode}")


text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
points = re.findall(r'[\-]?\d+', text)
sorted_points = sorted(points, key = lambda x: int(x))
distance = int(sorted_points[-1]) - int(sorted_points[0])
print(f"Points: {points}.\nSorted points: {sorted_points}.\nDistance: {distance}")

