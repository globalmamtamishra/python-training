
def ana(str1,str2):
    so=sorted(str1)==sorted(str2)
    return so
str1=input("enter your string:")
str2=input("enter your string")
output=ana(str1,str2)
print(output)