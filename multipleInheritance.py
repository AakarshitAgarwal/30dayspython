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

class Player:
    var = 9
    no_of_games = 11
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name} .Game is {self.game}"

class CoolProgrammer(Employee, Player):
    var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 122, "Instructor")
rohan = Employee("Rohan", 455, "Student")

# shubham = Player("Shubham", ["Cricket"])
karan  = CoolProgrammer("Karan",433,"Coolprogrammer")
# det = karan.printdetails()
karan.printlanguage()
# print(det)

# print(karan.var)