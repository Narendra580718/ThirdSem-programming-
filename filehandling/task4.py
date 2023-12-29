#WAP to enter your name, address, gender, age, faculty, and roll_number of 3 students into a file and display all  records from the file.

count = 0

while count < 3:
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    age=input("Enter your age: ")
    faculty=input("Enter your faculty: ")
    roll_number=input("Enter your roll number: ")
    print("\nANOTHER STUDENT")

    f=open("threestudent.txt", "a")

    f.write(f"\nName: {name}")
    f.write(f"\nAddress: {address}")
    f.write(f"\nAge: {age}")
    f.write(f"\nFaculty: {faculty}")
    f.write(f"\nRoll.Number: {roll_number}")

    count+=1
f=open("threestudent.txt","r")
f.read()
f.close