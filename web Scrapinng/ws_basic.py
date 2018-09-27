import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blogdata.csv", "w") as file:
	writer = writer(file)
	writer.writerow(["title","link","date"])
	for art in articles:
		title = art.find("a").get_text()
		href = art.find("a")["href"]
		date = art.find("time")["datetime"]
		writer.writerow([title,href,date])


# all_qoute =[]
# response = requests.get("http://quotes.toscrape.com/")
# soup = BeautifulSoup(response.text,"html.parser")
# # Qoute Scraped 
# qoutes = soup.find_all(".quote")
# for qoute in qoutes:
# 	all_qoute.append({
# 		"text": qoute.find(class_="text").get_text(),
# 		"author": qoute.find(class_="author").get_text(),
# 		"bio-link":qoute.find("a")["href"]
# 		})

# print(all_qoute)
