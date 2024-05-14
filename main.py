from utils import user_manager
user = user_manager.UserManager()

def main():
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
        user.login()
    elif choice == '4':
        for name in user.user_accounts.items():
            print(f"{name}")
    else:
        print("No")

if __name__ == "__main__":
    user.load_user()
    main()