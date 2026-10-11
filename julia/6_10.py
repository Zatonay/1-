"""
Вхідні дані #1
welcome to python!
Відповідь #1
wweellccoommee ttoo ppyytthhoonn!

"""

radok1=input()
radok2=""
for i in range(len(radok1)):
    if radok1[i] .isalpha():
        radok2+=radok1[i]*2
    else:
        radok2 += radok1[i]
print(radok2)

