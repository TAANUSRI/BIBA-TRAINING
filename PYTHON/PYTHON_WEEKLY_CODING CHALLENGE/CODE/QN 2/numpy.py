Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
# Create a  array
a = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
b=np.array([[6, 7, 5], [7, 4, 8], [1, 4, 7]])
print(a)
[[3 1 4]
 [1 5 9]
 [2 6 5]]
print(b)
[[6 7 5]
 [7 4 8]
 [1 4 7]]
# Sorting
c= np.sort(a, axis=0,kind='quicksort')
print(c)
[[1 1 4]
 [2 5 5]
 [3 6 9]]
# Unary operations
d = a+b
>>> print(d)
[[ 9  8  9]
 [ 8  9 17]
 [ 3 10 12]]
>>> e = a**2
>>> print(e)
[[ 9  1 16]
 [ 1 25 81]
 [ 4 36 25]]
>>> 
... # Universal function
>>> f = np.sqrt(a)
>>> g=np.abs(a)
>>> print(f)
[[1.73205081 1.         2.        ]
 [1.         2.23606798 3.        ]
 [1.41421356 2.44948974 2.23606798]]
>>> print(g)
[[3 1 4]
 [1 5 9]
 [2 6 5]]
>>> # linspace
>>> h = np.linspace(0, 1, 5)
>>> print(h)
[0.   0.25 0.5  0.75 1.  ]
>>> i = b.flatten()
>>> print(i)
[6 7 5 7 4 8 1 4 7]
>>> # Size, shape, and dimension
>>> array_size = a.size
>>> print("Size:", array_size)
Size: 9
>>> array_shape = a.shape
>>> print("Shape:", array_shape)
Shape: (3, 3)
>>> array_dimension = a.ndim
>>> print("Dimension:", array_dimension)
Dimension: 2
>>> array_dtype = a.dtype
>>> print("Data Type:", array_dtype)
Data Type: int32
