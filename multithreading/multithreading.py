from threading import Thread
from threading import *
import threading , time
from time import sleep

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)

start = time.perf_counter()

def Hello():
    for i in range(5):
        print("Hello")
        sleep(1)

def Hi():
    for i in range(5):
        print("Hi")
        sleep(1)

# t1 = Hello()
# t2 = Hi()
 
t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=Hi)

t1.start()
t2.start()
t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')

# t1.join()
# t2.join()

# print("Bye")

