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


karan = Employee.from_dash("Karan-420-Student") 


# print(karan.salary)
karan.printgood("Aakarshit")