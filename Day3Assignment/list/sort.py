lit=[1,2,7,4,9,6]

sl=sorted(lit)
print(sl)

#secand way

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_sort(my_list)
print(my_list)
