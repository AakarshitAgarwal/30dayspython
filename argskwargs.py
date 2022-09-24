def funargs(normal,*argsrohan,**kwargs):
    print(normal)
    for item in argsrohan:
        print(item)
    for key,values in kwargs.items():
        print(f"{key} is in {values}")    


har = ["Aakarshit","Rohan","Akshat","Utkarsh"]
normal = "My name is Aakarshit Agarwal"
mydictonary = {"Aakarshit":"DevOps","Akshat":"SDE","Anurag":"Microsoft"}
funargs(normal,*har,**mydictonary)