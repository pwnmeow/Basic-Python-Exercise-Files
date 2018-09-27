class Counter:
	def __init__(self,low,high):
		self.low = low
		self.high = high

	def __iter__(self):
		return iter("hello")

	def __next__(self):
		return 1

c = Counter(0,10)
iter(c)

for x in Counter(0,10):
	print(x)