#sort(reverse=True,key=function) method
a=[5,3,10,2,1,12,6]
a.sort()
print(a)

a.sort(reverse=True)
print(a)   #[12,10,6,5,3,2,1]


a=[(5,4),(3,2),(4,10),(12,1),(1,9)]
b=[(2,1),(4,5),(2,3),(0,1)]
def get_second_num(data):
    return data[1]

a.sort(key=get_second_num)
print(a)
b.sort(key=get_second_num)
print(b)

a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def get_last_num(data):
    return data[-1]

a.sort(key=get_last_num)
print(a)              #[(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]

a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def get_last_num(data):
    return data[-1]

a.sort(key=get_last_num)  #reverse=true
print(a)

