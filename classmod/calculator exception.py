class Calculator:
    def add(self):
        self.result=a+b
    def sub(self):
        self.result=a-"b"
    def mul(self):
        self.result=a*b
    def div(self):
        try:
            self.result=a//b
        except ZeroDivisionError:
            print("ZERO DIVISION ERROR:  Division by zero not possible")
    def display(self):
    	print(self.result)
obj=Calculator()
while True:
    try:
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        ch=int(input("Enter Your Choice: "))
        a=int(input("Enter 2 numbers: "))
        b=int(input("Enter the 2nd number: "))
        if ch==1:
            obj.add()
            print("Sum :",end='')
            obj.display()
        elif ch==2:
            obj.sub()
            print("Difference :",end='')
            obj.display()
        elif ch==3:
            obj.mul()
            print("Product :",end='')
            obj.display()
        elif ch==4:
            obj.div()
            print("Division: ",end='')
            obj.display()
        else:
            print("Enter Valid Choice")
        con=input("do you want to continue (y-Yes) (n-No): ")
        if con=='n':
            print('Exiting...')
            break
    except ValueError as e:
        print("Value Error",e)
    except NameError as e:
        print("Name error",e)
    except TypeError as e:
        print("Type error",e)
    except AttributeError:
        print("Attribute error",e)
    except KeyboardInterrupt:
        print("Keyboard Interupt error")
    except IndentationError as e:
        print("Intendation error",e)
    # except OverflowError:  
    #     print ("OverFlow Exception.")
    # except ArithmeticError:
    #     print("Arithematic error:   Division by zero not possible")
    finally:
        print("Pgm stopped")