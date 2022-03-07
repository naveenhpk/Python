a=int(input("Enter the age"))
class Ageerror(Exception):
    def __init__(self):
        self.msg="Age error occur Age is less than 18"

try:
    if a<18:
        raise Exception("Some error has occures")
        # raise Ageerror
except Ageerror as e:
    print(e.msg)
else:
    print("PGM runned susscessfully")