
# li=[1,2,3,4,5]
# l1= map(lambda x:x+2,li)
# print(l1)





# class Person:
#   def person(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)




# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()


# li=[1,2,3,4,5]
# l1= list(map(lambda x:x+2,li))
# print(l1)



# def evenOdd(num):
#     if num%2==0:
#         return "{} even ".format(num)
#     else:
#         return " {} odd".format(num)
# l=[1,2,3,4,5,6,7,8,9,10]
# p=list(map(evenOdd,l))
# print(p,end=' ')


#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

# r=lambda a:a+15
# print(r(10))

# r=lambda  x,y:x*y
# print(r(10,10))



# question2:
# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# def unknownNumber(n):
#
#     return lambda x:x*n
#
# m=unknownNumber(3)
# print(m(15))














#filter
# my1=[18,19,4,67,99,46]
#
# temp=list(filter(lambda  x:x%2==0,my1))
# print(temp)



# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# subject_marks.sort(key=lambda x:x[1])
# print(subject_marks)



# Create a list of dictionaries named 'models', each dictionary representing a mobile phone model with 'make', 'model', and 'color' keys
# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]
#
#
# #print("Original list of dictionaries:")
# print(models)
#
#
# sorted_models = sorted(models, key=lambda x: x['color'])
# print(sorted_models)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = list(map(lambda x: "{x} even " if x % 2 == 0 else "{x} odd ", numbers))
# print(even_odd)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = list(map(lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd", numbers))
# print(even_odd)

#string method
# a=10
# b=20
# name=("ramu")
#
# print(name,"has",a,"apple &",b,"banana")
#
# print("{2} has {0} apples & {1} bananes".format(name,a,b))
#
# print("%s has %d apple & %d banana " %(name,a,b))


# name = 'Tushar'
# age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")


# print(f"{name} has {a} apples & {b} bananas")




