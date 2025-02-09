student=[]
def add_student():
    name=input("Name of student:\t")
    roll=int(input("Roll number of student:\t"))
    age=int(input("Age of student:\t"))
    s={
        "name":name,
        "roll":roll,
        "age":age
    }
    student.append(s)
    print("student added successfully")
def display_student():
    for std in student:
        print(f"Name:{std["name"]}\nRoll no.:{std["roll"]}\nAge:{std["age"]}")
    
def search_student():
    roll=int(input("enter a roll no. to search:"))
    for std in student:
        if std["roll"]==roll:
            print(f"Name:{std["name"]}\nRoll no.:{std["roll"]}\nAge:{std["age"]}")
            return
    print("student not found ")
def update_student():
    roll=int(input("enter a roll number to update student detail:"))
    for std in student:
        if std["roll"]==roll:
            x=int(input("1.for name update\n2.for roll no. update\n3.for age update"))
            if x==1:
              std["name"]=(input("enter new name"))
            elif x==2:
                std["roll"]=int(input("enter new roll no."))
            elif x==3:
                std["age"]=int(input("Enter new age"))
            else:
                print("invalid number")
    


def delete_student():
    roll=int(input("enter a roll no. to search:"))
    for std in student:
        if std["roll"]==roll:
            student.remove(std)
            print("student was delete from list")
        return
    print("student not found")
    return
print("---Student Management System---")

while 1:

        print("\n1.Add_Student\n2.Display_Student\n3.Search_Student\n4.Update _Student\n5Delete_Student\n6Exit")
        choice=int(input("Enter your choice(1-6):"))
        print(choice)
        if choice==1:
            add_student()
        elif choice==2:
            display_student()
        elif choice==3:
            search_student()
        elif choice==4:
            update_student()
        elif choice==5:
            delete_student()
        elif choice ==6:
                 
         break
        else:
            print("please enter your choice from (1-6)")
        
            


