#to access random value from random  library
"""import random as r
print(r.randint(0,2))

#or

from random import randint as r
print(r(0,2))

#or

import random
print(random.randint(0,2))"""



#program to play rock paper scissor
"""import random as r

def game():
    user = input("Enter what do u choose? (Rock, Paper, Scissor)")
    num = r.randint(0,2)
    if(num==0):
        print(f"You: {user}\nComputer: Rock")

    elif(num==1):
        print(f"You: {user}\nComputer: Paper")

    else:
        print(f"You: {user}\nComputer: Scissor")

    if (user=="Rock" and num==0):
        print("Draw!!")
    elif (user=="Rock" and num==1):
        print("Victoryyy!!")
    elif (user=="Rock" and num==2):
        print("Victoryy!!") 
    elif (user=="Paper" and num==0):
        print("Lostt!!")
    elif (user=="Paper" and num==1):
        print("Victoryyy!!")
    elif (user=="Paper" and num==2):
        print("Losttt!!")
    elif (user=="Scissor" and num==0):
        print("Losttt!!")
    elif (user=="Scissor" and num==1):
        print("You Winn!!")
    elif (user=="Scissor" and num==1):
        print("Losttt!!")
   
game() 
while 1:
    again=input("Do u wanna play again??(y/n)")
    if again=='y':
        game()
    else:
        exit()"""
        
"""# Try and except
try:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter another number: "))

    result = num1/num2
    print("Result: ", result)

except ValueError:
    print("Invalid input. Please enter numbers only!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(e)"""
#OR 
"""num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
result=num1/num2
print("Result: ",result)"""


#OR
"""num1=int(input("Enter first number: "))
num2=int(input("Enter another number: "))
result = num1/num2
    print("Result: ",result)
except ValueError:
    print("Invalid input.Please enter numbers only")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(e)
finally:
    print("end")"""
#OR
"""

try:
    num=int(input("enter a number"))
    if num<0:
        raise ValueError("Number connot be negative")
except ValueError as error:
        print(error)"""














