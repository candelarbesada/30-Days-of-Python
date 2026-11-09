# Day 24

import numpy as np

python_list = [1, 2, 3, 4, 5]
print('Type: ', type(python_list))
print(python_list)

numpy_array_from_list = np.array(python_list)
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(type(numpy_array_from_list))
print(numpy_array_from_list)
print(type(numpy_array_from_list2))
print(numpy_array_from_list2)
print('shape of array: ', numpy_array_from_list.shape)

numpy_bool_array = np.array([0, 1, -2, 0, 0], dtype=bool)
print(numpy_bool_array)

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
print('shape of two dimensional list: ', numpy_two_dimensional_list.shape)

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_typle: ', python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

three_by_four_array = np.array([[0, 1, 2, 3], [4,5,6,7],[8,9,10,11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)


int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

print('The size:', numpy_array_from_list.size)
print('The size:', numpy_two_dimensional_list.size)


numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)


two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)


numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)



np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))



random_float = np.random.random()
print(random_float)
random_floats = np.random.random(5)
print(random_floats)
random_int = np.random.randint(0, 11)
print(random_int)
random_int = np.random.randint(2,10, size=4)
print(random_int)
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)



four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num=10))
# not to include the last value in the interval
print(np.linspace(1.0, 5.0, num=5, endpoint=False))

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('std: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


a = [1,2,3]
# Repeat whole of 'a' two times
print('Tile: ', np.tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))


## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g))

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))

## Determinant 2*2 matrix
print(np.linalg.det(i))