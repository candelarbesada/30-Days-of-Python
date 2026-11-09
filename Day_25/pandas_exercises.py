# Day 25

import pandas as pd

hacker_news = pd.read_csv('./hacker_news.csv')

print(hacker_news.head())
print(hacker_news.tail())

title = hacker_news['title']
print(title)

print(hacker_news.shape)

df_python = hacker_news[hacker_news['title'].str.contains('python', case=False, na=False)]
df_javascript = hacker_news[hacker_news['title'].str.contains('javascript', case=False, na=False)]
print(df_python.head())
print(df_python.shape)
print(df_javascript.head())
print(df_javascript.shape)