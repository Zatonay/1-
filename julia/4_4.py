"""
Вхідні дані #1
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Відповідь #1
4
3 3 2 12
"""

n1=int(input())
x1=[int(i) for i in input().split()]

n2=int(input())
x2=[int(i) for i in input().split()]

x3=[]

for i in x1:
    if i not in x2:
        x3.append(i)

print(len(x3))
print(*x3)



