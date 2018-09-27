import requests 
from bs4 import BeautifulSoup
from time import sleep
from random import choice
all_quotes =[]
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
	res = requests.get(f"{base_url}{url}")
	print(f"new Scraping {base_url}{url}.....")
	soup = BeautifulSoup(res.text,"html.parser")
	quotes = soup.find_all(class_="quote")

	for quote in quotes:
		all_quotes.append({
			"text":quote.find(class_="text").get_text(),
			"author":quote.find(class_="author").get_text(),
			"bio-link":quote.find("a")["href"]
			})
	next_btn = soup.find(class_="next")
	url = next_btn.find("a")["href"] if next_btn else None
quote = choice(all_quotes)
print("heres a quote: ")
print(quote['text'])
print(quote['author'])

rem_guesses = 4
guess =''
while guess.lower() != quote["author"].lower() and rem_guesses > 0: 
	guess = input(f"who said this qoute? remaining Guesses {rem_guesses}")
	rem_guesses -= 1
	if rem_guesses == 3:
		res = requests.get(f"{base_url}{quote['bio-link']}")
		soup = BeautifulSoup(res.text,"html.parser")

print("after While Loop")