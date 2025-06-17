#loop
"""l1=[1,2,3]
for i in l1:
    print(i)"""

#range using in for loop
"""for i in range(10):
    print(i)"""

# range using for loop with step 2 and exclude 7
"""for i in range(0,7,2):
    print(i)"""


"""l1=[1,5,9]
for i in l1:
    print(i)
else:
    print("done")"""


#using break
"""for i in range(100):
    print(i)
    if i==3:
        break"""


"""for i in range(10):
    if i==3:
        continue
    print(i)"""

"""#program to display even number using for loop with continue
for i in range(11):
    if i%2!=0:
        continue
    print(i)"""

# using pass in for loop when condition is not fixed and overcome error
"""for i in range(20):
    pass

for i in range(20):
    ..."""


"""a=enumerate(["Alice","bob","charlie"])
print(f"{i}:{name}")"""


#write a program to print :
"""row=5
for i in range(row):
    for j in range(i):
        print("*\t",end="")
    print()



row=5
for i in range(row):
    for j in range(row-i):
        print("*\t",end="")
    print()



row=5
for i in range(row):
    for j in range(row):
        print("*",end="")
    print()"""


#program to find sum of natural number and factorial
"""num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
        sum+=i
print(f"the sum of natural number up to {num} is {sum}")


fact=1
for i in range(1,num+1):
        fact*=i
print(f"the factorial of {num} is {fact}")"""


#fibonacci series
"""num=int(input("enter a number:"))
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b"""

#sum of digit
"""num=int(input("Enter a number"))
b=0
for i in range(num):
    a=int(num%10)
    b+=a
    num=int(num/10)
    
print(b)"""


"""num=int(input("Enter a number"))
b=0
for i in range(num):
    a=int(num%10)
    b+=a
    num=int(num/10)
print(b)

while num>0:
    rem=int(num%10)
    sum+=rem
    num=num/10
    temp=num
print(sum)

sum=sum*10+rem

if temp==sum:
    print("palindrome")
else:
    print("not palindrome")"""


#using function 
"""def greet(name):
    print("hello,",name)
greet("shasanka")
greet("shasanka")"""

#add two number using function
"""def add(x,y):
    return x+y
result=add(5,3)
print("sum:",result)"""

#doc string in function
# def func():
#     """
#     this  is doc string
#     """

# print(func.__doc__)

#
"""def greet(name,greeting="Hello"):
    print(greeting+",",name)
greet("Shasanka")
greet("Shasanka","hi")


def simple_interest(principle,time,rate=10):
    return (principle*time*rate)/100
print(f"simple interest with default parameter{simple_interest(5000,5)}")
print(f"simple interest without default parameter{simple_interest(5000,5,7)}")"""


# count and sum of args and unpack number
"""def add(x,y,*args):
    sum=0
    print(args)
    for num in args:
        sum+=num
    return sum
  
result = add(1,2,3,4,5)
print("sum:",result)
x,y,*unpack=[1,2,3,4,5,6]
print(unpack)"""


#program by using function args 
"""a=[]
num=int(input("Enter the range of number:"))
for i in range(num):
    c=int(input(f"enter the {i+1}th term"))
    a.append(c)
def add(*args):
    sum=0
    for b in args:
        sum+=b
    return sum
result=add(*a)
print("sum:",result)"""
#Mini project to perform on student management system
student=[]

















