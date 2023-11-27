# WAP to check whether the entered value is palindrome or not.
#1 2 1

num=int(input("Enter your number: "))
tmp=num
rem=0
reverse=0

while(tmp!=0):
    rem = tmp%10
    tmp = tmp//10
    reverse = reverse *10 + rem

if (reverse==num):
    print("Palindrome number.")

else:
    print("Not Palindrome number.")


#FOR BOTH STRING AND NUMBER:
num1=input("Enter your: ")
rev = num1[::-1]

if(num1==rev):
    print(f"Your {num1} is palindrome.")

else:
    print(f"Your {num1} is not palindrome.")