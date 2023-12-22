Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))
#Example using map() with lambda:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  

#Example using filter() with lambda:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

#Example using sorted() with lambda:
pairs = [(1, 5), (2, 3), (4, 1), (3, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  
