# # f =open("sample.txt","rt")
# # print(f.readlines())
# # print(f.readlines())
# # print(f.readlines())

# f = open("sample.txt","rt")


# # content = f.read()
# for line in f:
#     print(line)


# # print(content)

# # content = f.read(3)
# # print(content)

# f.close()


# #write mode
# f=open("sample.txt","w")

# f.write("Aakarshit is trying hands on python")
# f.close

#append mode
f=open("sample.txt","a")

a =  f.write("Aakarshit is trying hands on python")
print(a)
f.close
