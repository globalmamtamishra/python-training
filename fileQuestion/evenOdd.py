def num1(num):
    if num % 2 == 0:
        return True
    else:
        return False

with open("input.txt", "r") as inputfile, open("output.txt", "w") as outputFile:
    for i in inputfile:
        num = int(i)
        if num1(num):
            outputFile.write(f"{num} is even.\n")
        else:
            outputFile.write(f"{num} is odd.\n")
