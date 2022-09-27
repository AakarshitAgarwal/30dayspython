class Student:
    counter = 0
    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks
        Student.counter = Student.counter + 1

    @classmethod
    def object_count(cls):
        return cls.counter    

s1 = Student("Sia","93")
s2 = Student("Aakarshit","22")

print(Student.object_count())