from utils import user_manager
user = user_manager.UserManager()

def main():
    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
	
        choice = input("Action: ")

        if choice == '1':
            user.register()
            user.save_users()
            main()
        elif choice == '2':
            if not user.login():
                return False
        elif choice == '3':
            exit()
        else:
            print("Invalid Input")
            main()
            
if __name__ == "__main__":
    user.load_user()
    main()