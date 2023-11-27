f=open("basic.py","r")
print(f.read())
f.close()

# f=open("Newfile.txt","x")
# f.write("new file")
# f.close()

f=open("Newfile.txt","w")
f.write("WELCOME TO NEPAL!!!")
f.write("\nVisit Kathmandu")
f.close()


f=open("Newfile.txt","a")
f.write("\nNew line")
f.close()
