
"""
x=[i for i in range (5)] #list comphrehension
print(x)

"""
"""
x=[i : i+2 for i in range(10)]
print(x)               #dic comprehension
"""
"""
a=int(input())
n=hex(a).replace("0x", "").upper()
print(n)
"""
"""
a=int(input())
n=oct(a).replace("0o","")
print(n)
"""
"""
a=input()
n=ord(a)   #giving chareters
print(n)
"""
"""
import array as arr
My_Array=arr.array('i',[1,2,3,4])
print(My_Array)
t(n)
"""
"""
def Newfunc():
    print("Hi, Welcome to Edureka")
Newfunc(); #calling the function
"""
"""
class Employee:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = 20000
E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print(E1.name)
print(E1.age)
print(E1.salary)
"""
"""
a = lambda x,y : x*y
print(a(5, 6)) #An anonymous function is known as a lambda function.
               # This function can have any number of parameters but, can have just one statement.
"""
"""
n=input()
a=n.capitalize().help(n)
print(a)
"""
"""
import array as arr
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
a.pop(0)
print(a)
"""
"""
a="edureka python"
print(a.split("edureka"))
"""
"""
a=int(input("Enter the terms"))
f=0;#first element of series
s=1#second element of series
if a==0:
   print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a): 
         print(next,end=" ")
         f=s
         s=next
"""
"""
class MovieName:
    pass
m = MovieName()
"""
"""
class MovieName:
    print("lucky")
MovieName()
"""
"""
class Zoo:
    def __init__(self, category, food, living):
        self.category = category
        self.food = food
        self.living = living

    def description(self):
        return f"{self.category} eat {self.food} and lives in {self.living}"


class Lions(Zoo):
    def intro(self):
        return f"{self.category} is king of jungle"


z = Zoo('Lions', "meat", 'Jungle')
print(z.description())  #Accessing parent class method using parent method.
li = Lions('lioness', 'meat', 'jungle')
print("calling parent class method using child class object :", li.description()) #Accessing parent class method using child object
print("calling child class method using child class object :", li.intro())  #Accessing child method using child object.
"""
"""
class Zoo:
    def __init__(self, category, food, living):
        self.category = category
        self.food = food
        self.living = living

    def description(self):
        return f"{self.category} eat {self.food} and lives in {self.living}"
z=Zoo("lion","meat","jungle")
print(z.description())
"""
"""
# Python Program to Reverse a Number using Recursion
 
Num = int(input("Please Enter any Number: "))
Result = 0
def a(Num):
    if(Num > 0):
        global Result
        Reminder = Num %10
        Result = (Result *10) + Reminder
        a(Num //10)
    return Result
 
Result = a(Num)
print("n Reverse of entered number is = %d" %Result)
"""
# Get the number from user manually 
num = int(input("Enter your favourite number: "))
 
test_num = 0  # Initiate value to null
 
# Check using while loop
while(num>0):
    remainder = num % 10
    test_num = (test_num * 10) + remainder
    num = num//10
print("The reverse number is : {}".format(test_num))