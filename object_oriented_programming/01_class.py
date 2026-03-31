class Employee :
      language = "py" # This is an class attributes 
      salary = 1000000

yash = Employee ()
yash.name  = "yash" # This is an object / INSTANCE  attributes
print( yash.name , yash.language, yash.salary )

harsh = Employee()
harsh.name =  "Harsh of harsh "
print( harsh.name  ,  harsh.salary , harsh.language )

# Here name is the  object / INSTANCE attributes and language and salary is the class attributes 
# as they directly bleongs to the class 


class Delta:
      a = 95 # attributes

      def show(self): # method
            print("he;\lo")


game =Delta() # object 

game.show() # calling through object 
print(game.a) # method


class time:
      a = 12
      def play_time(self):
            print("gmaing_time")

gaming = time()
gaming.play_time()


# # Object oriented approach
# ''' Class - blueprint 
#     Object - instance of class'''

# # class jab tak create nahi hogi jab tak object create na hojaye
# # jis class ka object hoga usi class  ka attribute aur method access kr  payenge 

class SharmaVishnu:
    a = 10       # attribute (class k andar variable nahi bolte h isko attributes bolte h )

    def show(self):        # Method     (In class there is not a function it is called methods)
        print("XYZ") 


mp_nagar = SharmaVishnu()   # here mp_nagar is called an object 
#bracet use tab karege jab object create karege 
mp_nagar.show()
print(mp_nagar.a)

indrapuri = SharmaVishnu()
indrapuri.show()
print(indrapuri.a) 

# # object parameter bankar methods k pass jata h or check karta h 
# #ek class m multiple object create kar sakte


# ------------constructor----------------------
# Ak class me ak se jayeda constructor ho sakta hai par chalegi latest constructor

class SharmaVishnu:

    def _init_(self,waiter,tables,chairs):
        self.waiter = waiter   #Instance Attributes
        self.tables = tables
        self.chairs = chairs
        print("constuctors functions are called")

    def show(self):   # Instance Method
        print(f"Waiter name is {self.waiter}")
        print(f"No.  of tables {self.tables}")
        print(f"no. of chairs {self.chairs}")

indripuri = SharmaVishnu("Nathulal",20,30)
indripuri.show()






class Information:
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"my name is {self.name}")
        print(f"your age is {self.age}")

obj = Information("Ravish kumar",19)
obj.show()


class Bank:
    def _init_(self,balance):
        self.balance = balance
        print(f"The balance is {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"updated amount is {self.balance}")

obj = Bank(5000)
obj.deposit(2000)


class RajHans:
    def _init_(self,name):
        self.name = name

    def _str_(self):   # jab object ya class ka address/location show na krna ho
        print(self.name)

obj = RajHans("Bagadbilla")
obj._str_()



class Student:
    college = "Oriental"

    @classmethod   # Decorators
    def college_change(cls,new_name):
        cls.college = new_name
        print(f"college is {new_name}")

stud1 = Student()
print(stud1.college)
stud1.college_change("LNCT")

class sharmavishnu:
    def __init__(self , waiter):
         self.waiter = waiter 

    def show(self):
        name = "om" 
        
ob1 = sharmavishnu("sumit")
ob1.show()
# sharmavishnu.show()
print(f"the waiter {ob1.name}")

     
class sharmavishnu:
    def __init__(self , waiter):
          self.waiter = waiter 



    @staticmethod  # -> these are the independent of object 
    def show(waiter):
         print()



class sharmavishnu:
    def __init__(self  , price , dish ):
        self.dish = dish 
        self.price = price 
        self.__revenue = 30000

    def show(self):
         print(f" Dish is {self.dish}")
         print(f" price is {self.price}")
         print(f" Revenue is {self.__revenue}")


satoru = sharmavishnu('paneer kulche , 3+ kulche' , 180)
satoru.show()



class bank:
    def __init__(self , name , age , address):
          self.name = name
          self.age = age
          self.address = address
          self.__balance = 50000

    def change(self , new):
         self.__balance = new
    @property.setter
    def show(self):
         print(f"your name {self.name}")
         print(f"your age {self.age}")
         print(f"your address {self.address}")
         print(f"your balance {self.__balance}")

        

yash = bank("yash" , 18 , "ward no. 11")
yash.change(50000)
yash.show()

