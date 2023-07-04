import numpy as np

# Create arrays
array_1d = np.arange(10)
print(array_1d)

array_2d = np.zeros((3, 3))
print(array_2d)

array_3d = np.ones((2, 3, 4))
print(array_3d)

random_integers = np.random.randint(0, 101, size=10)
print(random_integers)

random_floats = np.random.random(10)
print(random_floats)

equally_spaced = np.linspace(0, 1, 5)
print(equally_spaced)

equally_spaced = np.linspace(0, 10, 5)
print(equally_spaced)

equally_spaced = np.linspace(-1, 1, 5)
print(equally_spaced)

angles = np.linspace(0, 2 * np.pi, 100)
sine_values = np.sin(angles)
print(sine_values)

# Scalar Operations:

array = np.array([[1, 2], [3, 4]])
multiplied_array = array * 2
print(multiplied_array)

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
added_array = array + 5
print(added_array)

array = np.array([[1, 4, 9, 16, 25, 36]])

square_root_array = np.sqrt(array)
print(square_root_array)
