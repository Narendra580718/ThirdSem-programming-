# WAP to do a menu1 driven program
# 1. addition 
# 2. subtraction 
# 3. multiplication 
# 4. division 
# 5. Exit 

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

print("CHOOSE YOUR OPTION: ")

op=int(input("Enter your option from below:\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit \n :"))

match op:
    case 1:
        print(f"Addition {num1 + num2}")
    
    case 2:
        print(f"Subtraction {num1 - num2}")

    case 3:
        print(f"Multiplication {num1 * num2}")
    
    case 4:
        print(f"Division {num1 / num2}")

    case 5:
        print(f"EXITING")
        exit()
    case _:
        print("INVALID OPTION")
