def my_for(itreble,func):
	itrator = iter(itreble)
	while True:
		try:
			thing = next(itrator)
		except StopIteration:
			break
		else:
			func(thing)


my_for("hello",print )