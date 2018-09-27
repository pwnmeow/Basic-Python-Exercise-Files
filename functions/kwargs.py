def fav_colors(**kwargs):
	for person,color in kwargs.items():
		print(f"{person}'s fav color is {color}")

fav_colors(sheeraz="red",unsa="pink")

