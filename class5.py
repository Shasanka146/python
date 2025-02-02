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
    print(f"Name:{i.name},address:{i.address}")



    




