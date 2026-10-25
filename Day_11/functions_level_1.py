# Day 11

print("------ ADD TWO NUMBERS ------")
def add_two_numbers(num1, num2):
    return num1+num2

print(add_two_numbers(3, 5))


print("\n------ AREA OF CIRCLE ------")
def area_of_circle(radius):
    return 3.14*(radius**2)

print(area_of_circle(10))


print("\n------ ADD ALL NUMBERS ------")
def add_all_nums(*args):
    sum = 0
    for i in args:
        if not isinstance(i, float) and not isinstance(i, int):
            sum = "There are elements in the list which are not numeric"
            break
        else:
            sum += i
    return sum
print(add_all_nums(2, 3, 5, -5))
print(add_all_nums(2, 5, 'hola', 10))


print("\n------ CONVERT CELSIUS TO FAHRENHEIT ------")
def convert_celsius_to_fahrenheit(temp):
    return temp * (9/5) + 32
print(convert_celsius_to_fahrenheit(15))


print("\n------ CHECK SEASON ------")
def check_season(month):
    if month.lower() in ['march', 'april', 'may']:
        return 'Spring'
    elif month.lower() in ['june', 'july', 'august']:
        return 'Summer'
    elif month.lower() in ['september', 'october', 'november']:
        return 'Autumn'
    elif month.lower() in ['december', 'january', ' february']:
        return 'Winter'
    else:
        return 'Invalid month'
print(check_season('October'))
print(check_season('hola'))


print("\n------ CALCULATE SLOPE ------")
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)
print(calculate_slope(1, 2, 8, 5))


print("\n------ SOLVE QUADRATIC EQUATION ------")
def solve_quadratic_eqn(a, b, c):
    aux = b**2 - 4*a*c
    if aux >= 0:
        x = (-b + (aux**0.5)) / 2*a
        y = (-b - (aux**0.5)) / 2*a
        return (x, y) if x != y else x
    else:
        return 'The equation does not have a solution'
print(solve_quadratic_eqn(2, 2, 1))
print(solve_quadratic_eqn(1, 2, 1))
print(solve_quadratic_eqn(1, 2, 0))


print("\n------ PRINT LIST ------")
def print_list(lst):
    for i in lst:
        print(i)
print_list(['banana', 'orange', 'mango'])


print("\n------ REVERSE LIST ------")
def reverse_list(lst):
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])
reverse_list(['banana', 'orange', 'mango'])


print("\n------ CAPITALIZE LIST ITEMS ------")
def capitalize_list_items(lst):
    lst_2 = []
    for i in lst:
        lst_2.append(i.capitalize())
    return lst_2
print(capitalize_list_items(['banana', 'orange', 'mango']))


print("\n------ REMOVE ITEM ------")
def remove_item(lst, item):
    lst_2 = []
    for i in lst:
        if i != item:
            lst_2.append(i)
        else:
            continue
    return lst_2
print(remove_item(['banana', 'orange', 'mango', 'apple'], 'apple'))


print("\n------ SUM OF NUMBERS ------")
def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
print(sum_of_numbers(5))


print("\n------ SUM OF ODDS ------")
def sum_of_odds(num):
    sum = 0
    for i in range(num+1):
        if i%2 != 0:
            sum += i
        else:
            continue
    return sum
print(sum_of_odds(5))

print("\n------ SUM OF EVENS ------")
def sum_of_evens(num):
    sum = 0
    for i in range(num+1):
        if i%2 == 0:
            sum += i
        else:
            continue
    return sum
print(sum_of_evens(5))