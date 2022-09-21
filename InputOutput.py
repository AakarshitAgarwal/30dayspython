from turtle import rt


# f =open("sample.txt","rt")
# print(f.readlines())
# print(f.readlines())
# print(f.readlines())

f = open("sample.txt","rt")


# content = f.read()
for line in f:
    print(line)


# print(content)

# content = f.read(3)
# print(content)

f.close()