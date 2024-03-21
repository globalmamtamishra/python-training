def login(self):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in self.__accounts and self.__accounts[username]['password'] == password:
        print("Login successful.")
        self.__logged_in_user = username
    else:
        print("Invalid username or password.")