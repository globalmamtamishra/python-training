# def factorial(number):
#     if number==0:
#         return 1
#     else:
#         return number*factorial(number-1)
#
# input_number=int(input("enter your number :"))
#
# result=factorial(input_number)
# print(result)



# find the intersection of list


# li1=[1,2,3,4,5]
# li2=[6,7,8,9,1,2,5]
#
# for i in li1:
#     if i in li2:
#         print(i)


# union of list

# li1=[1,2,3,4,5]
# li2=[10,7,8,9,1,2,5,7,7]
#
# lit1=set(li1)
# lit2=set(li2)
#
# union=lit1|lit2
# print(list(union))


# list1=[1,2,3,4]
# print(sum(list1))

# sum=0
# for i in list1:
#     sum+=i
# print(sum)


#max element in list

# list1=[4,5,2,3]
# print(max(list1))


#2nd way
# list1=[1,2,3,4]
# target=5
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#
#         if list1[i]+list1[j]==target:
#             print(list1[i],list1[j])




#max element in list
# list1=[1,8,2,9,3,5]
# max1=list1[0]
# for i in list1:
#     if i>max1:
#         max1=i
#
# print(max1)

# find secand max

# list1=[1,9,4,8,5]
# newa=sorted(list1)[-2]
# print(newa)




#removeduplicate from list

# list1=[1,1,2,3,4,5,6]
#
# print(list(set(list1)))


# list1=[1,1,2,3,4,4,4,4]
# target=3
# mm=list1.count(target)
# print(mm)



# list1=[1,2,3,4,5,9]
# list1.reverse()
# print(list1)




# list1=[1,2,3,4,5,9]
#
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])


#checking list is empty or not

# list1=[1]
# if len(list1)==0:
#   print("empty")
# else:
#     print("not empty")

# list1=[1,2,3,4,6,7,8]
# list2=[]
#
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)



#create the squre of list and store in to other list

# list1=[1,2,3,4]
# list2=[]
# for i in list1:
#     list2.append(i**2)
# print(list2)


# list1=[1,2,3,4,-1]

# for i in list1:
#     if i>0:
#         print("positive")
#
#
#     else:
#         print("not positive")


#remove all occurence of specific element in list

# list=[1,2,3,4,5]
# target=5
# for i in list:
#     if i!=target:
#         continue
# print(i)



#find comman element between two list
# li1=[1,2,3,4,5]
# li2=[2,3,4,5]
# print(set(li1) & set(li2))



#calculate the product of list
# list=[1,2,3,4,5]
# prod=1
# for i in list:
#     prod*=i
# print(prod)

#remove first and last element from the list

# list1=[1,2,3,4,5,6]
#
# new_list=list1[1:-1]
# print(list1[1:-1])







# list1=[1,2,3,4,5]
# list2=[9,8,7,6]
# print(sorted(list1+list2))



#find longest sublist in list

# def longest_sublist(list_of_lists):
#     longest = []
#     for sublist in list_of_lists:
#         if len(sublist) > len(longest):
#             longest = sublist
#     return longest
#
# # Example usage
# list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11, 12]]
# longest = longest_sublist(list_of_lists)
# print("Longest sublist:", longest)




#count the number of odd and even number in list

# list1=[1,2,3,4,5,6,7]
# event_list=0
# Odd_list=0
# for i in list1:
#     if i%2==0:
#         event_list+=1
#     else:
#         Odd_list+=1
# print(f"even list:{event_list}\nodd number:{Odd_list}")




#find the index of last occurence of an element






















#rotate a list to the left by a given number of position








# my_list = [1, 2, 3, 4, 5]
# positions = 2
#
# print(my_list[positions %len(my_list):]+my_list[:positions%len(my_list)])




