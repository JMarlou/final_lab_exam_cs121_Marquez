import os
from .user import User
from .dice_game import DiceGame
dice = DiceGame()

class UserManager:
    user_accounts = {}

    def load_user(self):
        if not os.path.exists("users.txt"):
            with open('users.txt', 'w') as f:
                f.write("")
       
        else:
            with open("users.txt", 'r') as f:
                for line in f:
                    user = line.strip().split(',')
                    self.user_accounts[user[0]] = User(user[0], user[1])

        
    def save_users(self):
        with open('users.txt', 'w') as f:
            for username, password in self.user_accounts.items():
                f.write(f'{username},{password.password}\n')

    def validate_username(self, username, password):
        if username in self.user_accounts:
            if self.user_accounts[username].password == password:
                print("Login Successfully\n")
                return True
            else:
                print("Wrong Password!")
                return False
        else:
            print("Invalid Username")
            return False

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
            dice.menu(username)
            return
        else:
            return False


    