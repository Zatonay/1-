# def write_ints(filename,array) :
#     f=open(filename, "wb")
#     for n in array:
#         x= b.to_bytes(2, "big", signed=True)
#
#
#
#
# from array import array
#
#
# def read_ints(flename):
#     array=[]
#     f=open


# opentry:
#     assrt 0 <10
# except ZeroDivisionError
#
#


try:
    condition = True and 1 > 10
    assert condition," Assertion"
    raise ZeroDivisionError("My exception")
except ZeroDivisionError as e:
    print(e)
except ArithmeticError:
    pass
except ArithmeticError as e :
    print (e)
finally:
    print("Hello!")
