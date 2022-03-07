from tkinter import *

Toggle=Tk()    #Toggle
Toggle.geometry("500x500")
Toggle.title("Zoom APP") 
txt1=StringVar()
txt1.set("HAI")
lb1=Label(Toggle, textvariable=txt1) 
lb1.place(x=250,y=220)
#button add aakan
def change():
    if txt1.get()=="HAI":
        txt1.set("NAVEEN")
    else:
        txt1.set("HAI")
but=Button(Toggle,text="Click me",command=change)
but.place(x=250,y=250)
Toggle.mainloop()