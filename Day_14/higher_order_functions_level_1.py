# Day 14 - Level 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(x):
    return x ** 2
print(list(map(square, numbers)))


for c in countries:
    print(c)


for n in names:
    print(n)


for num in numbers:
    print(num)