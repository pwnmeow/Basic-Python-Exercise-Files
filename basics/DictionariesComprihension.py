nums = dict(first=1, second=3, third=2)

sq_num = {key: value ** 2 for key,value in nums.items()}

print(sq_num)

str1 ="ABCD"
str2 = "12345"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)


instructor = {
    "name": "Colt",
    "favorite_language": "Python",
}

yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

print(yelling_instructor)

nuems = [1,2,3,4]

print({num:("even" if num % 2 == 0 else "odd") for num in range(1,100)})


