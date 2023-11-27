# Write a menu driven program using function for the following:
#     WAP to calculate smaller between two number     
#     WAP to calculate greatest amony any three number
#     WAP to print the middle number among three numbers.
#     WAP to print the following series:
#         5 10 15 20 ....so on upto tenth terms.
#     WAP to print the odd numbers from 100 to 20.

# and also ask the user to continue the menu

def small():
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))

    if num1<num2 or num1<=num2:
        print(f"Number 1 = {num1} is lesser than Number 2 = {num2}")

    else:
        print(f"Number 2 = {num2} is smaller. ")

def great():
    num1=int(input("Enter your first number: ")) #30
    num2=int(input("Enter your second number: ")) #10
    num3=int(input("Enter your third number: ")) #20

    if (num1>num2 and num1>num3):
        print(f"{num1} is greatest among all three number.")

    elif (num2>num1 and num2>num3):
        print(f"{num2} is greates among all three numbers.")

    else:
        print(f"{num3} is greatest among all three numbers.")

def middle():
    num1=int(input("Enter your first number: ")) #20
    num2=int(input("Enter your second number: ")) #10
    num3=int(input("Enter your third number: ")) #30

    if (num1<num3 and num1>num2) or (num1<num2 and num1>num3):
        print(f"{num1} is your middle number.")

    elif (num2<num3 and num2>num1) or (num2>num3 and num2<num1):
        print(f"{num2} is your middle number.")

    else:
        print(f"{num3} is your middle number.")

def thenth():
    for i in range (1,50,5):
        print(i, end=" ")

def odd():
    print(f"These numbers are odd numbers.")
    for i in range (100,20,-1):
        if (i%2!=0):
            print(i, end=" ")
    

def conti():
    cont= int(input("\nDO YOU WNAT TO CONTINUE: \n1. Yes \n2.No\n : \n"))
    
    match cont:
        case 1:
            menu()

        case 2:
            exit()

        case _:
            print("ERROR")


def menu():
    menu=int(input("CHOOSE YOUR OPTION:\n1. Calculate smaller between two number \n2. Calculate greatest amony any three number \n3. Print the middle number among three numbers. \n4. Print the following series: 5 10 15 20 ....so on upto tenth terms. \n5. Print the odd numbers from 100 to 20. \n6. Exit \n:"))

    match menu:
        case 1:
            small()
            conti()

        case 2:
            great()
            conti()
        
        case 3:
            middle()
            conti()
        
        case 4:
            thenth()
            conti()

        case 5:
            odd()
            conti()

        case 6:
            exit()

        case _:
            print("ERROR")
menu()






        

    