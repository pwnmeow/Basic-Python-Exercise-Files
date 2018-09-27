nestedList = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print( nestedList[-2][-1] )#[last list second,last objeact]
print( nestedList[1][3] )

print("#######################################################")

for x in nestedList: # takes every single list in x 
	for val in x: # takes out one value each time from each list
		print(val)

print("#######################################################")
boardGame = [ [num for num in range(1,4)] for val in range(1,4)]
print( boardGame ) #num for num in range(1,4) = [1,2,3] then repeat 3 times

boardGame1 = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)] 
print("#######################################################")

symbols = [ [ "@" if num % 2 != 0 else "#" for num in range(1,4)] for val in range(1,4)]

l = [[ ]]
print("#######################################################")
print(boardGame1)