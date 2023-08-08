#string indexing amd slicing is similar to that of list
#forward indexing starts from 0 and reversing indexing starts from -1

message= "hello world"
print(message[0])
print(message[3])
print(message[5])
print(message[-1])
print(message[-7])
print(message[20])
print(message[-14])
print(message[0])




message="hello world"
message[2]="L"   # it raises errror bcoz we cant change the existing iten in string as it is immutable 
#del message[2]
#del message #it deletes the string


#iterating through string
message="hello world"
for each in message:
    print(each)  # >>> message="hello world"
    for each in message:
     print(each)