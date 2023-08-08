#pythonlist are mutable datatypes and are sequential (also an iterable).
# list are created enclosing data in big bracket [] or using builtin function list()

# creating an empty list
a=[]
b=list()

# creaing a non empty list
a=[1,2,3]
print(a)
vowels=["a","e","i","o","u"]
# the above are the examples of list with homogeneos datatypes


# list can also contain heterogeneos datatype

a=[1,2.3,["a","e"],("i",3),{1,2,3},{"a":1,"b":2}]

########accessing list items #######
# list items can be accesed using indexing and slicing
# indexing in list starts from 0 for forward traverse and -1 for reverse traverse
vowels=["a","e","i","o","u"]
print(vowels[0])  #a

print(vowels(-3)) #i

#print(vowels[10]) #indexerror: list index out of range
#print(vowels[-3]) #indexerror: list index out of range


#item assignment is possible in list as it is mutable
vowels=["a","e","i","o","u"]
vowels[1]="E"
print(vowels)


###list slicing####
a=["a","b","c","d","e","f","g","h","i","j"]
print(a[0:5])  # ["a","b","c","d","e"]
print(a[:5]) #same
print(a[2:])  #"c","d","e","f","g","h","i","j"
print(a[2:7]) #"c","d","e","f","g"

#print(a[7:2])  #[]
print(a[0: -2])  #"c","d","e","f","g"
print(a[: -2])  #"c","d","e","f","g"

print (a[-5:])  #"f","g","h","i","j"
print (a[-7:-2])  #"d","e","f","g","h"
#print (a[-2:-7])  #[]


##list operation 
#concatination 
a=[1,2,3]
b=[4,5,6]
result=a+b
print(result)  #[1,2,3,4,5,6]


##membership opration
print(2 in [1,2,3]) #true
