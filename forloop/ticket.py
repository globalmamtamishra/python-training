age=int(input("enter your age :"))

if age>3 and age<=100:
    if age<17:
        print("half ticket")
    elif age==17 and age<=60:
        print("full ticket")
    elif age>60:
        print("discount")

else:
    print("invalid age")