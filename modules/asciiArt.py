import pyfiglet
from termcolor import colored
msg = input("write bitch!!!! ")
color = input("what color ")

art = pyfiglet.figlet_format(msg)
colordArt = colored(art,color="red")
print(colordArt)