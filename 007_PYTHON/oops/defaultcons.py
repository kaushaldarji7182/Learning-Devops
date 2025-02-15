class Person:
    def __init__(self, fname='Kaushal', lname='Darji', age=22):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.skills = []  
    def printing(self):
        return f'fname={self.fname}, lname={self.lname}, age={self.age}, skills={", ".join(self.skills)}'

    def skill(self, skill):
        self.skills.append(skill)  

p = Person()
p.skill("Python")


print(p.printing()) 