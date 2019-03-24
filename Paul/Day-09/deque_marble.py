import collections


def play_game(players, turns):
    cir = collections.deque([0])
    player_list = [0] * players
    for marble in range(1, turns+1):
        if marble % 23 != 0:
            cir.rotate(-2)
            cir.appendleft(marble)
            #print(cir)
        else:
            player_index = marble % players
            cir.rotate(7)
            score = marble + cir.popleft()
            player_list[player_index] += score
            #print(cir)
    print(max(player_list))

play_game(493, 71863*100)