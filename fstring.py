a = "Aakarshit"
age = 23

#1st way
# print(f"this is me {a} of age {age}")

#2nd way
# print("this is me %s of age %s"%(a,age))

#3rd way
a = "This is me {1} of age {0}"
b = a.format(a,age)
print(b)

