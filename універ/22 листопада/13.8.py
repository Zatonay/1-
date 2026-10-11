from binascii import Error


def readPolinon(file):
    try:
        coefs={}
        with open(file) as f:
            for line in f :
                power, coef = line.split()
                power=int(power)
                coef= float(coef)
                coefs[power]= coef

        return coefs
    except FileNotFoundError: # якщо файл не знайдений
        print("Filen not found")
        return None

    except ValueError:
        print("Filen not good")
        return None

    except Error:
        if coefs>2:
            print("a lot of чисел")
            return None


    except Error:
        if file(Polinon) :   #file(Polinon) dont be
            print("a lot of чисел")
            return None


print(readPolinon().read())

# if __name__== ' __main__':
#     readPolinon('polinol.txt')