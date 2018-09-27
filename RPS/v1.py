print("rock")
print("paper")
print("scissors")

player1 = input("PLAYER 1 , MAKE YOUR MOVE: ")
player2 = input("PLAYER 2 , MAKE YOUR MOVE: ")


if player1 == "r" and player2 == "s":
    print("player 1 wins")
elif player1 == "r" and player2 == "p":
    print("player 2 wins")
elif player1 == "s" and player2 == "p":
     print("player 1 wins")
elif player1 == "s" and player2 == "p":
     print("player 1 wins")
elif player1 == "p" and player2 == "s":
     print("player 2 wins")
elif player1 == "s" and player2 == "r":
     print("player 2 wins")
elif player1 == "s" and player2 == "r":
     print("player 2 wins")
elif player1 == "p" and player2 == "r":
     print("player 1 wins")
elif player1 == player2:
    print("its a tie")
else: print("something went wrong")


    
