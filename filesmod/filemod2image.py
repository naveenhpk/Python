#to read an image
#f=open("path of file","rb")
#img=f.read()
# print(img)
# f.close()

# to writ the image into another file
#f=open("path of new file","wb")
#f.write(img)
# f.close()

#cursor position
print(f.tell())
#to change the cursor pocsit
f.seek(0,0) #(0 start,1 current,2 end)
