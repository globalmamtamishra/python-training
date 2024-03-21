def max_len(input_string):
   word1= input_string.split()
   max_v= max(word1,key=len)
   return max_v



input_string="mamta mishra helllllllllll"

max_len1=max_len(input_string)

print(max_len1)