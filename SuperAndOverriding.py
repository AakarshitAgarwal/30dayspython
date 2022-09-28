class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am in class A's constructor, "
        self.classvar1 = "Instance var of class A, "
        self.special = "Special, "

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()    # call a super class constructor
        self.var1 = "I am in class B's constuctor"
        self.classvar1 = "Instance var of class B, "


a = A()
b = B()

print(b.special,b.classvar1, b.var1)
