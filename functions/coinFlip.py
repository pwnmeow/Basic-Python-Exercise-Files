import random

def coilflip ():
	coinValue = random.randint(0,1);
	if coinValue == 1:
		print("heads")
	else:print("tails")

coilflip()