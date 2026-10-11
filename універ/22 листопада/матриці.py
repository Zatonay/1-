def writeMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end="")
        print()

def multiply(a,b):
    if len (a[0])!=len(b):
        return None
