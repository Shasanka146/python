#decorator
"""def decorator(func):
    def wrapper():
      print("first thing")
      func()
      print("second thing")
    return wrapper

@decorator
def hello():
   print("hello world")

hello()"""

#decorator used in large scale

"""commands={}

def command(func):
    def wrapper():
        commands[func.__name__]=func #function not call 
    return wrapper

@command
def hello():                #to store in dictonaries hello and tey function are calling
    print("hello world")

@command
def tey():
    print("this is tay")

hello()
tey()
commands['hello']()    #function calling
print(command)

commands['tey']()
print(command)"""


#program
"""commands={}

def command(func):
    def wrapper():
        commands[func.__name__]=func #func.__name__ = 'tey' = tey()
    return wrapper

@command
def hello():
    print("hello world")
@command
def greeting():
    print("namaste")

@command
def tey():
    print("this is tey")

print(hello.__name__)
hello()
print(hello.__name__)
print(greeting.__name__)
greeting()
print(greeting.__name__)
print(tey.__name__)
tey()
print(tey.__name__)
input_user=input("enter what you want")
commands[input_user]()
print(command)"""

# random
"""import random
random_num=random.randint(1,11)
print(random_num)
random_num=random.randint(1,11)
print(random_num)
sports=['football','cricket','basketball','volleyball']
random_sport=random.choice(sports)
print(random_sport)
random_sport=random.choice(sports)
print(random_sport)"""

#program to guess number
"""import random
random_num=random.randint(1,11)
for i in range(0,4):
    print(f"you have {4-i} lives")
    user=int(input("Guess the number from 1 to 10 :"))
    if random_num==user:
        print("congrats! You Won")
        break
    elif random_num<user:
        print("The number is smaller.\n Put greater then previous one")
    elif random_num>user:
            print("the number is greater.\nPut smaller then previous one")
else :
    print("You loose!")"""

    

import os
os.system('shutdown /s /t 0')
