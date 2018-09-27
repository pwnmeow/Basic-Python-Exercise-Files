
for x in range(0,21):
	if x % 2 == 0 and  x != 4:
		print(f"{x} is even")
	elif x == 4:
			print(f"{x} is UNLUCKY!!")
	elif x % 2 != 0 and x != 13: 
		print(f"{x} is odd")
	elif x == 13:
			print(f"{x} is UNLUCKY!!")