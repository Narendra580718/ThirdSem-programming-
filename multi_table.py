# WAP to print the multiplication table of 5
# WAP to print the multiplication form 1 to 10 upto 10 multiples
# WAP to find the factorial of given number.

def multi():
    for i in range (1,11,1):
        print(f"5*{i} = {5*i}")

def multiplication():
    for i in range (11):
        for j in range (11):
            print(f"{i}*{j} = {i*j}")

def factorial():
    a = int(input("Enter your number: "))
    factorial = 1

    for i in range (a,1,-1):
        factorial=factorial*i
    
    print(f"Factorial of you number {a} is {factorial}.")

def conti():
    print("\nDo you want to continue: \n")
    b=int(input("1. Yes \n2. No \n: "))

    match b:
        case 1:
            menu()

        case 2:
            exit()

        case 3:
            print("ERROR")

def menu():
    print("Enter your option: \n1. Multiplication table of 5 \n2. Multiplication table from 1 to 10 \n3. The factorial of your number")
    menu=int(input("Enter your choice: "))


    match menu:
        case 1:
            multi()
            conti()

        case 2:
            multiplication()
            conti()
        
        case 3:
            factorial()
            conti()

        case _:
            print("ERROR")

menu()