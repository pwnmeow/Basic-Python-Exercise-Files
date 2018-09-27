import random
print("welcome to rock paper scissor in python ")
print("for rock chose r")
print("for paper chose p")
print("for scissor chose s")
player = input("make your move: ").lower()
rand_num = random.randint(0,2);
if rand_num == 0:
    computer = "r"
elif rand_num == 1:
    computer = "p"
else:
    computer = "s"
print(f"Computer plays {computer}")

if player == computer:
		print("its a tie")
elif player == "r":
	if computer == "s":
		print("player wins")
	elif computer == "p":
		print("computer wins")
elif player == "s":
	if computer == "p":
		print("player wins")
	elif computer == "r":
		print("computer wins")
elif player == "p":
	if computer == "r":
		print("player wins")
	elif computer == "s":
		print("computer wins")
else:print("invalid option")