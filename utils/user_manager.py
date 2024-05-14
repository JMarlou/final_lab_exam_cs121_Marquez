from user import *

class UserManager:

    user_accounts = {}

    def load_user(self):
        try:
            with open('users.txt', 'r') as f:
                self.user_accounts = eval(f.read())
        except FileNotFoundError:
            self.user_accounts = {}

    def save_users(self):
        with open('users.txt', 'w') as f:
            print(self.user_accounts, file=f)

    def validate_username(self, username, password):
        if username in self.user_accounts:
            if self.user_accounts[username].password == password:
                print("Login Successfully")
            else:
                print("Wrong Password!")
                return
        else:
            print("Invalid Username")
            return

    def register(self):
        username = input("Enter Username(at least 4 characters): ")
        if len(username) < 4:
            print("Username too short!")
            input()
        else:
            password = input("Enter Password(at least 8 characters): ")
            if len(password) < 8:
                print("Password too short")
                input()
            else:
                if username in self.user_accounts:
                    print("Username already exists")
                    input()
                    return
                else:
                    print("Registration Successful!\n")
                    self.user_accounts[username] = User(username, password)
        

    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        if self.validate_username(username, password):
            print("Login Successfully")
            return True
        else:
            return False

    