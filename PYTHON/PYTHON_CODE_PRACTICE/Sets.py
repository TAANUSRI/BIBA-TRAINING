#creating set
set={"hello","java","python"};
print(set)

#add element
set.add("sql")
print(set)

#set with different values
set={"hello",40,4.5,False}
print(set)

# find number of elements
n = {2,4,6,8}
print(n)
print('Total Elements:', len(n))

#union
a={1,2,3,4}
b={4,5,6,7}
print(a.union(b))

#intersection
a={1,2,3,4}
b={4,5,6,7}
print(a.intersection(b))

#difference
a={1,2,3,4}
b={4,5,6,7}
print(b.difference(a))

