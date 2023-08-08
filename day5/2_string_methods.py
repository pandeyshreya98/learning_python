
# 1. capitalize()
message="helloworld"
print(message.capitalize())  #Hello world
#or

message="helloworld"
result=(message.capitalize())  #Hello world
print(result)

#2. tittle()
result=message.title()
print(result)  #Hello World

#3. upper
result=message.upper()
print(result)  #HELLO WORLD

#4. lower()
result=message.lower()
print(result)  #hello world

#5. split()
message="hello world i am shriya"
result = message.split()  #calling split() without any parameters. it splits with <space> by default
print(result)   # ["hello", "world", "i","am", "shriya"]

message="hello world i am shriya"  #['hell', ' w', 'rld i am shriya']
result= message.split("o")
print(result)  #

message= "hello,all,i,am,learning,python"  #['hello', 'all', 'i', 'am', 'learning', 'python']
result= message.split(",")
print(result) 


#join()
info=['hello', 'all', 'i', 'am', 'learning', 'python']  #hello all i am learning python
result= " ".join(info)
print(result) 

#info.join(" ")  #it raises error bcoz join() should be called with string object not with list

info=['hello', 'all', 'i', 'am', 'learning', 'python']  #hello+all+i+am+learning+python
result= "+".join(info)
print(result) 

info=['hello', 'all', 'i', 'am', 'learning', 'python']  #hello,all,i,am,learning,python
result= ",".join(info)
print(result) 

#find()
message = "hello world"
result=message.find('w')
print(result)  #6


message = "hello world"
result=message.find("rld")
print(result) #8


message = "hello world"
result=message.find("Rld")
print(result) #-1  #if string us not found then the find returns -1



message = "hello world"
search_value= "Rld"
result=message.lower().find(search_value.lower())
print(result) 


#replace()
message="hello world"
result= message.replace("hello","Hello")
print(result)   #Hello world

