def addition(a,b):
    return a+b

print(addition(3,5))

#here addition() is a user-defined function
#there are several built in functions len(), print(), map()
class Student:
    def ten_years(self, current_age):
        return current_age + 10
    
    student1 = Student()
    age_after_ten_years = student1.ten_years(10)
    print(age_after_ten_years)
# class Student:
#     def ten_years(self, current_age):
#         return current_age + 10

# student1 = Student()
# age_after_ten_years = student1.ten_years(10)

# print(age_after_ten_years)

    
    
    #here ten_years() is a method of a class student which an be called using student
    #object only
    