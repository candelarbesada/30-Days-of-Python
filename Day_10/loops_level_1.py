# Day 10 - Level 1
print("------ FOR LOOP ------")
for x in range(11):
    print(x)

print("\n------ WHILE LOOP ------")
y = 0
while y <= 10:
    print(y)
    y+=1

print("\n------ TRIANGLE ------")
z = 1
while z <= 7:
    print('#'*z)
    z+=1


print("\n------ NESTED LOOPS ------")
str = ""
for i in range(8):
    for j in range(8):
        str += "# "
    str += "\n"
print(str)


print("------ MULTIPLICATION ------")
for k in range(11):
    print(f"{k} x {k} = {k**2}")


print("\n------ LIST ------")
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lst:
    print(item)


print("\n------ EVEN NUMBERS ------")
for l in range(100):
    if l%2 == 0:
        print(l)


print("\n------ ODD NUMBERS ------")
for m in range(100):
    if m%2 != 0:
        print(m)