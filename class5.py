#class and object
"""class Student:
    def __init__(self,fname,lname,age,address):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.address=address


    def get_name(self):
        return self.fname+' '+self.lname
    
    def upper_name(self):
        return self.fname.upper()
    def update_address(self,address):
        self.address=address
    
student1=Student('shasanka','Acharya',20,'kathmandu')
student2=Student('bibek','Ghimire',19,'illam')
print(student2.age)
print(student1.get_name())
print(student1.upper_name())"""

#program to change address of student using class and object
"""
student=[]
class A:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def get_name(self):
        return self.name
    def address_update(self,address):
        self.address=address
    def __repr__(self):
       return (f"{self.name}{self.address}")

num=int(input("Enter the range of number:"))
for i in range(num):
    c=input(f"Enter {i+1}th name : ")
    d=input(f"Enter address:")
    std=A(c,d)
    student.append(std)
    
name=input("Enter the name to change address")
for i in student:
    print(i.name)
    if  i.name == name:
        new_add=input("Enter new address:")
        i.address = new_add
    else:
        print("student not found")

print(student)
for i in student:
    print(f"Name:{i.name},address:{i.address}")"""

"""
class Animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

    def speak(self):
        return "speak"
    def wag_tail(self):
        return "wag"
class Dog(Animal):
    def __init__(self,name,age,color,breed):
        super().__init__(self,name,age,color)
        self.breed=breed
    def speak(self):
        return "bark"

class Cat(Animal):
    def __init__(self,name,age,color,breed):
        super().__init__(self,name,age,color)
        self.breed=breed
    def speak(self):
        return "meow"
    
cat1=Cat('kitty',5,'black','persian')
print(cat1.speak())
dog1=dog('jonson',7,'golden','german-shepherd')
print(Dog1.speak())
"""

   #list compression technique     
# student1=[]
# for i in range(1,10):
#     student1.append(i)
# student2=[i for i in range(1,10)]
# print(student1,student2)
#comprehension of inheritance      
class Root:
    f='root'
class A(Root):
    f='A'
class B(Root):
    f='B'
class C(A,B):
    fx='C'

c=C()
print(c.f)
print(C.__mro__)
print([cls.__name__ for cls in C.__mro__])


    




