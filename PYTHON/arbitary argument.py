#arbitary keyword operator
def fun(*argv):
    for fun in argv:
        print(fun)
fun("hello","my","friends")

def fun (**kwargs):
    for key,value in kwargs.items():
        print(key,value)
fun(name="ria",age=90)
