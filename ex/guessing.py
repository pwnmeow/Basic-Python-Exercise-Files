import random

random_number = random.randint(1,10)  
num = None
while num != random_number:
	num = int(input("guess the number bw 1 - 10 "))
	if num == random_number:
		print("you guessed it right!")
	elif num < random_number:
		print("you guessed too low")
	else:
		print("thats too high")
print(random_number)
