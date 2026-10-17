# Day 3

age = 23
height = 1.65
complex_number = 1 + 4j


print("TRIANGLE:")
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area = 0.5 * base * height_triangle
print(f"The are of the triangle is {area}")

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")


print("RECTANGLE:")
length_rectangle = float(input("Enter length: "))
width_rectangle = float(input("Enter width: "))
area_rectangle = length_rectangle * width_rectangle
print(f"The are of the rectangle is {area_rectangle}")



print("CIRCLE:")
radius = float(input("Enter radius: "))
area_circle = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius
print(f"The are of the circle is {area_circle} and the circumference of the circle is {circumference}")



slope_1 = 2
x_intercept = (1, 0)
y_intercept = (0, -2)
print(f"Slope1: {slope_1}, X Intercept: {x_intercept}, Y Intercept: {y_intercept}")

slope_2 = (10 - 2) / (6 - 2)
euclidean_distance = ((6 - 2)**2 + (10 - 2)**2)**0.5
print(f"Slope2: {slope_2}, Euclidean distance between (2, 2) and (6, 10): {euclidean_distance}")


x = -3
y = x**2 + 6*x + 9
print(f"Value of y: {y}")


print(f"Length of 'python': {len("python")}")
print(f"Length of 'dragon': {len("dragon")}")
print(len('python') > len('dragon'))


print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in 'python' and 'on' not in 'dragon')

print(str(float(len('python'))))

modulus_even = 4 % 2
modulus_uneven = 5 % 2

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)



hours = int(float(input("Enter hours: ")))
rate_per_hour = int(float(input("Enter rate per hour: ")))
pay = hours * rate_per_hour
print(f"Your weekly earning is {pay}")


years = int(float(input("Enter number of years you have lived: ")))
seconds = 60 * 60 * 24 * 365
print(f"You have lived for {seconds} seconds")


for i in range(1, 6):
    print(i, 1, i**2, i**3)