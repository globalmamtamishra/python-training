# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# mylist=list(filter(lambda x:(x%2==0),li))
#
# print(mylist)


#Filter all people having age more than 18, using lambda and filter() function

# ages = [13, 90, 17, 59, 21, 60, 5]
#
# originallist=list(filter(lambda age:age>18,ages))
# print(originallist)


# Multiply all elements of a list by 2 using lambda and map() function

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# mylist=list(map(lambda x:x*2,li))
#
# print(mylist)



# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)


#Write a Python program to find the intersection of two given arrays using Lambda.


# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
#
# lis=list(filter(lambda x:x in array_nums1,array_nums2))
#
# print(lis)





# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
#
#
# print(thisdict["colors"])

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
#
#
# thisdict["colors"][0] = "green"
#
# thisdict["colors"][1] = "yellow"
# del thisdict["colors"][0]
#
# thisdict.update({"age": 22})
#
# thisdict.pop("electric")
#
# for x in thisdict.values():
#   print(x)

# print(thisdict)





child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

myfamily["child2"]["name"]="mmata"


print(myfamily["child2"]["name"])
print(myfamily)

