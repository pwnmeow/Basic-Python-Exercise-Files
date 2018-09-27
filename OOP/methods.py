class User:
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
	def fullName(self):
		return f"{self.first} {self.last}"

	def initials(self):
		first = self.first
		last = self.last
		return f"{first[0].last[0]}"
	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def isSenior(self):
		return self.age >= 65


user1 = User("jhon","snow",37)

print(user1.fullName())