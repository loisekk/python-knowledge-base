class Employee : 
      language = "py" # This is an class attributes 
      salary = 1000000

      def __init__(self , name , salary , language):
           self.name = name 
           self.salary = salary
           self.language = language
           print(" I'm creating this object ") # dunder method  which is  automatically called 

      def getinfo(self): 
        print(f" The language is {self.language } and salary is {self.salary }")



      @staticmethod 
      def greet ():   
          print("yokoso")

yash = Employee ("yash", 1300000, "JAVASCRIPT")
# yash.name = "yash"
print(yash.name , yash.salary , yash.language)