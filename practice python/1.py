"""
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
duplicate.sort(reverse=True)
print(Remove(duplicate))
"""
"""
def para_function(**kwargs):
    return kwargs['salary'],kwargs['Hero']

print(para_function(Hero='Rajni',salary=300000))
"""
"""
n=int(input())
a=hex(n).replace("0x","").upper()
print(a)
"""
"""
def sumVowel(string):
    a=input()
    n = len(string(a))
    sum = 0
    string = string.lower()
    for i in range(0, n):
        s = string[i]
    if (s=="a" or s == "e" or s == "i" or s == "o" or s == "u"):
        sum += ((n - i) * (i + 1))
        return sum
"""
"""
class MovieName:
    def __init__(self,hero,villian):
        self.hero=hero
        self.villian=villian
    def description(self):
        return f" releasing movie with hero {self.hero} and villian is {self.villian}"

m=MovieName("Prabhas",'Rana')
print(m.description())
#print(m.description())
"""
"""
class MyName:
    def __init__(self,firstname,lastname,age,profession):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.profession=profession
    def description(self,user_name="User ID"):
        return f"{user_name} is {self.lastname}  {self.firstname} with age {self.age} and profession is {self.profession}."
firstname=input("enter first name:")
lastname=input("enter last name:")
age=int(input("enter age:"))
profession=input("enter profession:")
m=MyName(firstname,lastname,age,profession)
print(m.description())
"""
"""
class Zoo:
    def __init__(self, category, food, living, age):
        self.category = category
        self.food = food
        self.living = living
        self.age = age
    def description(self):
        return f"{self.category} eat {self.food} and lives in {self.living}"


class Lions(Zoo):
    def vara(self):
        return f"{self.category} is king of jungle and age is {self.age}"


z = Zoo('Lions', "meat", 'Jungle',20)
print(z.description())  #Accessing parent class method using parent method.
li = Lions('lioness', 'meat', 'jungle',20)
print("calling parent class method using child class object :", li.description()) #Accessing parent class method using child object
print("calling child class method using child class object :", li.vara())  #Accessing child method using child object.
"""
"""
class Class1:
    def m(self):
        print("In Class1")
       
class Class2(Class1):
    def l(self):
        print("In Class2")
 
class Class3(Class1):
    def k(self):
        print("In Class3") 
        
class Class4(Class2, Class3):
    def n(self):
        print("in class4")
     
obj = Class4()
obj.m()
obj.l()
"""
"""
class MyName:
    def __init__(self,firstname,lastname,age,profession):
        self.__firstname=firstname
        self.lastname=lastname
        self.age=age
        self._profession=profession
    def description(self,user_name="User ID"):
        return f"{user_name} is {self.lastname} {self.__firstname} with age {self.age} and profession is {self._profession}."
firstname=input("enter first name:")
lastname=input("enter last name:")
age=int(input("enter age:"))
profession=input("enter profession:")
m=MyName(firstname,lastname,age,profession)
print(m.description())
print(m._profession) #accecing public variable with single underscrore
print(m._MyName__firstname) # used to access private variables
"""
"""
class employee(object):
    def __init__(self):   
        self.name = 1234
        self._age = 1234
        self.__salary = 1234
 
object1 = employee()
print(object1.name)
print(object1._age)
print(object1.__salary)
"""
