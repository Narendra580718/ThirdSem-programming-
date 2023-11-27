f=open("InfoManjul.txt", "w")

f.write("Name: Manjul aka HeckerMan")
f.write("\nAddess: Bhaktapur, Gathhaghar. ")
f.write("\nAge: 24")
f.write("\nEmail: heckerman_m@gmail.com")
f.write("\nPh.no. 9841bakisabaaafaihanus")
f.close()

f=open("InfoManjul.txt","r")
print(f.read())
f.seek(0) #reads from the beginning
print(f.readline())
f.seek(0)
print(f.readlines())
print(f.tell())
f.close

