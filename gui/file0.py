from tkinter import *
root = Tk()

#size manupulation
root.geometry("750x600") #WIDTH BY HEIGHT
root.minsize(500,50)
root.maxsize(1920,1080)

#title
root.title("HELLO Nibba/nibbi")

Label(text="Goodbye cruel world",font=("garamond",50),bg="grey").pack() #text comes on center
a=Label(text="Nikal")
a.pack(side="bottom")

b=Label(text="Going",relief="raised",background="green",foreground="white",font=("garamond",30))
b.pack(side="right")

Label(text="Not going",background="black",foreground="white").pack(side="left")
#code to run widget will go here.
root.mainloop()
