def special_greating(**kwargs):
	if "Daived" in kwargs and kwargs["Daived"] == "speacial":
		return "you get a speacial greating Daived"
	elif "Daived" in kwargs:
		return f"{kwargs['Daived']} Daived!!"
	return f"Not sure who this is"

print(special_greating(Daived="hello"))
print(special_greating(Daived="speacial"))
print(special_greating(ron="hello"))
print(special_greating(helio="hello",Daived = "speacial"))
