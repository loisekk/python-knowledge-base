# polymorphism  -> compile time ->  method overloading  , Run TIme -> Method Overriding


# methfod overlading 

# class sample:
#     def add(self,  a,b):
#         print(a+b)

#     def add(self, a , b,c):
#         print(a+b+c)

# obj = sample.add(12, 24)



0
0# #method overriding (duck Typing)

# class Parent:
#     def skill (self):
#         print("this is parent class")

#     def skull (self):
#         print("zero civic sence")

# class child:
#     def sill(self):
#         print("THis is child class")

#     def siii(self):
#         print("THis is the idiot ")


# obj = Parent()



# class Bank:
#     def __init__(self , amount , name , pin , address , balance):
#         self.name = name 
#         self.amount = amount
#         self.pin = pin
#         self.__balance = balance

#     def new_amount(self , balance):
#         self.__new_balance = balance
#         print(f"{self.name} , {self.amount} , {self.__balance}")

#     def prev_amount(self , new_amount , amount):
#         self.new_amount = new_amount - amount
#         print(f"{self.new_amount}")
        
# obj = Bank("pnb" , 20000 , 23456 , 4566 , 3434 )
# obj.new_amount(2332)

nums  = [1 ,1 , 1, 2,2,3 , 3, 4 , 4, 3 , 3, 2 , 1,1,5 ]
def occuring(self , nums):
    count = 0
    freq = []
    for i , nums in enumerate(nums):
     if nums not in freq:
        freq.append()
     else :
      nums.remove(i)
    print(f"{i} occur {nums.count} times")
    ount +=1

    return count

print(occuring(nums))
    


# nums = [1,1,1,2,2,2,3,3,3,3]

# nums = int(nums)
# for i in range(len(nums)):
#     pair = nums//2
#     leftover = nums % 10 

    
#     print(leftover)


# num = "aeiouAEIOU"
# count = 0
# for _ in range(len(num)):
#     if num.lower() == 'aeiou':
#         count +=1 
# print(count)

# a = 23
# b = 32

# for i in a , b :
#     if str(a) == str(b):
#         print("palindrone number ")
    


