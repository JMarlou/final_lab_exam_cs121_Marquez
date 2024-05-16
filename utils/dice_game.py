import random
from .score import Score

class DiceGame:
    user_score = {}
    points = 0
    wins = 0

    def load_scores(self):
        pass
    def save_scores(self):
        pass

    def show_top_score(self, username):
        print("===LEADERBOARD===")
        for scores in self.user_score.items():
            print(f"[{username}: {self.scores}]")

    def play_game(self, username):
        input()
        while True:
            if self.dice(username) == True:
                input()
            else:
                break

    def dice(self, username):
        RoundWin = 0
        RoundLoss = 0
        print(f"Starting Game.....")
        input()
        while RoundWin < 2 and RoundLoss < 2:
            user = random.randint(1,6)
            computer = random.randint(1,6)
            print(f"{username} rolled a {user}")
            print(f"Computer rolled a {computer}")
            if user < computer:
                print("You lost this round!")
                RoundLoss += 1
            elif user > computer:
                print("You won this round!")
                RoundWin += 1
                self.points += 1
            elif user == computer:
                print("It's a tie this round!")
            input()  

        if RoundWin == 2:
            print(f"Congratulations, {username}! You won the game!")
            self.points += 3
            self.wins += 1
        elif RoundLoss == 2:
            print(f"Sorry, {username}. You lost the game.")

        print(f"You have won {self.wins} stages so far.")
        print(f"You currently have {self.points} points so far.")
        print("Would you like to play again? (yes/no): ")
        play_again = input().lower()
        if play_again == "yes":
            self.dice(username)
        elif play_again == "no":
            print("Goodbye!")
            self.menu(username)
        else:
            print("Invalid Input!\n")
            self.menu(username)
        self.user_score[username] = Score(self.points, self.wins)

    def menu(self, username):
        print(f"Welcome {username}!\n")
        print("Menu: ")
        print("1. Start Game")
        print("2. Show top scores")
        print("3. Logout")

        choice = input("Choose Action: ")

        if choice == '1':
            self.play_game(username)
        elif choice == '2':
            self.show_top_score(username)
        elif choice == '3':
            return
        else:
            print("Invalid Input")
            self.menu(username)
        