
#2nd way

# tuple = (1, 2, 3, 4, 1, 2, 1, 3, 4, 5)
# p=0
#
# if p in tuple:
#     print("exist")
# else:
#     print("not exist")




tuple = (1, 2, 3, 4, 5)
element= 0

exists = False
for i in tuple:
    if i == element:
        exists = True
        break

if exists:
    print("exist")
else:
    print("not exist")


# 3rd way

tuple = (1, 2, 3, 4, 5)
element= 3

try:
    my_tuple.index(element)
    print("exists")
except ValueError:
    print("not exist")
