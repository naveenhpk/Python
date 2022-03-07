num=int(input("Enter a number:"))
x=['','one','two','three','four','five','six','seven','eight','nine',]
x2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
x3=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
if num<10:
	print("%d:%s"%(num,x[num]))
elif 10<=(num)<20:
	print("%d:%s"%(num,x2[num%10]))
elif 20<=num<100:
	print("%d:%s"%(num,x3[num//10]+x[num%10]))
else:
	tens=num%100
	print("%d:%s"%(num,x[(num//100)]+"hundred"+x3[tens//10]+x[tens%10]))
