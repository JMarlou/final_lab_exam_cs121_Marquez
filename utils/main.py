from user_manager import *
Register = UserManager()

def main():
    print("Welcome to Dice Roll Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
	
    choice = input("Action: ")

    if choice == '1':
        Register.register()
        main()
    else:
        print("No")


if __name__ == "__main__":

	main() 