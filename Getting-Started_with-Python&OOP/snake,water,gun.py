import random

def swg(player,computer):
    if( player==computer ):
        return "Draw"
    elif(( player == "S" and computer == "W") or
        ( player == "W" and computer == "G") or
        ( player == "G" and computer == "S") ):
        return "Player Wins"
    else:
        return "Computer Wins"

choices = ["S","W","G"]
print("enter computers choice:")
computer = random.choice(choices)
print("enter players choice:")
player = input().upper()
result=swg(player,computer)
print(result)



# import random

# def check_winner(player, computer):
#     if player == computer:
#         return "Draw"

#     # winning conditions for player
#     if (player == "S" and computer == "W") or \
#        (player == "W" and computer == "G") or \
#        (player == "G" and computer == "S"):
#         return "You Win"
#     else:
#         return "Computer Wins"


# # possible choices
# choices = ["S", "W", "G"]

# # computer chooses randomly
# computer = random.choice(choices)

# # user input
# player = input("Enter S (Snake), W (Water), G (Gun): ").upper()

# # result
# print("Computer chose:", computer)
# print("You chose:", player)

# result = check_winner(player, computer)
# print(result)