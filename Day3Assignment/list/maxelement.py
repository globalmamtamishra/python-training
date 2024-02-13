
#find max element type1

# list=[1,3,5,4,2,]
#
# max=0;
#
# for i in list:
#     if i>max:
#         max=i
# print(max)



#find max element type2

# list=[1,3,5,4,2,]
#
# max=list[0]
#
# for i in list:
#     if i>max:
#         max=i
# print(max)

#find max element type3


# list=[1,3,5,4,2,]
#
#
# max= float('-inf')
#
# for i in list:
#     if i>max:
#         max=i
# print(max)

#find max element type4

# list=[1,3,5,4,2,]
#
# ls=max(list)
#
# print(ls)

#find max element type5
# list=[1,3,5,4,2,]
#
# ls=sorted(list)[-1]
#
# print(ls)

#find max element type6

def revers(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], revers(lst[1:]))

list=[1,3,5,4,2,]
maximum = revers(list)
print( maximum)
