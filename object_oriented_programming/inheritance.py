
# inHeritance -> 

# 1. single inheritace
# 2. multiple inheritance
# 3. multilevel in
# 4. hybrid inheritance
# 5. herichiral inheritnace 



class animal :
    def __init__(self , name , age ):
        self.name = name 
        self.age = age
        self.can_walk = True

    def show(self):
        print(f"Name is {self.name} and age is {self.age} or he can walk {self.can_walk}")

class cat(animal):
    # def show2(self): 
    #  print("this is cat class ")

    def __init__(self, name, age , breed):
        super().__init__(name, age)
        self.breed = breed
    
    def sleep(self):
      self.can_walk = False


    def gender(self):
      print(f"Gender of my animal is {self.__gender}")
    
    def show2(self):
        print(f"This is cat class {self.name} and his age is {self.age} , the breed is {self.breed}")       

obj = cat("Rocky" ,3 , "parshion")
obj.show2() 
obj.sleep()
obj.show2()
obj.show() 



# multi level inheritance 
class A :
    def __init__(self , name ):
        self.name = name

    def show(self):
        print("This is parent class")
class B(A):
    def show2(self):
        print("THis is child Class")

class C(B):
    def show3(self):
        print("this is super child class")
obj = C("yash")
obj.show()
obj.show2()
obj.show3()



class A :
    def __init__(self , name ):
        self.name = name

    def show(self):
        print("This is parent class")

class B(A):
    def __init__(self, name , weight):
        super().__init__(name)
        self.weight = weight

    def show2(self):
        print("this is the child class")


class C(B):
    def __init__(self, name, weight , age , gender ):
        super().__init__(name, weight)
        self.age = age 
        self.gender  = gender 

    def show3(self):
        print(f"")



obj = C("gojo" , 23 , 'm' , 56) 
obj.show3()







# Multiple inheritance 


class restaurant:
    def __init__(self):
     print("this is restaurant class (Parent 1)")


class menu:
    def __init__(self):
        print("This is menu class (parent 2 )")

class Customer(restaurant, menu):
    pass

obj = Customer()



class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        val = list[val]
        for val in range(len(nums)):
            if val in nums :
                val_remove = nums.remove
                nums_count = nums.count(nums)
                nums = nums_count
        return nums              
                              
        


class Bank:
    def __init__(self  , name ):
        self.name = name 
    def show(self):
        print(f"THis is bank class {self.name}")

class Account(Bank):
    def __init__(self, name , Account_no):
        Bank().__init__(name)  
        Account().__init__(Account_no)
    
    def show2(self):
        print(f"thii is Account class {self.Account_no}")


class Customer(Account):
    def __init__(self, name, Account_no):
        Account().__init__(self, Account_no)
        Bank().__init__(self, name)
    def show3():
        print(f"This is customer class ")
        
obj = Customer()
obj.show()
obj.show2()

obj.show3()




class papa :
    def skill(sslf):
        print("belt is marna")

class mummy(papa):
    def skill(sslf):
        print(" khana ")

class me(papa , mummy): # mutilevel inheritance 
    def skill(self):
        print('na padhne aur na padhne dena ')

class student (me): # multilevel inheritance 
    def skill (self):
        print('chit banana')


