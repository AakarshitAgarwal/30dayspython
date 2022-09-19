s = set()

# 1) set made from list

l =[1,2,3,4]
s_from_list = set(l)
# print(type(s_from_list))
# print(s_from_list)


# 2) set made form by iteration

s.add(1)
s.add(2)
print(s)

# s1=s.union({3,4})
s1=s.intersection({2,4})
print(s1)
print(max(s))