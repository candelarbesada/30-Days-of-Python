# Day 5

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}. Max age: {max_age}")
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

if len(ages) % 2 != 0:
    median = ages[len(ages) // 2]
else:
    median = (ages[len(ages) // 2] + ages[(len(ages) // 2) + 1]) / 2
print(f"Median: {median}")

average = 0
for i in range(len(ages)):
    average += ages[i]/len(ages)
print(f"Average: {average}")

range_age = max_age - min_age
print(f"Range: {range_age}")

print(f"Min - average: {abs(min_age - average)}. Max - average: {max_age - average}")


from countries_list import countries
print(len(countries))
if len(countries) % 2 != 0:
    print(countries[len(countries) // 2])
else:
    print(countries[len(countries) // 2 : (len(countries) // 2) + 2])

first_half = countries[:len(countries)//2]
second_half = countries[len(countries)//2:]
print(first_half)
print(len(first_half))
print(second_half)
print(len(second_half))

china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(f"China: {china}\nRussia: {russia}\nUSA: {usa}\nScandic: {scandic}")