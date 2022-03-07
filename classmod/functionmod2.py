# gloabaly accesing varaible inside the function
a=3
b=5

def myfun():
    #accesing outside variable 
    global a
    a=a+3
    b=3
    print(a)
    def hai():
        #acessing value inside the function of anathor function
        nonlocal b
        b+=5
        print(b)
    hai()
myfun()
print(a)



# lamda function:it is a single line list,any number of argumnets can be given but only 1 expression
#syntax:lamda argument:expression
a=lambda x:x**3
#calling lambda functon
print(a(5))
print(b(3,4,4))
