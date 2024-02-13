
# string=input("enter your string here :")
#
# py=string.split()
#
# reverse_string=' '.join(py[::-1])
# print(reverse_string)


#another way2

# def reverse_string(input_string):
#     reversed_string = ''
#     for char in input_string:
#         reversed_string = char + reversed_string
#     return reversed_string
#
#
# input_string = input("Enter a string: ")
# reversed_string = reverse_string(input_string)
# print("Reversed string:", reversed_string)



# third way to reverse the string
def reverse_string(input_string):
    return ''.join(reversed(input_string))


input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
