#frozenset
s={1,5,9}
print(frozenset(s))

#frozenset are immutable
s.add(5)
print(s)

#clear
s.clear()
print(s)

#copy
a = {1, 2, 3, 4}
b = a.copy()
print(b)

#changes made if = is given
a=b
a.add(7)
print(b)

#changes not made in shallow copy
a={5,6,7}
b=a.copy()
a.add(9)
print(b)

#pop
a={9,10,23}
a.pop()
print(a)

#remove
c={89,78,"te"}
c.remove(78)
print(c)

#isdisjoint-return true if no common element in both sets
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))

#issubset-true if all elements in B are present in true
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

#issuperset-true if all elemnts are in the Bs
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
print(A.issuperset(B))
