nums = [1,2,3,4]

print([x+x for x in nums]) # [2, 4, 6, 8]

friends = ["sheeraz","faraz","aasim","unsa"]

print([x[0].upper() for x in friends]) # ['S', 'F', 'A', 'U']

name ="unsa"

print([char.upper() for char in name]) # ['U', 'N', 'S', 'A']

empty  =["",0,[]]

print([bool(char) for char in empty]) # [False, False, False]