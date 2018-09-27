import requests
import pyfiglet
import termcolor
from termcolor import colored
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
print(header)
topic = input("what joke do you want: ")

response = requests.get(
	"https://icanhazdadjoke.com/search",
	headers={"Accept":"application/json"},
	params={"term":topic}
)
data = response.json()
joke = data["results"]
jokeCount = int(data["total_jokes"])

if jokeCount > 1:
	print(f"there are {jokeCount} jokes about your topic")
	print(f"heres your joke lol {choice(joke)['joke']}")
elif jokeCount == 1:
	print(
		f"I've got one joke about {topic}. Here it is:\n",
        joke[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")