instructor = ['colt',True, 4, "python",False] #List only one bitch\

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

print(instructor["name"])
print(instructor["owns_dog"])
print(instructor["num_courses"])
print(instructor["favorite_language"])
print(instructor["is_hilarious"])
print(instructor[44])


for value in instructor.values():
    print(value)

# "Colt"
# True
# 4
# "Python"
# False
# "my favorite number!"

for key in instructor.keys():
    print(key)

# name
# owns_dog
# num_courses
# favorite_language
# is_hilarious
# 44

for key,value in instructor.items():
    print(key,value)

# name "Colt"
# owns_dog True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number!"

for v in instructor.values():
	print(v)
print("##################################")
for v in instructor.keys():
	print(v)
print("##################################")
for v in instructor.items():
	print(v)
print("##################################")

for k,v in instructor.items():
	print(f"key is {k} and value is {v}")