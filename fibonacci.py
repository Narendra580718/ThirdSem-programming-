#WAP to print the fibonacci Series upto 10th series.
a=1
b=1
print(a,b, end=" ")
for i in range (1,11,1):
    c=a+b
    a=b
    b=c
    
    print (c, end=" ")

# a=1
# b=1
# for i in range(5):
#     print(a,b,end=" ")
#     a=a+b
#     b=a+b