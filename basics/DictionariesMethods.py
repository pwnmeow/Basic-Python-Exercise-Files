#clear clears the whole dictionary 


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

instructor.clear()

#copy - it makes copy of a dictionary

clone  = instructor.copy()

#fromkeys  used to create one value in all the object 

{}.fromkeys("a","b") #{'a':'b'}

 newUser = {}.fromkeys(['name','score','email','profile bio'],'unknown')
>>> newUser
{'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}

# always put in a list or chars become list
##############################Problem
newUser = {}.fromkeys('phone','unknown')
>>> newUser
{'p': 'unknown', 'h': 'unknown', 'o': 'unknown', 'n': 'unknown', 'e': 'unknown'}

###############################Solution
>>> newUser = {}.fmromkeys(['phone'],'unknown')
>>> newUser
{'phone': 'unknown'}

##########################################################
					#Get 
##########################################################

instructor.get('name')
#checks if key is in the dictionary

##########################################################
					#Pop
##########################################################

instructor.pop("owns_dog")
#Returns a True if removed key

instructor.popitem()
#Returns the key the last one and takes no arguments
##########################################################

###########################################################
					#Update
###########################################################


