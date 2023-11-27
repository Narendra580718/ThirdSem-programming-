#Write a meny driven program for the following case:
# 1. hello
# 2. hi
# 3. bye
# 4. welcome
# 5. exit

num= int(input("Enter your option: "))

match num:
    case 1:
        print("Hello")
    case 2:
        print("hi")
    case 3:
        print("Bye")
    case 4 | 6 | 7 | 8:
        print("Welcome")
    case 5:
        print("Exit")
    case _:
        print("Invalid input")
    
exit()