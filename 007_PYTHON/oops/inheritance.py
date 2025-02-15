class Person:
    def __init__(self, fname='default_name', age=9): #create class with constructor
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):     #write a function
        return f'fname={self.fname}, age={self.age}, skills={self.skills}' 
    
    def skill_insertion(self, skill):
        self.skills.append(skill)


class Student(Person):
    pass

s1=Student(22,"Ram")
# s1.skill_insertion("CPP")
print(s1.printing())