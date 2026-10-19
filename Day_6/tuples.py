# Day 6

tple = tuple()
sisters = ('Sabrina', 'Chappel', 'Dua', 'Charli')
brothers = ('Tony', 'Scott', 'Steve', 'Peter')
siblings = brothers + sisters
print(siblings)
print(len(siblings))

family_members = siblings + ('Josh', 'Emily')
print(family_members)

siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

fruits = ('Apple', 'Pear', 'Orange', 'Pinapple')
vegetables = ('Cucumber', 'Pepper', 'Onion', 'Squash')
animal_products = ('Milk', 'Cheese', 'Bacon', 'Egg')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

if len(food_stuff_tp) % 2 != 0:
    middle = food_stuff_tp[len(food_stuff_tp)//2]
else:
    middle = food_stuff_tp[len(food_stuff_tp)//2:(len(food_stuff_tp)//2)+2]
print(middle)

print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)