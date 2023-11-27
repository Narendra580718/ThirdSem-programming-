num1 = int(input("Enter your number: "))   
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if ( num1>num2 and num1<num3) or (num1>num3 and num1<num2):
    print(f"Your middle number is {num1} ")

elif ( num1<num2 and num2<num3) or (num2>num3 and num2<num1):
    print(f"Your middle number is {num2}")

else:
    print(f"Your middle number is {num3} ")
