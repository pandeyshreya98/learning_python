#concatination = we can concatinate string using "+" operator

n1="hello"
n2="world"
print(n1+n2)  #helloworld



#repition/ broadcast operation  = broadcast in string is done using * operator
message="hello"
print(message*3)  #hellohellohello


#membership operation
print("m" in "message")  #true
print("m" not in "message")   #false

#built in function



#1. len() => it gives the length of sequential data types. eg list string tuple etc
message="hello world"
print(len(message))  #11


##2 type() => return the type of function
print(type(message))  #<class"str">

#slice() => this funtion is similar to string and list slicing

sliced_data = slice(2,7)
print(message[sliced_data])   #llo W