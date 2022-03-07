try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    # ip
    # print("sum is:",a+b)
#     print("an errror has occured in the input",e)
except ValueError as e:
    print("Input not correct",e)
except NameError as e:
    print("Name not foound",e)
else:   #error onnum illenki
    print("sum:",a+b)

finally:
    print("Pgm stoped")# error indenkilum illenkilum print cheyyan
