from os import write

try:
    n = int(input())
except ValueError:
    print("введіть число")
else:


    if n==0 :
        print("Число дорівнює нулю")
    else:

        if n>0:
            print("Число більше нуля")
        if n<0:
            print("Число меньше нуля")


