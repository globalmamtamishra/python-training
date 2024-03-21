#ndex Out of Bound
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("ZeroDivisionError:")
except IndexError:
    print("index out of range")
