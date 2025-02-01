#program using try and except 
"""list=[]
roll=int(input("Enter the range of roll no."))
for i in range(roll):
    a=int(input(f"enter the{i+1}th term"))
    try:
        if a in list:
            raise ValueError("roll no. already exist in list")
    except ValueError as error:
        print("error")
    else:
        list.append(a)
        print(f"{a} has successfully added")"""


#program 
"""def triangle(a,b,c):
    try:
        if ((a+b)<c) or ((a+c)<b) or ((c+b)<a):
            raise ValueError("it is not triangle")
    except:
        raise
    return 
try:
    x=int(input("Enter 1st side of triangle"))
    y=int(input("Enter 2nd side of triangle"))
    z=int(input("Enter third side of triangle"))
    triangle(x,y,z)
except ValueError as e:
    print(e)"""
    

"""def triangle(a,b,c):
    try:
        if ((a+b)>c) and ((a+c)>b) and ((c+b)>a):
            print("it is  triangle")
    except:
        raise ValueError("error expected")
    return 
try:
    x=int(input("Enter 1st side of triangle"))
    y=int(input("Enter 2nd side of triangle"))
    z=int(input("Enter third side of triangle"))
    triangle(x,y,z)
except ValueError as e:
    print(e)"""
    #recursive function
"""def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
result=factorial(5)
print("factorial:",result)
   """ 
#sum of natural number
"""def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
result=sum(10)
print("sum:",result)"""

#fibonacci 
"""def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
    print(fibonacci(i))"""


#function overloading

"""def sum(num1,num2=0,num3=0):
    print(num1+num2+num3)
num1=5
num2=7
num3=10
sum(num1)
sum(num1,num2)
sum(num1,num2,num3)"""


  
# number=[1,2,3,4,5]
# squares=list(filter(lambda x:x%2==0, number))
# print(f"Squares: {squares}")
"""list ma vako element ko sum """
number=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y, number)
print(f"Sum is {sum}")
 #lambda function 
number=[1,2,3,4,5,6,7,8,9]
even_number=list(filter(lambda x:x%2==0,number))
print(f"even number:{even_number}")
