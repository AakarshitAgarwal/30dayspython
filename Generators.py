"""
#   Iterable -> __iter__() or __getitem__()
#   Iterator -> __next__() #used on those functon which are iterable
#   Iteration -> 
# 
#   GENERATORS -> functon that can we iterate once used to save RAM (Sone ka anda dene wali murgi) / Iterators that can be used once
#   yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
for i in g:
    print(i)