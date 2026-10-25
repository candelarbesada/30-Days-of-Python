# Day 10 - Level 2

sum_total = 0
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    sum_total += i
print(f"The sum of all number is {sum_total}")
print(f"The sum of all evens is {sum_even}. The sum of all odds is {sum_odd}")

