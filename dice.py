import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("enter the number of players(2-4)")
    if players.isdigit()  and 2 <= int(players) <= 4:
        players = int(players)
        break
    else:
            print("palyers should between 1 - 4")         

max_score = 69
player_scores = [ 0 for _ in range(players)]   

while max(player_scores) < max_score:

    for players_idx in range(players):
        print("\nplayer",players_idx + 1," turn has started\n")
        current_score = 0

    while True:  
        should_roll = input(" want to roll(y)")
        if should_roll.lower()!="y":
            break
        
        value = roll()
        if value == 1:
            print("turn done")
        else:
            current_score += value
            print("rolled",value)

        print("your score is",current_score)

    player_scores[players_idx] += current_score
    print("your total scoreis ",player_scores[players_idx])


     





