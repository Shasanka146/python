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


