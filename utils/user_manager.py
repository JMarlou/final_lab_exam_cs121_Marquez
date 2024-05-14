from user import *

class UserManager:

    user_accounts = {}

    def load_user():
        pass

    def save_users():
        pass

    def validate_username():
        pass

    def register(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in self.user_accounts:
            print("Username already exists")
            input()
            return
        else:
            self.user_accounts[username]
            print("Successfully Registered!")
        self.user_accounts[username] = User(username, password)
        

    def login():
        pass

    