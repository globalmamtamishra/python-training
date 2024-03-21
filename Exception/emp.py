

class InvalidEmployee(Exception):

    def __str__(self):
        return "not employee of genzeon"



Empid=input("enter employee id: ")




try:
    if Empid[:1]!='GEN':
        print("error")
except InvalidEmployee as e1:
    print("invalid")
print("detailed check")