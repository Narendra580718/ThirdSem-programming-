#Write a meny driven program for the following case:
# 1. hello
# 2. hi
# 3. bye
# 4. welcome
# 5. exit


def first():
    print("Hello")

def second():
    print("hi")

def third ():
    print("bye")

a=int(input("Enter your choice: "))

match a:
    case 1:
        first()
    
    case 2:
        second()

    case 3:
        third()

    case _:
        print("INVALID OPTION")