from csv import reader
with open("data.csv") as file:
	csv_reader = reader(file)
	data = list(csv_reader)
	for row in csv_reader:
		print(row)

from csv import DictReader
with open("data.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row)