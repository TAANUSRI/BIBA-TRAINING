Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> s = pd.Series([1, 6, 8])
>>> print(s)
0    1
1    6
2    8
dtype: int64
>>> #creating data frame
>>> a = pd.DataFrame({'Name': ['Rita', 'lata', 'tom'],'Age': [25, 30, 22],'Salary': [50000, 60000, 45000]})
>>> print(a)
   Name  Age  Salary
0  Rita   25   50000
1  lata   30   60000
2   tom   22   45000
>>> #mean finding
>>> total_salary=a['Salary'].mean()
>>> print (total_salary)
51666.666666666664
>>> #conitions
>>> young_worker=a[a['Age']<25]
>>> print(young_worker)
  Name  Age  Salary
2  tom   22   45000
>>> #sorting
>>> sorted_salary = a['Salary'].sort_values()
>>> print("Original DataFrame:\n", a)
Original DataFrame:
    Name  Age  Salary
0  Rita   25   50000
1  lata   30   60000
2   tom   22   45000
>>> print("\nSorted 'Salary' column:\n", sorted_salary)

Sorted 'Salary' column:
 2    45000
0    50000
1    60000
Name: Salary, dtype: int64
