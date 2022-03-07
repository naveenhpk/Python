#unordered collection of elements
example={1:'one','two':2,"hello":5.36}
print(example["two"])
#insert
example["hai"]="hello how do u do"
print(example)
#delete
del example["hai"]
print(example)
#update
example["two"]="number 2"
print(example)
#
print('value of 1 is ',example.get(3,"Not fond"))
#create dictnary by using 2 list
l1=["one","two","three","four"]
l2=[1,2,3,4]
dictionary=dict(zip(l1,l2))
print(dictionary)
dictionary=dict.fromkeys(l1,10)
print(dictionary)
#
print(example.keys())
print(example.value())
print(example.items())
#pop delete ;but returns the value
print(example.pop("hello"))
#pop item deetes the last inserted item
example["koii"]="poda"
print(example.popitem())
#add list in dictnary & how to accces values uses index
example['list']=l1
print(example)
print(example['list'][2])
#adding dictnary to a dictnary and accesing dictnary values uses keys
example["dictnary"]=dictionary
print(example)
print(example["dictnary"]["four"])