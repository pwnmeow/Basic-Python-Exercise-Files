import random

random_number = random.randint(1,10)  
num = None
while True:
	num = int(input("guess the number bw 1 - 10 "))
	if num == random_number:
		print("you guessed it right!")
	elif num < random_number:
		print("you guessed too low")
	else:
		print("thats too high")
		play_again = input("Do you want to play again (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			num = None
		else: print("thanks for playing")
		break
print(random_number)
