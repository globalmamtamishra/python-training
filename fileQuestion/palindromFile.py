def palindrome(str):

  return str == str[::-1]

with open("input.txt", "r") as inputfile, open("output.txt", "w") as outputFile:
    for i in inputfile:
        str = i.strip()
        if palindrome(str):
            outputFile.write(f"{str} is a palindrome")
        else:
            outputFile.write(f"{str} is not a palindrome")
