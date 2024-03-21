
#first Way to Do
# list=[12,35,9,56,24]
# temp=list[0]
# list[0]=list[-1]
# list[-1]=temp
# print(list)





#secand Way

# list=[12,35,9,56,24]
#
#
# first=list.pop(0)
# last=list.pop(-1)
#
#
# list.insert(0,last)
# list.append(first)
# print(list)



# List = [23, 65, 19, 90], pos1 = 1, pos2 = 3

list = [23, 65, 19, 90]

temp=list[2]
list[2]=list[0]
list[0]=temp
print(list)





