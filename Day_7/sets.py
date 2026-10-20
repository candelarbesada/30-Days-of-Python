# Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Meta', 'CapGemini'])
print(it_companies)
it_companies.remove('CapGemini')
print(it_companies)

# remove() returns error if the element doesn't exist. discard() doesn't raise any errors

print(A | B)
print(A & B)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A | B, '\n', B | A)
print(A.symmetric_difference(B))
del A
del B


ages_set = set(age)
print(len(age), len(ages_set))

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split(' ')
unique_words = set(words)
print(len(unique_words))
