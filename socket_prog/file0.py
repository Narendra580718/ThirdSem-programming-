import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET==IPv4, SOCK_STREAM==tcp
ip= "10.1.1.254"
port=80
print(ip)
s.connect((ip,80))
print("Connection Successful")

# ip=socket.gethostbyname("www.google.com")
# # print(ip)
# port=80
# s.connect((ip,port))
# print("Connection Successful")