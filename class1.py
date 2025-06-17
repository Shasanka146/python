print('My First Python Class')
#Arthimetic operation
a="Shasanka Acharya"
print(a)
a=15
print(a)
b=20
print(b)
sum=a+b
sub=b-a
mul=a*b
div=a/b
print(sum)
print(sub)
print(mul)
print(div)
print(type(a))
a="shasanka acharya"
a=15

print(type(a))
print(str(a))
print(int(a))
print(float(a))


print(float(a))("enter a number")
b=input("enter a number")
print(a+b)


a=int(input("enter a number"))
b=int(input("enter a number"))
print(a+b)



#condition statement
"""if condition:
    ---
elif condition:
    ---
else condition:
    ---    """


"""a=int(input("enter a number"))
b=int(input("enter a number"))
if a>b:
    print('a is greater')
elif b>a: 
    print('b is greater')
else:
    print("equal")"""


#indexing
"""a="stri'ng"
print(a[0])
print(a[0:3])
print(a[3:])
print(a[0::3])
print(len(a))
print(a.count("'"))
print(a.capitalize())
print(a.find("ng"))
print(a.upper())
print(a.lower())"""



#escape sequence
"""a="string \n \t \' \\"
print("shasanka".upper(), end=" ")
print("acharya".upper())"""



#string format
"""a=str(input("enter a name\t"))
b=str(input("enter something\t"))
sum=b + a
print(f':{sum}')"""



#list indexing
"""l1=[1,2,3,4,5,'s,h,a,s,a,n,k,a',"hello"]
l2=l1.copy()#copy the element from one list to another
print(l1)
print(l1[:3])
l3=[3,6,8,4,0,1]
l3.sort()#sorting by ascending order
print(l3)
a=l3.pop(2)#pop the element from the index
print(a)
b=l3.remove(8)#remove the value
print(b)
l3.reverse()#reverse the order of element
print(l3)"""



#Q.N.1: program to store the list of marks and display it
"""a=[]
marks1=int(input("enter the marks"))
a.append(marks1)
marks2=int(input("enter the marks"))
a.append(marks2)
marks3=int(input("enter the marks "))
a.append(marks3)
a.sort()
print(a)

#Q.N.2 : program to store the list of fruits and display it on array
a=[]
f1=input("enter the fruitsname")
a.append(f1)
f2=input("enter the fruits name")
a.append(f2)
f3=input("enter the fruits name")
a.append(f3)
a.sort()
print(a)"""



#dictionaries
"""x={
    "name":"shasanka acharya",
    "age":[20, 16, 17],
    "roll":{
        "a":30,
        "b":31,
        "c":32
    }
}
print(x["age"])
print(x.keys())
print(x['roll']['a'])
print(x['roll'].keys())"""



#write a program to present a report card of a student incuding name,age,roll number and marks as well as percentage
"""a={
    "name":input("enter the name of student"),"age":int(input("enter the age of student")),
    "roll":int(input("enter the roll no. of student")),
    "marks":{
        "math":int(input("enter the marks of mathematics")),
        "science":int(input("enter the marks of science")),
        "English":int(input("enter the marks of english"))
    }
}
print("------Report Card------")
print("Enter the name of student:",a["name"])
print("Enter the age of student:",a["age"])
print("Enter the roll no. of student:",a["roll"])

print("Enter the marks of mathematics",a["marks"]["math"])
print("Enter the marks of science",a["marks"]["science"])
print("Enter the marks of English",a["marks"]["English"])
total=a["marks"]["math"]+a["marks"]["science"]+a["marks"]["English"]
percentage=total/3
print("total marks is:",total)
print(f"percentage :{percentage}%")  
if percentage>40:
    print("Result:Passed🟩")
elif percentage==40:
    print("Result:Passed🟩")
if percentage<40:
    print("Result: fail🔴") """

#swapping two numbers using only to variables
"""a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(f"a={a}")
print(f"b={b}")
a=a+b
b=a-b
a=a-b
print(
    f"after swapping a={a} and b={b}"
)
   """ 


