time = int(input("whats the time ?"))
place = input("whats the place of pick up ?")
person = input("whats your name ? ")

 
if time <= 12:
	if place == "karond-k" or place == "7dukan-k" or place == "bhopalt-k" or place ==  "hamidia-k":
		print("you are drunk")
else: print("you are not drunk")		