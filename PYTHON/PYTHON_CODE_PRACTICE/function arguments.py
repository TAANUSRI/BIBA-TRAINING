#Default arguments
def add(x,y=6):
    z=x+y
    print(z)
add(4)

#Keyword arguments
def emp(age,sex):
    print(age,sex)
emp(age=27,sex="male")
emp(sex="female",age=28)
 
 #Positional argument
def emp(age,sex):
    print("age of employee is",age)
    print ("gender of employee is",sex)
emp(27,"male")
emp("female",34)

#arbitary keyword operator
def fun(*argv):
    for fun in argv:
        print(fun)
fun("hello","my",)
