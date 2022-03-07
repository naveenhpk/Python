a=int(input("Enter a number"))
class Ageerror(Exception):
    def __init__(self):
        self.a=a
try:
    if a<10:
        raise Exception("Number too small")
    elif a>25:
        raise Exception("Number too large")
except Exception as e:
    print(e)
else:print("you have selected ",a)