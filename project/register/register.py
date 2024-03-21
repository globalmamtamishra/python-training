def register(self):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username not in self.__accounts:
        self.__accounts[username] = {'password': password, 'accounts': {}}
        print("Registration successful.")
    else:
        print("Username already exists. Please choose a different username.")
