#if else statement
a=10
if (a>18):
    print("Elgible to vote")
else:
   print("Not Elgible to vote")
   
#elif satement
n=5;
if (n>0):
       print("It is positive number")
elif (n<0):
   print("It is negative number")
else:
   print("It is whole number")
#if else chain
age=15
if age==18:
      print("can vote")
   
else: 
    if age>18:
     print("do your duty of voting")
     
    else:
       
        if age<18:
            print("wait to vote")
       
        else: 
            print("go to ec office")


# if-elif statement example
 
country="others"
 
if country == "india":
    print("Give adhar card")
 
elif country == "others":
    print("no adhar card")
 
elif country == "india and another country":
    print("Dual citzenship")
 
else:
    print("check your country name")

