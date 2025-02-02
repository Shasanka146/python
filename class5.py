#class and object
class Student:
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
print(student1.upper_name())


