# def view(string):
#
#     str = ""
#
#
#     even = True
#
#
#     for char in string:
#
#         if even:
#
#             str += char.upper()
#         else:
#
#             str += char.lower()
#
#
#         even = not even
#
#
#     return str
#
#
# string = "This is an example string."
# output = view(string)
# print(output)





# test_str = "geeksforgeeks"
#
# mp=str(test_str)
# res = ""
# for i in range(len(mp)):
#     if not i % 2:
#         res = res + mp[i].upper()
#     else:
#         res = res + mp[i].lower()
#
# print("The alternate case string is : " + str(res))

# ,open("output.txt", "w") as outputFile

with open("input.txt", "r") as inputfile:
  mp = inputfile.read()

res = ""
for i in range(len(mp)):
    if not i % 2:
        res += mp[i].upper()
    else:
        res += mp[i].lower()

# outputFile.write(str(res))

print(res)















# with open("input.txt", "r") as inputfile, open("output.txt", "w") as outputFile:
#     mp = inputfile.read()
#
# res = ""
# for i in range(len(mp)):
#     if not i % 2:
#         res += mp[i].upper()
#     else:
#         res += mp[i].lower()
#
# outputFile.write(res)












# def num1(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# with open("input.txt", "r") as inputfile, open("output.txt", "w") as outputFile:
#     for i in inputfile:
#         num = int(i)
#         if num1(num):
#             outputFile.write(f"{num} is even.\n")
#         else:
#             outputFile.write(f"{num} is odd.\n")







# with open("input.txt", "r") as inputfile, open("output.txt", "w") as outputFile:
#     mp = inputfile.read()
#
#     res = ""
#     for i, char in enumerate(mp):
#         if not i % 2:
#             res += char.upper()
#         else:
#             res += char.lower()
#
#     outputFile.write(res)









