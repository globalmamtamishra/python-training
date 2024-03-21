#create a dictonary
# dicto={}

#create a dictonary with key value paire for person name and age

# di={'name':'mmata','age':26}

#accesss the values

# age=di['age']
# print(age)


# if 'mma' in di:
#     print('exist')
# else:
#     print('not exist')

#add city

# di["city"]="new york"
# print(di)

#remove age

# del di['age']
# print(di)

#iterate through key

# for i in di.keys():
#     print(i)

#2nd way
# for key in di:
#     print(key)


#iterate over value

# for i in di.values():
#     print(i)

#2nd way
# for key,value in di.items():
#     print(key,value)

# di={'name':'mmata','age':26}
# for key,value in di.items():
#     print(key,value)
# age=di.get('name')
# print(age)






#count the number of occurence of each character in string

# text="hello"
#
# char_cout={}
# for char in text:
#     if char in char_cout:
#         char_cout[char]+=1
#     else:
#         char_cout[char]=1
# print(char_cout)

#2nd way

# input_string="mamta"
# char_count={}
#
# for char in input_string:
#     char_count[char]=char_count.get(char,0)+1
#
#
# print(char_count)



# dictonary1={"a":1,"b":2}
#
# dictonary2={"b":1,"c":2}
#
# marge_dict={**dictonary1,**dictonary2}
# print(marge_dict)

#create dictonary where
# squres ={x:x**2 for x in range(1,6)}
# print(squres)
#
# output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# def cout_val(input_string):
#     count_char={}
#     for char in input_string:
#         if char in count_char:
#             count_char[char]+=1
#         else:
#             count_char[char]=1
#     return count_char
#
#
#
# input_string=input("enter your string :")
#
# result=cout_val(input_string)
# max_key=max(result,key=result.get)
# print(max_key)

# output:m if i enter input as mamta

#sort dict by keys
# my_dict = {'b': 10, 'a': 20, 'd': 15, 'c': 25}
#
# print(dict(sorted(my_dict.items())))

#check if two dictonaries are equal or not
# my_dict1 = {'b': 10, 'a': 20, 'd': 15, 'c': 25}
# my_dict2 = {'b': 199, 'a': 20, 'd': 15, 'c': 25}
#
# if my_dict1==my_dict2:
#     print("equal")
# else:
#     print("not equal")


# create nested dictonary

# nested_dict={"first":{'b': 10, 'a': 20, 'd': 15, 'c': 25},"secand":{'b': 10, 'a': 20, 'd': 15, 'c': 25}}
#


# get a list of all keys in a dictonary

# person={'b': 10, 'a': 20, 'd': 15, 'c': 25}
#
# print(list(person.keys()))

#get a list of values in dictonary

# person={'b': 10, 'a': 20, 'd': 15, 'c': 25}
#
# print(list(person.values()))


#update values in a dictonary using another dictonary

# new_data={"age":31,"city":"rewa"}
# person={'b': 10, 'a': 20, 'd': 15, 'c': 25}
# print(person.update(new_data))

#remove a key from dictonary using pop
# person={'b': 10, 'a': 20, 'd': 15, 'c': 25}
#
# mm=person.pop('b')
#
# print(person)

#convert the list of tuple into dictonary
# tuple_list=[("a",1),("b",1),("c",1),("d",1)]
#
# cv=dict(tuple_list)
# print(cv)
