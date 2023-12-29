#Inaccurate Method
# import time
# s=time.time()
# print("Hello")
# print("Hi Everyone")
# e=time.time()
# print(e-s)

#Using timeit Module
#It gives more accurate result
from timeit import default_timer as timer
start = timer()
print(23*2.3)
end = timer()
print(end-start)