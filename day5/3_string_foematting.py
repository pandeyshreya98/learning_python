#we do string formatting using fstring


programming_language= "Python"
message= f"i am learning{programming_language}"
print(message)

programming_language= input("enter a language")
message= f"i am learning{programming_language}"
print(message)
#if not working cmd ma garne
###
#D:\python\day5>cd ..

#D:\python>cd day5 

#D:\python\day5>python 3_string_foematting.py
#i am learningPython
#enter a languagejava
#i am learningjava


name="shreya"
age=12
message=f"i am {name} and i am {age} years old"
print(message)


name="shreya"
age=12
print("i am %s and iam %d years old"%(name,age))


name="shreya"
age=12
print("i am {} and i am {}".format(name,age))

