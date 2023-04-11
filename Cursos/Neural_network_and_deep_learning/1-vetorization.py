import numpy as np

def iterative_sum(arr_x, arr_y, n):
    arr_z = []
    for i in range(0, n):
        arr_z = arr_x[i] + arr_y[i]

    return arr_z

def vectorized_sum (arr_x, arr_y):
    return arr_x + arr_y

#Creating two arrays with 10.000.000 elements
num_elements = 10000000
arr_x = np.random(num_elements)
arr_y = np.random(num_elements)

#Sum every element and save into another array
arr_z1 = iterative_sum(arr_x, arr_y, num_elements)
arr_z2 = iterative_sum(arr_x, arr_y)


