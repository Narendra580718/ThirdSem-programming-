#WAP to print Armstong number.

number=int(input("Enter your number: "))

tmp=number
rem=0
check=0
while (tmp!=0):
    rem=tmp%10
    check=check+rem**3
    tmp=tmp//10

if (number==check):
    print("Armstrong Number.")

else:
    print("No")
