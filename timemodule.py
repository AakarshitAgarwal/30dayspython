import time

initial =time.time()

k=0
while(k<10):
    print("This is Aakarshit")
    k+=1
print("While loop runs in", time.time() - initial,"seconds")

initial2=time.time()
for i in range(10):
    print("This is Aakarshit")
print("For loop ran in",time.time() - initial2,"seconds")