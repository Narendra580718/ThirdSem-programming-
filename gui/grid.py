#grid
from tkinter import*
root=Tk()
root.geometry("700x600")
root.title("hemloo")
Label(text="Hi! How you doing?", font=("Algerian",18), bg="lightyellow", fg="Black").grid()
n=Label(text="Doing Great",font=("Algerian",16),relief= RAISED, background="gray", foreground="white")
n.grid(row=2,column=1)
p=Label(text="Awesome", relief= SUNKEN, bg="palegreen", fg="Black", font="Arial 18 underline bold")
p.grid(row=6,column=6)
root.mainloop()
from tkinter import *
root=Tk()
root.geometry("700x700")
a=Button(text="Click Me", relief=RAISED, font=("Algerian",18), bg="Gray", fg="Black")
a.grid(column=1, row=2)
b=Button(text="close",font=("Algerian",18), command=root.destroy)
b.grid(column=3, row=2)

root.mainloop()