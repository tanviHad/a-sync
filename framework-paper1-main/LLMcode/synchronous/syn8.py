import numpy as np

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

# Add two arrays
result_arr = arrayOne + arrayTwo
print(result_arr)

# Modify result array by calculating the square of each element
result_arr_sq = result_arr**2
print(result_arr_sq)