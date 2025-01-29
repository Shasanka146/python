print('My First Python Class')
#Arthimetic operation
"""a="Shasanka Acharya"
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


print(float(a))
a=input("enter a number")
b=input("enter a number")
print(a+b)


a=int(input("enter a number"))
b=int(input("enter a number"))
print(a+b)"""



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
x={
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
print(x['roll'].keys())


