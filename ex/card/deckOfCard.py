from random import shuffle 
class Card:
	def __init__(self, value,suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"


c  = Card("A","Heart")
c2 = Card("10","diamond")
c3 = Card("K","Spades")
print(c,c2,c3)


class Deck:
	def __init__(self):
		suits = ["Hearts","Diamond","Clubs","Spades"]
		values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		self.cards = [Cards(values,suit) for suit in suits for value in values]
		print(self.cards)

	def __repr__(self):
		return f"deck of {self.count} cards"
	
	def count(self):
		return len(self.cards)

	def _deal(self,num):
		count = self.count()
		actual = min([count,num])
		print f"Going to remove {actual} cards"
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def deal_card(self):
		return self.deal(1)[0]
	def deal_hand(self,num):
		self._deal(hand_size)
	def shuffle(self):
		if self.count() <52:
			raise ValueError("only full deck can bbe shuffled")
		shuffle(self.cards)
		return self

d = Deck()
d._deal(5)
print(d)
