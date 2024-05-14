from user_manager import *
User = UserManager()

def main():
    print("Welcome to Dice Roll Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
	
    choice = input("Action: ")

    if choice == '1':
        User.register()
        main()
    elif choice == '2':
        User.login()
    elif choice == '4':
        for name in User.user_accounts.items():
            print(f"{name}")
    else:
        print("No")


if __name__ == "__main__":

	main() 