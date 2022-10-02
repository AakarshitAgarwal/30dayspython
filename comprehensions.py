# ls = []

# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# print(ls)

# ls = [i for i in range(100) if i%3==0]
# print(ls)

# Not a SMATER WAY
# dict1 = {0:"item0",1:"items1"}

#SMATER WAY
dict = {i:f"item{i}" for i in range(5,100) if i%3==0}
#reverse Dictonary
dict = { value:key for key,value in dict.items()}
print(dict)