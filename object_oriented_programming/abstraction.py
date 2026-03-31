#       ABSTRACTION -> meaningfull data dekho or bina kaam k data ko ignore karo
#       alwaya happens in inheritance 

# 1- concrete method -> jinka andar code likha ho 
# 2- abstract method -> jinka andar coder na likha ho  

# protected attribute ,   method overloading , data abstraction ye teeno cheeze python m nai hoti h 


#ABC -> abstract base class 
#abstractmethod ->


from abc import ABC , abstractmethod

class Sharmavishnu(ABC):
    def greet(self):
        print("Welcome to sharmavishnu class")

    @abstractmethod
    def menu(self):
        pass
    
    @abstractmethod
    def details(self):
        pass

class minal(Sharmavishnu):
    def show(self):
        print("THis is minal class")


    def menu(self):
        print("paneer kulche , paneer cheese sandwich")

    def details(self):
        print("details...")

class Areracolony(Sharmavishnu):
    pass

obj = minal()
obj.details()
obj.show()
obj.greet()
obj.menu()


from abc import ABC , abstractmethod

class BankAPP(ABC):
    def database(self):
        print("Database create and accessed...")

    @abstractmethod
    def account(self):
        pass

class WebApp(BankAPP):
    def account(self): # concreate method
        print("Account Accessed..")
    
class MobApp(BankAPP):
    def account(self):
        print("This is account of webapp class ")

obj = WebApp()
obj.database()
obj.account()