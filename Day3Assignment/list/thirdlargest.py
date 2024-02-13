
#find third largest element in list

list=[6,7,9,10,44,87,99]

s=sorted(list)[-3]
print(s)

#find third largest element in list

def third_largest(lst):
    if len(lst) < 3:
        return "List has less than three elements"

    sorted_list = sorted(lst, reverse=True)
    return sorted_list[2]


my_list = [1, 9, 3, 7, 5, 8]
third_lar= third_largest(my_list)
print(third_lar)
