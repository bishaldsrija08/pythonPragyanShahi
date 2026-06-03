import numpy as np
import time

# --- Basic setup ---
# Python list
py_list = list(range(1_000_000))

# NumPy array
np_array = np.arange(1_000_000)

# --- Performance test: sum ---
start = time.time()
sum_list = sum(py_list)
end = time.time()
print(f"Sum with list: {sum_list}, Time: {end - start:.6f} seconds")

start = time.time()
sum_array = np.sum(np_array)
end = time.time()
print(f"Sum with NumPy: {sum_array}, Time: {end - start:.6f} seconds")

# --- Element-wise operations ---
# Lists need loops or comprehensions
list_squared = [x**2 for x in py_list[:10]]
print("List squared (first 10):", list_squared)

# NumPy does it directly
array_squared = np_array[:10] ** 2
print("NumPy squared (first 10):", array_squared)

# --- Memory comparison ---
print("List type:", type(py_list[0]))
print("NumPy type:", np_array.dtype)