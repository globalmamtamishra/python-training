# def count_characters(input_string):
#     char_cout={}
#     for char in input_string:
#         if char in char_cout:
#             char_cout[char]+=1
#         else:
#             char_cout[char]=1
#     return char_cout
#
# input_string=input("enter the char's:")
# result=count_characters(input_string)
#
# for char, count in result.items():
#
#
#   print(f"'{char}':{count}")


#secand way to do this question

# def count_characters(input_string):
#     word=input_string.split()
#
#
#     char_cout={}
#     for char in word:
#       char_cout[char]=char_cout.get(char,0)+1
#
#     return char_cout
# #
# input_string=input("enter the char's:")
# result=count_characters(input_string)
# print(result)

# for char, count in result.items():
#     # print(char,":",count)
#
#   print(f"'{char}':{count}")




# import os
# cwd = os.getcwd()
# print("Current working directory:", cwd)






def most_frequent_character(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count

input_string = input("Enter the characters: ")
most_frequent, frequency = most_frequent_character(input_string)
print(f"The most frequent character is '{most_frequent}' with frequency {frequency}.")




