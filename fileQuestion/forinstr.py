

str="geekforgeek"
res=" "

for i, char in enumerate(str):
    if i%2==0:
        res+=char.upper()
    else:
        res+=char.lower()

   # print(i, char)

print(res)