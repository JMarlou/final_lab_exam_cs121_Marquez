from utils import user_manager
from utils import dice_game
dice = dice_game.DiceGame
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
         
    elif choice == '3':
        exit()
    else:
        print("Invalid Input")
   
def login_menu(self):
    dice.load_scores()
    print(f"Welcome {self.username}!")
    print("Menu: ")
    print("1. Start Game")
    print("2. Show top scores")
    print("3. Logout")

    choice = input("Choose Action: ")

    if choice == '1':
        dice.play_game()
    elif choice == '2':
        dice.show_top_scores()
    elif choice == '3':
        return
    else:
        print("Invalid Input")
        login_menu(self)
            

if __name__ == "__main__":
    user.load_user()
    main()