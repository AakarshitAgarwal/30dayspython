d1 = {}

d2 = {"Aakarshit" : "Chicken" , "Harivansh" : "Dimaag" , "Mayank" : "Protein", "xyz" : {"A":"Maggie" , "B":"junk Food", "C":"Roti"}}

# print(d2["xyz"]["A"])  # access nested dictonary
# print(d2["xyz"])

# d2[420] = "Cyware"
# print(d2)
# del d2[420]
# print(d2)


# non copy function

# d3 =d2
# del d3["Aakarshit"]
# print(d2)
# print(d3)

# d3 = d2.copy()

# del d3["Aakarshit"]

# print(d3)

# print(d2.items())   # return key value pairs

# d2.update({"Shanu" : "Coffee"})
# print(d2)
# print(d2.keys())    # return keys of dictionary

print(d2.get("Aakarshit"))
