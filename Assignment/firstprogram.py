#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.

import numpy as np

arr1=(np.zeros(10)).astype(int)
print(arr1)

arr2=(np.ones(10)).astype(int)
print(arr2)

arr3=np.full(10,5)
print(arr3)
