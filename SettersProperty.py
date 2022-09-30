class Employee:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname
        # self.email = f"{fname}.{lname}@coder.com"

    def explain(self):
        return f"This is me {self.fname} {self.lname}"
    
    @property
    def email(self):
        return  f"{self.fname}.{self.lname}@coder.com"
    
    @email.setter
    def email(self, string):
        print("Setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
aakararshit_coder = Employee("Aakarshit", "Agarwal")

# print(aakararshit_coder.email())   # use this when property as a decorator is not defined

print(aakararshit_coder.email)

hindustani_supporter.email = "setter.agarwal@coder.com"
print(hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)