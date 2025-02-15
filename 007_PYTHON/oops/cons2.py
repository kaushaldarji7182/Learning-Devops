class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def printing(self):
        return f'fname={self.fname}, lname={self.lname}, age={self.age}'

p = Person("Kaushal", "Darji", 22)


print(p.printing())  
