# 1. WAP to enter your name, address, gender, age, faculty and roll_number into a filename "info.txt"
# 2. WAP to display name, address, and faculty from the file "info.txt"

name= input("Enter your name: ")
address= input("Enter your address: ")
age= input("Enter your age: ")
gender= input("Enter your gender: ")
faculty= input("Enter your faculty: ")
roll_number= int(input("Enter your roll number: "))

f=open("info2.txt", "w")

f.write(f"Name: {name}")
f.write(f"\nAddress: {address}")
f.write(f"\nAge: {age}")
f.write(f"\nGender: {gender}")
f.write(f"\nFaculty: {faculty}")
f.write(f"\nRoll_Name: {age}")
f.close()

# f=open("info.txt", "r")
# for line in f:
#     if line.startswith("Name"):
#         print(line,end=" ")
#     elif line.startswith("Address"):
#         print(line,end=" ")
#     elif line.startswith("Faculty"):
#         print(line, end=" ")


f=open("info.txt", "r")
lines=f.readlines()
print(lines[0])
print(lines[1])
print(lines[4])
f.close()
