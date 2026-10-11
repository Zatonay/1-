def readfile(filename):
    with open(filename, encoding="utf-8") as f:
        return f.readlines()
    return lines

def a(filename):
    lines = readfile( filename)
    print(*lines)


def b(filename):

    lines = readfile( filename)
    x=""
    for line in lines :
        if len(line)>len(x):
            x=line
    print(x)


        # if len(line) > len(line):
        #     print(line)

if __name__=='__main__':
    b("input.txt")
