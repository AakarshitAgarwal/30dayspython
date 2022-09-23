l = 10

def function(n):
    global l   # have to intialize the local variable with a key to get it used in the function
    m=8
    l=l+45
    print(l,m)

function(5)    
