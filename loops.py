list1 = [["Harry",1],["Larry",2],["Carry",6],["Marry",250]]

dict1 = dict(list1)
print(dict1)

#how to iterate within list

# for items,lollipop in list1:
#     print(items, " eats lollypop with values ",lollipop)

#how to iterate within dictonary

# for items , lollipop in dict1.items(): 
#     print(items, "eats lollypop with values ",lollipop)


items = [int, float, "Harry" ,5,3,4,7,34,5,676,434,24,9]

for item in items:
    if str(item).isnumeric() and item>8:
        print(item)