a=[1,2,3]
b=a
print(a)  #[1,2,3]
print(b)  #[1,2,3]              ######memory location same
print(a is b)  #true

b=a.copy()
print(a)  #[1,2,3]
print(b)  #[1,2,3]           ############memory location different
print(a is b)  #false


#shallow copy
a=[[1,2,3],4,5]
b=a.copy()
a[0][1] =7
print(a)   #[[1,7,3],4,5]
print(b)    #[[1,7,3],4,5]


#even if b is copy of a , if wechange any mutable object inside 'a' then
#the change is also reflected in 'b' . this type of copy is caleed shallow copy


####deep copy
from copy import deepcopy
a=[[1,2,3],4,5]
b=deepcopy()
print(a)   #[[1,2,3],4,5]
print(b)    #[[1,2,3],4,5]

a[0][1] =7
print(a)   #[[1,7,3],4,5]
print(b)    #[[1,2,3],4,5]




