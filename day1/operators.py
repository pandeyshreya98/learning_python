#### operators ####
#operators are the symbols in python or in any programming language that carry out arithmetic and logical operation
#the python operators are 
#1. arithmetic operator
#2. relational or comparison operators
#3. logical
#4. membership
#5. identity
#6. assignment

###arithmetic operators

#1. addition (+)
a=1
b=2
print(a+b)


#2. subtractiona1
a=2
b=1
print(a-b)

#multiplication
print(a*b)

#modulus : modulus operators gives remainder of the division operation 
a=4
b=2
print(a%b)#  result 0
print (5%2) # result 1


#exponential(**)
print(a**2) #4**2 = 16

#floor division(//)
#this operator omits the decimal values from the division operation and gives floor value
print(3//2) #ans 1
print(-3//2) #ans -2


####comparison operator ####
# =,<,>,>=,<=,!= are relational operators
# relational operators give boolean results{true or false)

a=5
b=3
print(a=b) #false
print(a>b) #true
print(a<b) #false
print(a!=b) #false


######logical operators#####
# and or not are logical operators

print(a>b or b!=a)
print(a>b and b!=a)
print(not true) #false
print(not false) #true

a=5
print(not a) #false

a=0
print(not a) #true. concept of truthy and falsey


#####assignment operator#####
# is equals to (=) is the simplest assignment operator
a=2+3


a=1
a=a+1
print (a) #2
a+= 1 #3
# here +=,-=,*=,/=,%=,//= is also an assignment operator

a=20
a%=2
print(a) #gives 0

######membership operator #########
# in and not in are the membership operators we can use membership operator in sequesntial datatype
print(2 in [1,2,3] ) #true
print(3 not in (1,2,3))#false


#####identity opertor#####
#" is" and is not are identity operators
a= [1,2,3]
b=a
print(a is b) # true
#here a nad b are the same object and liess at the same memory location
print(id(a) == id(b) ) # true

b= a.copy()
print(a is b) # false
print(id(a)== id(b) ) # false
#here a and b have same value but are in diff memorylocati0n

#######precedence and associativity#####
#if an operation has multiple operators then precedence defines the order of such operators
#if multiple operators have same precedence then the operation is done based on associativity 
#normally all the operators have left-right associativity ecept **

print(2*3/3) # ans 2 . here * and / have same precedence but the associativity is from left to rignt
#so multiplication is done first and then division

print(2**3**2) #522
# for ** associativity is right to left

