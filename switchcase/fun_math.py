def add(num1, num2):
    print(f"Addition {num1 + num2}")

def sub(num1, num2):
    print(f"Subtraction {num1 - num2}")

def multi(num1, num2):
    print(f"Multiplication {num1 * num2}")

def div(num1, num2):
    print(f"Division {num1 / num2}")

num1= int(input("Enter your first number: "))
num2= int(input("Enter your second number: "))

print("CHOOSE YOUR OPTION: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n")

option = int(input("Enter your Option: "))

match option:
    case 1:
        add(num1, num2)

    case 2:
        sub(num1, num2)

    case 3:
        multi(num1, num2)

    case 4:
        div(num1, num2)

    case _:
        print("INVALID OPTION.")











