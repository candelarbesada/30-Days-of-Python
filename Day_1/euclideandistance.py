# Find an Euclidean distance between (2, 3) and (10, 8)
# https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.

x = (2, 3)
y = (10, 8)

dist2 = ((x[0]-y[0])**2) + ((x[1]-y[1])**2)
dist = dist2 ** 0.5

print(f"Euclidean distance between x = {x} and y = {y} is {dist}")