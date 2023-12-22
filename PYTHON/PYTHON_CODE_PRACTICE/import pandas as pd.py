import pandas as pd
s = pd.Series([1, 6, 8])
print(s)
#creating data frame
a = pd.DataFrame({'Name': ['Rita', 'lata', 'tom'],'Age': [25, 30, 22],'Salary': [50000, 60000, 45000]})
print(a)
#mean finding
total_salary=a['Salary'].mean()
#conitions
young_worker=a[a['Age']<25]
print (total_salary)
print(young_worker)
#sorting
sorted_salary = a['Salary'].sort_values()
print("Original DataFrame:\n", a)
print("\nSorted 'Salary' column:\n", sorted_salary)

import numpy as np
# Create a  array
a = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
b=np.array([[6, 7, 5], [7, 4, 8], [1, 4, 7]])
# Sorting 
c= np.sort(a, axis=0,kind='quicksort')
# Unary operations
d = a+b
e = a**2

# Universal function 
f = np.sqrt(a)
g=np.abs(a)

# linspace 
h = np.linspace(0, 1, 5)

# Flatten the array
i = b.flatten()

# Size, shape, and dimension
array_size = a.size
array_shape = a.shape
print("Data Type:", array_dtype)array_dimension = a.ndim

# Data type of the array
array_dtype = a.dtype

# Display results
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print("Size:", array_size)
print("Shape:", array_shape)
print("Dimension:", array_dimension)

