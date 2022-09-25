# numbers = ["21","54","32"]

# map -> it return in the form of objects and it helps to typecast elements in list in any form
# print(map(int, numbers))
# numbers = list(map(int, numbers))
# print(numbers[2])

#code to return square of elements

# def sq(a):
#     return a*a

# num=[2,4,6,7,8]
# sqaure = list(map(sq,num))
# print(sqaure)

#code to return square of elements with lambda function

# num=[5,7,3]
# square = list(map(lambda x: x*x,num))
# print(square)


# -----------------FILTER----------------

# NUM = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5

# grt_5 = list(filter(is_greater_5,NUM))
# print(grt_5)



# ---------------- REDUCE ----------------
from functools import reduce
l = [1,2,3,4,5]
sum = reduce( lambda x,y:x+y, l)
print(sum)