# write a Menu Drive program for the following:
# 1. scannning single port only
# 2. scannning range of ports.
# 3. scannning Selected ports
# 4. scannning
#         system or well-known ports: form 0 to 1023
#         user or registered prots: from 1024 to 49151
#         dynamic or private ports: 49192 to 65535
# 5. scannning all ports
# 6.Exit

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def singleport():
    IP=input("Please enter the IP address: ")
    port=int(input("Please enter the port you want to scan: "))

    result=s.connect_ex((IP,port))
    if(result==0):
        print("Port{} is open".format(port))
    else:
        print("Port {} is closed".format(port))

def rangeport():
    ip = input("Please enter the IP you want to scan: ")
    port = input("Please enter your port with range using '-' in between: ")

    port1,port2 = port.split('-')
    port1=int(port1)
    port2=int(port2)

    for port in range(port1,port2+1,1):
        result=s.connect_ex((ip,port))
        if (result==0):
            print("Port {} is open.".format(port))

        else:
            print("Port {} is closed.".format(port))

def seletedport():
    ip=input("Please enter the  IP you want to scan: ")
    print("PORTS=0-65535")

    ports=input("Enter the ports you want to scan(seperate them using ','): ")
    port_list= list(ports.split(','))

    for i in port_list:
        port=int(i)
        result=s.connect_ex((ip,port))

        if(port==0):
            print("Port {} is open".format(port))

        else:
            print("Port {} is close".format(port))

def options():
    ip=input("Please enter the IP you want to scan: ")
    
    print("Please choose an option from below:")
    print("\n1. System or well-known ports: 0-1023")
    print("\n2. User or registered ports: 1024-49151")
    print("\n3. Dynamic or private ports: 49192-65535")
    user_choice=int(input("\nEnter your choice="))

    match user_choice:
        case 1:
            for i in range(0,1023+1,1):
                result=s.connect_ex((ip,i))
                if (result==0):
                    print("Port {} is open.".format(i))
                else:
                    print("Port {} is closed.".format(i))

        case 2:
            for i in range (1024,49151+1,1):
                result=s.connect_ex((ip,i))
                if (result==0):
                    print("Port {} is open.".format(i))
                else:
                    print("Port {} is closed.".format(i))
        
        case 3:
            for i in range (49151,65525+1,1):
                result=s.connect_ex((ip,i))
                if (result==0):
                    print("Port {} is open.".format(i))
                else:
                    print("Port {} is closed.".format(i))

def all_port():
    ip=input("Please enter the IP you want to scan: ")
    
    for i in range (0,65535+1,1):
        result=s.connect_ex((ip,i))

        if result==0:
            print("Port {} is open.".format(i))
        
        else:
            print("Port {} is closed.".format(i))

def conti():
    cont=input("\nDo you want to conitnue (yes/no): ")
    if cont=="no":
        exit()
    elif cont!="no" and cont!="yes":
        print("INVALID OPTION")
        print("PLEASE TRY AGAIN\n")
        conti()
    else:
        scan_port()

#STARTING POINT OF MENU
def scan_port():
    print("Port Scanner:")
    print("\n1. Scannning single port only")
    print("2. Scannning range of ports.")
    print("3. Scannning Selected ports")
    print("4. Scannning options:")
    print("5. Scannning all ports ")
    print("6. Exit")
    choice=int(input("\nSelect your options: "))

    match choice:
        case 1:
            singleport()
            conti()

        case 2:
            rangeport()
            conti()
        
        case 3:
            seletedport()
            conti()
        
        case 4:
            options()
            conti()

        case 5:
            all_port()
            conti

        case 6:
            exit()

scan_port()