# Day 9 - Level 2

score = int(float(input('Enter your score: ')))
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Grade: F')


month = input('Enter the month: ')
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
if month in autumn:
    print('Season: Autumn')
elif month in winter:
    print('Season: Winter')
elif month in spring:
    print('Season: Spring')
elif month in summer:
    print('Season: Summer')
else:
    print('You entered an invalid month')


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit)
    print(fruits)
