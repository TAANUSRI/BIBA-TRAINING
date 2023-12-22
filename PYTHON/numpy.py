import numpy as np
ar=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(type(ar))
print(ar.shape)
print(ar.size)
print(ar.ndim)
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='complex')

b=np.array((1,3),(5,8))
print(b)
# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
 # Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print(c)
 #creating tuple
 d=np.array([[1,2],[98,78]])
 print(d)
 # Create an array with random values
 e=np.random.random((2,3))
 print(e)

#operands
import numpy as np
a = np.array([[1, 2, 3], [6, 7, 8], [9, 8, 5]])
b = a + 1
print(b)
c=a-1
print(c)
d=a*2
print(d)
e=a/2
print(e)
f=a.T
print(f)
#unary operands
import numpy as np
a = np.array([[5, 6],[7, 8]])
b = np.array([[2, 3],[4, 5]])
c=print( a - b)
d=print(a / b)
e=print(a ** 2)
f=print(a % b)


#univeral operandds
import numpy as np
a = np.array([0, np.pi/3, 2*np.pi/3])
print(np.cos(a))
print(np.sin(a))
print(np.tan(a))
b = np.array([1, 2, 5, 10])
print(np.log(b))
c = np.array([2, 3, 4])
print(np.power(c, 2))
d = np.array([-1, -2, 3, -4])
print(np.abs(d))
#sort
import numpy as np
b = np.array([[7, 4, 9],[5, 2, 8],[3, 1, 6]])
print("Column-wise sort using quicksort:\n",np.sort(b, axis=0, kind='quicksort'))
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
values = [('John', 2010, 8.2),('Alice', 2009, 9.5),('Bob', 2010, 8.9),('Eva', 2009, 9.1)]
arr = np.array(values, dtype=dtypes)
print("\nStructured array sorted by graduation year and then cgpa:\n",np.sort(arr, order=['grad_year', 'cgpa']))
