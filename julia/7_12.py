"""
Приклади
Вхідні дані #1
2000 2015
Відповідь #1
2013 2014 2015
Вхідні дані #2
9875 9999
Відповідь #2
9875 9876
"""
def check(n):
    k=str(n)
    if k[0]==k[1] or k[0]==k[2] or k[0]==k[3] or k[1]==k[2] or k[1]==k[3] or k[2]==k[3]:
        return False
    else:
        return True

a,b=[int(i) for i in input().split()]
for j in range(a,b+1) :
    if check(j):
        print(j,end= " ")


