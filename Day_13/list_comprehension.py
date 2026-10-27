# Day 13

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print(f"Filter only negative and zero: {[i for i in numbers if i<=0]}")


list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nFlatten the list: {[num for sublist in list_of_lists for num in sublist]}")


list_of_tuples = [(i, *(i**p for p in range(6))) for i in range(11)]
print("\r",*list_of_tuples, sep="\n")


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_upper = [[c[0][0].upper(), c[0][0][:3].upper(), c[0][1].upper()] for c in countries]
print(f"\nUpper list: {countries_upper}")


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dict = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]
print("\r", *list_of_dict, sep="\n")


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_names = [f"{name} {surname}" for sublist in names for (name, surname) in sublist]
print(f"\nList names: {list_names}")


slope = lambda x1, x2, y1, y2: ((y2-y1)/(x2-x1))
print(slope(1, 7, 8, 2))