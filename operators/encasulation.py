class A:
    _age=30
    address="kannur"
    __number=484758454
    def __init__(self):
        self.name="Naveen"
        self.__number+=2
        A._age=50
        print(A._age)

print(A.address)
print(A._age)
obj=A()
print(obj._A__number)
