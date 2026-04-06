"""
Author: Shubhkarman Saharan (164698219)
Group: 12
Date: 2026-04-04
"""

import random



#functions
def roll_dice():
    roll = random.randint(1, 6)
    print(f"Roll : {roll}")
    return roll


def move_player(player):
    #basic die roll
    players[player] += roll_dice()

    #check for snl
    if players[player] in snl:
        if players[player] < snl[players[player]]:
            print(f"===={player} climbs ladder to {snl[players[player]]}")
        else:
            print(f"===={player} slides down snake to {snl[players[player]]}")
        players[player] = snl[players[player]]
    
    #check for overflow
    if players[player] >= 30:
        players[player] = 30
        print(f"===={player} wins!====")
    
    return players[player]


def display():
    print("-"*10)
    for p in players:
        print(f"{p} : {players[p]}")

    print("-"*10, "\n")


#board , players
snl = {
    2 : 29,
    4 : 20,
    6 : 9,
    28 : 1,
    15 : 8
}

players = {}


#game
print("Snakes and ladders")
p1 = str(input("Enter player1 name : "))
p2 = str(input("Enter player2 name : "))
players[p1] = 0
players[p2] = 0


display()

winner = None
turn = 0
while not winner:
    #print turn number
    turn += 1
    print(f"Turn : {turn}")

    #move player
    for p in players:
        input(f"{p} press Enter to roll")
        players[p] = move_player(p)

        #check for winner
        if players[p] == 30:
            winner = p
            break
    #display positions
    display()
