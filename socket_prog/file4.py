# import socket

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# IP = input("Please enter your IP Address : ")
# Port = int(input("Please enter your port: "))

# result=s.connect_ex((IP,Port))

# if(result==0):
#     print("port {} is open".format(Port))

# else:
#     print("port {} is closed".format(Port))

#WITH RANGE 
# import socket

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# IP = input("Please enter your IP Address : ")
# port_one = int(input("Please enter your port range: "))
# port_two = int(input("Please enter your second range: "))

# for port in range (port_one,port_two+1,1):

#     result=s.connect_ex((IP,port))

#     if(port==0):
#         print("Port {} is open".format(port))

#     else:
#         print("Port {} is closed".format(port))

#WITH RANGE & WITH '-'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input("Please enter host name: ")
port = input("Please enter your port with range: ")

port1,port2 = port.split('-')
port1=int(port1)
port2=int(port2)

for port in range(port1,port2+1,1):
    host=socket.gethostbyname(ip)
    result=s.connect_ex((host,port))
    if (result==0):
        print("Port {} is open.".format(port))

    else:
        print("Port {} is closed.".format(port))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ip=input("Please enter the  IP you want to scan: ")
# print("PORTS=0-65535")

# ports=input("Enter the ports you want to scan(seperate them using ','): ")
# port_list= list(ports.split(','))

# for i in port_list:
#     port=int(i)
#     result=s.connect_ex((ip,port))

#     if(port==0):
#         print("Port {} is open".format(port))

#     else:
#         print("Port {} is close".format(port))

