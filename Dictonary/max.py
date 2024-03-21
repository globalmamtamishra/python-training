

# def char_counter1(input_string):
#     char_count={}
#     for char in input_string:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#
#     max_count=max(char_count.values())
#
#     max_chars = [char for char, count in char_count.items() if count == max_count]
#     max_chars1=' '.join(max_chars)
#     return max_chars1,max_count
# input_string=input("enter your string :")
#
# result_chars1, result_count=char_counter1(input_string)
# print(f"{result_chars1}:{result_count}")




#secand way

# def char_counter1(input_string):
#     char_count={}
#     for char in input_string:
#         char_count[char]=char_count.get(char,0)+1
#     return max(char_count,key=char_count.get)
#
#
# input_string=input("enter your string :")
#
# result_chars1, result_count=char_counter1(input_string)
# print(f"{result_chars1}:{result_count}")




# def char_counter1(input_string):
#     char_count = {}
#     for char in input_string:
#         char_count[char] = char_count.get(char, 0) + 1
#     max_char = max(char_count, key=char_count.get)
#     return max_char, char_count[max_char]
#
# input_string = input("Enter your string: ")
#
# result_char, result_count = char_counter1(input_string)
# print(f"Maximum occurring character: {result_char}, Count: {result_count}")





def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array:", my_list)






