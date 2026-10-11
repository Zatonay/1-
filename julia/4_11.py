"""
Вхідні дані #1
4
1 2 3 4
Відповідь #1
4 1 2 3
"""

n=int(input())
x=[int(i) for i in input().split()]
for i in range(n-1,0,-1) :
    a=x[i-1]
    x[i-1]= x[i]
    x[i]=a
print(*x)

