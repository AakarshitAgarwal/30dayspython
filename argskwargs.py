def funargs(normal,*argsrohan):
    print(normal)
    for item in argsrohan:
        print(item)

har = ["Aakarshit","Rohan","Akshat","Utkarsh"]
normal = "My name is Aakarshit Agarwal"
funargs(normal,*har)