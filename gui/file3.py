from tkinter import *
root=Tk()

def close():
    root.destroy()

root.geometry("700x800")
root.title("Admission Form")
Label(root, text="First Name").grid(row=1)
Label(root, text="Last Name").grid(row=2)
Entry(root).grid(row=1,column=1)
Entry(root).grid(row=2,column=1)


Label(root, text="HOBBIES",font=("times new roman",15,"bold"),bg="black",fg="white").grid(row=3)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()


#CHECKBUTTON
Checkbutton(root,text="Drugs",variable=var1).grid(row=4,sticky=W)
Checkbutton(root,text="Game",variable=var2).grid(row=5,sticky=W)
Checkbutton(root,text="Guitar",variable=var3).grid(row=6,sticky=W)
Checkbutton(root,text="Bike",variable=var4).grid(row=7,sticky=W)

#radiobutton
Label(root,text="GENDER",font=("Times new roman",15,"bold")).grid(row=8)
Radiobutton(root,text="Male",variable=var5,value=1).grid(row=9,sticky=W)
Radiobutton(root,text="Female",variable=var5,value=2).grid(row=10,sticky=W)


Button(root,text="Close Form",command=close,bg="black",fg="white",width=10,height=3).grid(row=40,column=1)
mainloop()
