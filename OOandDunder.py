class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


    def __add__(self,other):
        return f"{self.salary}+{other.salary}"

    def __truediv__(self, other):
        return self.salary / other.salary

    def __len__(self):
        return len(self.name)

    

emp1 = Employee("Aakarshit" , 500, "Programmer")
emp2 = Employee("Shanu" , 10, "Coder")

# print (emp1 + emp2)
# print(len(emp1))
print(emp1 / emp2)
