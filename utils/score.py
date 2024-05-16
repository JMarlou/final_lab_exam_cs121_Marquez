from .user import *

class Score:
    def __init__(self, username, points, wins, gameID):
        self.username = username
        self.points = points
        self.wins = wins
        self.gameID = gameID