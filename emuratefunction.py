ll1 = ["Aakarshit","Anurag","Akshat","Utkarsh"]

# i=1
# for item in ll1:
#     if i%2 !=0:   #it wll treat 1st as a 0 index
#         print(f"Odd person in list are {item}")
#     i=i+1    


# by emurate function

for index,item in enumerate(ll1):
    if index%2==0:  #since it will treat 1st as a 1 index
        print(f"Odd person in list are {item}")