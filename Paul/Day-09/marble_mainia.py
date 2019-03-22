# 459 players; last marble is worth 71790 points
import datetime

class Circle(object):
    def __init__(self):
        self.circle = [0]
        self.current_index = 0

    def set_current_index(self, new_index):
        self.current_index = new_index

    def current_marble(self):
        return self.circle[self.current_index]

    def insert_marble(self, new_marble):
        if self.current_index == len(self.circle)-1:
            insert_location = 1
        elif self.current_index == len(self.circle)-2:
            insert_location = len(self.circle)
        else:
            insert_location = self.current_index + 2

        self.circle.insert(insert_location, new_marble)
        self.set_current_index(insert_location)

    def multiple_of_23(self, new_marble):
        removed_marble_index = self.current_index - 7
        if removed_marble_index < 0:
            removed_marble_index = len(self.circle) + removed_marble_index
        removed_marble = self.circle.pop(removed_marble_index)
        self.set_current_index(removed_marble_index)
        return new_marble + removed_marble

    def __str__(self):
        return str([" {} ".format(i) if i != self.current_marble()
                    else "({})".format(i) for i in self.circle])


class Players(object):
    def __init__(self, n):
        self.n = n
        self.player_list = [0] * (n+1)
        self.current_player = 1

    def find_current_player(self, turn):
        if turn % self.n == 0:
            return self.n
        else:
            return turn % self.n

    def add_score(self, index, score):
        self.player_list[index] += score

    def top_score(self):
        return max(self.player_list)

    def winner(self):
        return self.player_list.index(self.top_score())

    def __str__(self):
        return str([i for i in self.player_list])


def play_game(num_of_players, turns):
    circle = Circle()
    players = Players(num_of_players)
    # print("[-]", circle)
    for turn in range(1, turns+1):
        current_player = players.find_current_player(turn)
        if turn % 23 == 0:
            player_score = circle.multiple_of_23(turn)
            players.add_score(current_player, player_score)
        else:
            circle.insert_marble(turn)
        # print("["+str(current_player)+"]", circle)
    # print(players)
    print("player {} won with a score of {}".format(players.winner(), players.top_score()))


print('the code started at:', datetime.datetime.now())
play_game(493 , 71863*100)
print('the code finished at:', datetime.datetime.now())