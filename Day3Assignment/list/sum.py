
  #find sum of list type1
# lit=[1,2,3,4,5,6,7]
#
# sum=0
# for i in lit:
#     sum=sum+i
# print(sum)

#2d type

# lit=[1,2,3,4,5,6,7]
#
# print(sum(lit))


# 3rd type

# lit=[1,2,3,4,5,6,7]
#
# sum=0
# i=0
# while i<=len(lit):
#     sum=sum+i
#
#     i=i+1
# print(sum)


# 4th type


def sum_of_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])




lit=[1,2,3,4,5,6,7]
s=sum_of_list(lit)
print(s)

