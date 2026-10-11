"""
Вхідні дані #1
palindrom
Відповідь #1
NO

Вхідні дані #2
a roza upala na lapu azora
Відповідь #2
YES
"""

radok=input()
radok=radok.replace( " ", "")
if  radok[::-1]== radok:
    print("YES")
else:
    print("NO")



