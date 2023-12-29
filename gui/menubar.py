from tkinter import *  #<ERROR>
root=Tk()
root.geometry("700x800")
root.title("MENU")
txt=Text(root,bg="Black",fg="white")
txt.pack()

# def info1():
#     # print("Hello, I am Misha but not literally.") <shows result in terminal>
#     output=("Hello, I am Misha but not literally.")
#     txt.insert(END,output)

# def info2():
#     # print("Hello, Luzman is my name and I like to take free kills.")
#     output=("Hello, Luzman is my name and I like to take free kills.")
#     txt.insert(END,output)

# def info3():
#     # print("Hello, Raka mera naam.")
#     output=("Hello, Raka mera naam.")
#     txt.insert(END,output)

# def close():
#     root.destroy()

# mymenu=Menu(root)
# mymenu.add_command(label="Misha",command=info1)
# mymenu.add_command(label="Luzman",command=info2)
# mymenu.add_command(label="Raka",command=info3)
# mymenu.add_command(label="EXIT",command=close)



def file():
    output=("File")
    txt.insert(END,output)

def edit():
    output=("Edit your face")
    txt.insert(END,output)

def view():
    output=("OutPut")
    txt.insert(END,output)

def clear():
    txt.delete("1.0",END)


mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label="New",command=file)
filemenu.add_command(label="New Window",command=file)
filemenu.add_command(label="Open",command=file)
filemenu.add_separator()
filemenu.add_command(label="Save",command=file)
filemenu.add_command(label="Save As",command=file)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
mainmenu.add_cascade(label="File",menu=filemenu)

Editmenu=Menu(mainmenu,tearoff=0)
Editmenu.add_command(label="Copy",command=edit)
Editmenu.add_command(label="Paste",command=edit)
Editmenu.add_separator()
Editmenu.add_command(label="Open",command=edit)
mainmenu.add_cascade(label="Edit",menu=Editmenu)

Viewmenu=Menu(mainmenu,tearoff=0)
Viewmenu.add_command(label="Zoom in",command=view)
Viewmenu.add_command(label="Zoom out",command=view)
mainmenu.add_cascade(label="View",menu=Viewmenu)


Button(text="CLEAR",command=clear).pack()

root.config(menu=mainmenu)
root.mainloop()