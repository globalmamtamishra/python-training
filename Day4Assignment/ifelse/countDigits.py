
num =12

num_str = str(num)
count= 0
for i in num_str:

   if i.isdigit():
        count += 1

print(num, ":",count)
