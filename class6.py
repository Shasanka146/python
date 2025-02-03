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

commands={}

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
print(command)


    


