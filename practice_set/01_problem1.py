# Creating a class "programmer " for storing information of few programmers working at microsoft 

class Programmer :
    company = " Microsoft "
     
    def __init__(self , name , salary , role , pin ):
        self.name = name 
        self.salary = salary 
        self.role = role 
        self.pin = pin 

y = Programmer("Yash ", 4500000 , " as a py dev ", 483001)
print(y.name , y.salary , y.role , y.pin)

h = Programmer(" Harsh ", 4500050 , " as a java  dev ", 345001)
print(h.name , h.salary , h.role , h.pin)

