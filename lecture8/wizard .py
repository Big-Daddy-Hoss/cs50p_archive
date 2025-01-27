class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.name = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")