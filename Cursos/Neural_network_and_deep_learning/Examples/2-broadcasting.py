import numpy as np

a = np.array([100, 200, 300])
b = np.array([1000, 2000, 3000])
c = a+b
print(c)


a = np.array(
    [
        [100, 200, 300],
        [101, 201, 301],
        [102, 202, 302]
    ]
)
# Since array A has three rows, but array b only has one, 
# the array b will receive a copy of itself until it fills the number of rows from the a array
c = a+b
print(c)


# Now the array A is 3x3 but the array B is 3x1
# Then python will make a copy so B will become 3x3
# So the value of each row will be copied twice in the new columns 

b = np.array(
    [
        [500], 
        [600], 
        [800]
    ]
)
print(b.shape)
c = a + b
print("\n"+str(c))
