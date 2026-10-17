# Day 2: 30 Days of python programming

first_name = 'Tony'
last_name = 'Stark'
full_name = 'Anthony Edward Stark'
country = 'USA'
city = 'New York City'
age = 38
year = 2008
is_married = True
is_light_on = False
has_kids, wife = True, 'Pepper'


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(has_kids))
print(type(wife))


print(len(first_name))
print(len(last_name))


num_one = 5
num_two = 4
print(f'Num1: {num_one}, Num2: {num_two}')
total = num_one + num_two
print(f'Total: {total}')
diff = num_one - num_two
print(f'Diff: {diff}')
product = num_one * num_two
print(f'Product: {product}')
division = num_one / num_two
print(f'Division: {division}')
remainder = num_two % num_one
print(f'Remainder: {remainder}')
exp = num_one ** num_two
print(f'Exp: {exp}')
floor_division = num_one // num_two
print(f'Floor division: {floor_division}')



radius = 30
area_of_circle = 3.14*(radius**2)
circum_of_circle = 2*3.14*radius
print(f'Radius: {radius}m | Area: {area_of_circle}m2 | Circumference: {circum_of_circle}m')

radius = float(input('Choose the radius: '))
area_of_circle = 3.14*(radius**2)
circum_of_circle = 2*3.14*radius
print(f'Radius: {radius}m | Area: {area_of_circle}m2 | Circumference: {circum_of_circle}m')


first_name = input('What is your name? ')
last_name = input('What is your last name? ')
country = input('Which country are you from? ')
age = input('How old are you? ')

print(first_name, last_name, country, age)

