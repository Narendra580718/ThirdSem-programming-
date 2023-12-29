# 1. WAP to enter your name, address, gender, age, faculty and roll_number into a filename "info.txt"
# 2. WAP to display name, address, and faculty from the file "info.txt"

f=open("info.txt", "w")

f.write("Name: Narendra")
f.write("\nAddress: Balaju")
f.write("\nAge: 21")
f.write("\nGender: Male")
f.write("\nFaculty: Ethical Hacking")
f.write("\nRoll_Name: 21")
f.close()

f=open("info.txt", "r")
lines=f.readlines()
print(lines[0])
print(lines[1])
print(lines[4])
f.close()