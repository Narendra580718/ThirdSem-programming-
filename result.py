# WAP to print the marksheet of a student for the following condition:
# first class(>=70%)
# upper second class (>=60% and <70% )
# lower second class (>=50% and <60% )
# thirsd class (>=40% and <50%)
# fails (<40%)

name= input("Enter your name: ")  
faculty= input("Enter you faculty: ")
your_id= int(input("Enter your student id: "))

english = int(input("Enter your marks for ENGLISH: "))
math = int(input("Enter your marks MATHS: "))
science = int(input("Enter your marks SCIENCE: "))
nepali = int(input("Enter your marks NEPALI: "))

if (english>=40):
    print("PASSED")
else:
    print("FAILED")

if (math>=40):
    print("PASSED")
else:
    print("FAILED")

if (science>=40):
    print("PASSED")
else:
    print("FAILED")

if (nepali>=40):
    print("PASSED")
else:
    print("FAILED")

marks = english+math+science+nepali
total_marks = (marks/400)*100

if (total_marks>=70):
    print("congratulations, you got first division")

elif(total_marks>=60) and (total_marks<70):
    print("Congratulation, you got upper second class.")

elif(total_marks>=50) and (total_marks<60):
    print("Congratulations, you got lower second class.")

elif(total_marks>=40) and (total_marks<50):
    print("Congratulations,You got third class.")

else:
    print("Better luck next time.")