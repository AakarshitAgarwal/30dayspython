class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def from_dash(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good "+string)


class Programmer(Employee):
    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role} and the languages are {self.languages}"

karan = Employee.from_dash("Karan-420-Student") 


harry = Employee("Harry",255,"Instructor")
rohan = Employee("Rohan",455,"Student")


shubham = Programmer("Shubham",555,"Programmer",["python"])
# print(Programmer.printprog(shubham))

print(shubham.printprog())

# print(karan.salary)
# karan.printgood("Aakarshit")