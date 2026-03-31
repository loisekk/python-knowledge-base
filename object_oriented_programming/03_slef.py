class Employee : 
      language = "py" # This is an class attributes 
      salary = 1000000

      def getinfo(self): # if giving an arguments were accepts by self operator using like this " def getinfo(slef )"
        print(f" The language is {self.language } and salary is {self.salary }")


  # for defining an whole object to an yokoso fn so that using it as static function 

      @staticmethod # decorator to mark it as a static method
      def greet ():    #  def greet (self):  # 'it work as self call 
          print("yokoso")

yash = Employee ()
yash.language   = "javascript " # This is an object / INSTANCE  attributes

yash.greet()
yash.getinfo() # Employee.getinfo() takes 0 positional arguments but 1 was given
# it automatically convert's into this 
Employee.getinfo(yash) # work as previus only syntax diff 
