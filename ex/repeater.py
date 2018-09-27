howmany = int(input("how many times do i have to tell you ? "))
message = input("Enter the message here what you want done: ")

for x in range(howmany):
	print(f"times {x+1} {message}")
for num in range(0,21):
	if num == 4 or num == 13:
		print(f"{num} is UNLUCKY!")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:print(f"{num} is odd")

for num in range(0,21):
	if num == 4 or num == 13:
		state = "UNLUCKY!"
	elif num % 2 == 0:
		state = "even"
	else:state = "odd"
	print(f"{num} is {state}")


for x in range(0,21):
	if x % 2 == 0 and  x != 4:
		print(f"{x} is even")
	elif x == 4:
			print(f"{x} is UNLUCKY!!")
	elif x % 2 != 0 and x != 13: 
		print(f"{x} is odd")
	elif x == 13:
			print(f"{x} is UNLUCKY!!")