"""file=open("example.txt","w")
file.write("hello world")
file.close()

file=open("example.txt","r")
content=file.read()
print(content)
file.close()"""

#file handling using single dictonary
import json
dict={
    "name":"",
    "age":10

}
with open("text.json","w")as f:
    json.dump(dict,f)
with open("text.json","r")as f:
    loaded =json.load(f)
print(loaded)


#file handling using multiple dictonary
