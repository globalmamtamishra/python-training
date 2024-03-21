# def isPalindrome(s):
#     return s == s[::-1]
# f1 = open("Palindrome.txt"):
# file_string = f1.read()
#  if isPalindrome(file_string):
#         print("Palindrome")
#     else:
#         print("Not Palindrome")



def view(siva):
    return siva == siva[::-1]

with open("Palindrome.txt") as f1:
    siva = f1.read()
    if view(siva):
        print("Palindrome")
    else:
        print("Not Palindrome")
