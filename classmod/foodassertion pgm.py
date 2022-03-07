a= [15,25,45,55,12,23,20,93,58]
a.sort()  
for i in a: 
    assert i <= 40, "FOOD TEMPERATURE GREATER THAN 40 IS REJECTED"
    print (i," FOOD IS ACCEPTED" )