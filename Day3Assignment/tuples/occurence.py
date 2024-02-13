
tup=(1,2,3,4,3,2,1,2,3,4)

tp=tup.count(1)

print(tp)


#2nd type

tuple = (1, 2, 3, 4, 1, 2, 1, 3, 4, 5)
el_count = 1

count = 0
for element in tuple:
    if element == el_count:
        count += 1

print(count)
