# public -> name as it is
# protected -> _protec = 9 ( Base class and derived class can use that variable )
# private ->  cannot access outside class || name angling 

class Student:
    no_of_leaves = 9
    var = 9
    _protect = 9   # used _ (single underscore)
    __private = 10 # used __ (double underscore)

    def __init__(self, aname , asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"My name is {self.name}. Salary is {self.salary} and role is {self.role}"    

  
stu = Student("harry", 23, "Student")
# print(stu._protect)
# print(stu.__private)   # wrong way to access private variables
print(stu._Student__private)   # name mangling
 