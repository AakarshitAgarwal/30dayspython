import time

# initial =time.time()

# k=0
# while(k<10):
#     print("This is Aakarshit")
#     # time.sleep(2)
#     k+=1
# print("While loop runs in", time.time() - initial,"seconds")

# initial2=time.time()
# for i in range(10):
#     print("This is Aakarshit")
# print("For loop ran in",time.time() - initial2,"seconds")


#print local time 

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
