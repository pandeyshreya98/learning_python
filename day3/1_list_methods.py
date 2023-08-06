# append()
vowels = ["a","e","i","o"]
vowels.append("u")
print(vowels)

#extend()
a=[1,2,3]
b=[4,5,6]
result=a.extend(b)
#print(result)  #none
print(a)   #[ 1,2,3,4,5,6]


#insert(index,value)
vowels =  ["a","e","o","u"]
vowels.insert(2,"i")
print(vowels)   # ["a","e","i,"o","u"]


#remove(value)
a=[1,2,3,4]
a.remove(3)
print(a)
a.remove(6)   #error


#pop(index)
vowels = ["a","e","i","o","u"]
result = vowels.pop(1)
print(result)  #e
print(vowels)  #aiou

#pop() method doesnt neessari 


#clear
a=[1,2,3,4]
a.clear()
print(a)  #[]

#index(value,start,end)[]
vowels= ["a","e","i","o","u"]
result=vowels.index("i")
print(result)


a=[1,2,3,4,1,4,5,2,3,2]

#count()
a=[1,2,3,1,2,4,]



#reverse()
a=[2,1,10,9,3]
a.reverse()
print(a)  #[3,9,10,1,2]

