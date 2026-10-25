# Day 11 - Level 2

print("------ EVENS AND ODDS ------")
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num+1):
        if i%2 == 0:
            evens += 1
        else:
            odds += 1
    return f'The number of odds is {odds}.\nThe number of evens is {evens}'
print(evens_and_odds(100))


print("\n------ FACTORIAL ------")
def factorial(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res
print(factorial(5))


print("\n------ IS EMPTY ------")
def is_empty(param):
    return len(param) == 0
print(is_empty([]))


print("\n------ LISTS ------")
def calculate_mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)
print(f"Mean: {calculate_mean([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")

def calculate_median(lst):
    sorted(lst)
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2+1] + lst[len(lst)//2+2]) / 2
    else:
        return lst[len(lst)//2+1]
print(f"Median: {calculate_median([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")

def calculate_mode(lst):
    cont = {}
    for i in lst:
        if i in cont.keys():
            cont[i] += 1
        else:
            cont[i] = 1
    return sorted(cont.items(), key=lambda x: x[1], reverse=True)[0][0]
print(f"Mode: {calculate_mode([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")

def calculate_range(lst):
    lst.sort()
    return lst[-1]-lst[0]
print(f"Range: {calculate_range([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")

def calculate_variance(lst):
    mean = calculate_mean(lst)
    sum = 0
    for i in lst:
        sum += (i - mean)**2
    return sum / len(lst)
print(f"Variance: {calculate_variance([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")

def calculate_std(lst):
    return calculate_variance(lst) ** 0.5
print(f"Standard deviation: {calculate_std([1, 2, 3, 4, 5, 0, 3, 6, 2, 1])}")


print("\n------ GREET ------")
def greet(name='Guest'):
    print(f'Hello, {name}!')
greet()
greet('Alice')


print("\n------ SHOW ARGS ------")
def show_args(**args):
    str = 'Received: '
    for key, value in args.items():
        str += f"{key} : {value}, "
    print(str)
show_args(name='Alice', age=30, city='New York')
