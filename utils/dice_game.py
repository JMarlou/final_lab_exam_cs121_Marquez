class DiceGame():
    def load_scores(self):
        try:
            with open("scores.txt", 'r') as f:
                for line in f:
                    user = line.strip().split(',')
                    self.users[user[0]] = int(user[1])
        except FileNotFoundError:
            print("Scores file not found.")
        except Exception as e:
            print(f"Error loading users: {e}")

    def save_scores(self):
        with open('scores.txt', 'w') as f:
            for username, scores in self.user_accounts.items():
                f.write(f'{username},{scores.points}, {scores.win}\n')

    def play_game():
        pass

    def show_top_score():
        print("\nScores:")
        scores = []
        try:
            with open("scores.txt", 'r') as f:
                for line in f:
                    username, score, win = line.strip().split(',')
                    scores.append((username, int(score), int(win)))
            scores.sort(key=lambda x: x[1], reverse=True)
            for username, score, win in scores:
                print(f"{username}: {score} ({win} win{'s' if win > 1 else ''})")
        except FileNotFoundError:
            print("Scores file not found.")
        except Exception as e:
            print(f"Error loading scores: {e}")

    def logout():
        pass

    def menu():
        pass