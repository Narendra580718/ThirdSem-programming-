num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 <= num2 and num1 <= num3:
    print(f"{num1} is smallest amoung 3 numbers.")
elif num2 <= num1 and num2 <=num3:
    print(f"{num2} is smallest amoung 3 numbers.")
else:
    print(f"{num3} is smallest amoung 3 numbers.")