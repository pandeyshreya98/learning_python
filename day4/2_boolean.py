#True and False are the boolean datatypes in python. keywords "true" and "false" are used to represent true state 
#and false state

#########operation that give boolean type ######
#1, comparison operator
a=5
b=3
print(a>b)   #true
print(a<=b)   #false


#logical operation
a=5
b=3
print(a>b and b!=a)   #true
print(not True)  #false
print(not a)  #false


#membership operation
print("a" in ["a","e","i"])   #true
print("a" not in ["a","e","i"])  #false


#identity operation
a=1
b=1
print(a is b)  #true       #id ra value same bhayeni false huna sakxa as limit hunxa no ko pani
print(a is not b)   #false


#concept of truthy and falsy
a=5
print(not a)  #false

#any non zero or non-empty datatype including true itself is a truthy data type
#5,1,-23,[1,2],(1,2,3),{-4,-5,"a"},{a:1}, true;all these data are truthy data types

#in contrast, all empty data-types ,zero ,none including false are falsy data types
#0,[],(),{}<dictionary,set(),'',none,false; all are falsey datatypes

#how can we verify data is truthy or falsy
#we can use bool() built in 

#check for truthy
a=4
b=-4
c=[1,2,3]
d=(1,2)

print(bool(a))  #true
print(bool(b))  
print(bool(a))  #true
print(bool(a))  #true
print(bool(a))  #true
print(bool(a))  #true

#applying not operation to any truthy value 

#chaeck for falsey


#applying not operation to any falsy value result in true

print(not a)  #true
print(not none) #true



