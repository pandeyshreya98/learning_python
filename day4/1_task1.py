#create a lsit of first 10 multiples of 3 using list comprehension
#range(7)
#print(list(range(7)))
a=[]
for value in range(1,11):
    a.append(value*3)
    print(a)
    
    
    #using comprehension
    a=[i*3 for i in range(1,11)]
    print(a)
    