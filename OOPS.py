# class Students:
#     no_of_leaves = 8
#     pass

# harry = Students()                                                        |
# larry = Students()                                                        |                __init__
#                                                                           |                                                                                     
# harry.name = "Harry"                                                      |
# larry.names = ["Aakarshit","Anurag","Utkarsh"]                            |
# harry.std = 3                                                             |    


# print(Students.no_of_leaves)
# print(Students.__dict__)

# larry.no_of_leaves = 10
# print(larry.no_of_leaves)


class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry",256,"Instructor")

harry.change_leaves(34)

print(harry.no_of_leaves)

# rohan = Employee()  # rohan is the instance over here of class Employee

# print(rohan.printdetails())