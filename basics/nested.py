age = input("How old are you ?")
if age:
    age = int(age)
if age >= 18 and age < 21: 
    print("You can enter but need wristband")
elif int(age) >= 21 :
    print("you can enter and drink")
else:
    print("you cant enter little one :(")

