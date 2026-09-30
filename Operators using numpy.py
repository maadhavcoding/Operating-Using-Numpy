import numpy as np
arr = np.linspace(0, 9, 10, dtype=int)
print("Original array:")
print(arr)
new_arr = arr.copy()
new_arr[new_arr % 2 != 0] = -1
print("\nArray after replacing odd numbers with -1:")
print(new_arr)
two_d_array = arr.reshape(2, 5)
print("\n2-D array with two rows:")
print(two_d_array)
even_sum = 0

for num in arr:
    if num % 2 == 0:
        even_sum += num

print("\nSum of all even numbers:", even_sum)