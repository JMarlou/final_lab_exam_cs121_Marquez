import random
import os
import datetime
from .score import Score

class DiceGame:
    user_score = {}
    points = 0
    wins = 0

    def load_scores(self):
        if not os.path.exists("scores.txt"):
            with open('scores.txt', 'w') as f:
                f.write("")
        else:
            with open('scores.txt', 'r') as f:
                for line in f:
                    values = line.strip().split(',')
                    if len(values) == 4:
                        username = values[0]
                        points = int(values[1])
                        wins = int(values[2])
                        gameID = values[3]
                        if username not in self.user_score:
                            self.user_score[username] = []
                        self.user_score[username].append(Score(username, points, wins, gameID))

    def save_scores(self):
        with open('scores.txt', 'w') as f:
            for scores in self.user_score.values():
                for score in scores:
                    f.write(f"{score.username},{score.points},{score.wins},{score.gameID}\n")

    def show_top_score(self):
        pass

    def save_and_reset(self, username):
        gameID = datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.user_score[username] = [Score(username, self.points, self.wins, gameID)]
        self.save_scores()
        self.points = 0
        self.wins = 0

    def play_game(self, username):
        input("Press Enter to Start the Game!")
        while True:
            if self.dice(username):
                print("Would you like to play again? (yes/no): ")
                play_again = input().lower()
                if play_again == "yes":
                    continue
                elif play_again == "no":
                    self.save_and_reset(username)
                    print("Thanks for playing!\n")
                    self.menu(username)
                    break
                else:
                    print("Invalid Input!\n")
                    self.menu(username)
                    break
            else:
                break

    def dice(self, username):
        RoundWin = 0
        RoundLoss = 0
        print("Starting Game.....\n")
        input("Press Enter to Roll the Dice\n")

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
            else:
                print("It's a tie this round!")

            input("Press Enter to Continue!\n")  

        if RoundWin == 2:
            print(f"Congratulations, {username}! You won the stage!")
            self.points += 3
            self.wins += 1
        elif RoundLoss == 2:
            print(f"Sorry, {username}. You lost the stage.")

        print(f"You have won {self.wins} stages so far.")
        print(f"You currently have {self.points} points so far.")
        return True

    def menu(self, username):
        self.load_scores()
        print(f"Welcome {username}!\n")
        print("Menu: ")
        print("1. Start Game")
        print("2. Show top scores")
        print("3. Logout")

        choice = input("Choose Action: ")

        if choice == '1':
            self.play_game(username)
        elif choice == '2':
            self.show_top_score()
            input("Press Enter to Continue!")
            self.menu(username)
        elif choice == '3':
            return    
        else:
            print("Invalid Input")
            self.menu(username)
        