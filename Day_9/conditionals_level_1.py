# Day 9 - Level 1

age = int(float(input('Enter your age: ')))
if age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f"You need {18-age} more years to learn to drive")



my_age = 23
your_age = int(float(input('Enter your age: ')))
diff = abs(my_age - your_age)
str = f"You are {diff} year" if diff == 1 else f"You are {diff} years"
if my_age > your_age:
    str += ' younger than me'
elif my_age < your_age:
    str += ' older than me'
else:
    str = 'We are the same age'
print(str)


number_1 = int(float(input('Enter number one: ')))
number_2 = int(float(input('Enter number two: ')))
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_1 < number_2:
    print(f"{number_1} is smaller than {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")

