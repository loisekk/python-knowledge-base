# def Avg():
#     # Function Defination 
#     a = int(input ("Enter the  number 1 :"))
#     b = int(input ("Enter the  number 2 :"))
#     c = int(input ("Enter the  number 3 :"))

#     average = (a+b+c)/3
#     print(average)


# Avg() # fun call
# Avg() # used  for calling a fun and used at any situation at any line 
# Avg()
# Avg()
# Avg()

''' Write a program to greet a user with "Good day" using functions.'''

# def goodday(name , ending ):
#     print (" good day,  " + name )
#     print ( ending )
#     return "done"

# a=   GoodDay = ("print" , "thank you")
# print(a)

# def GoodDay(name , ending = "thank you "): # for early define that if we forget  to put something then it will run as default  
#     print(f"Good Dayy", name)
#     print(ending) 

# GoodDay("print" , "thankyou")
# GoodDay("gojo" )


# def Greet(name = "print"):
#     print(name)
#     # Function body 

# Greet()# Name will be the "print" in function body (Default)  
# Greet("gojo") # Name will be "gojo" in function body (passed) 


'''  RECURSION  '''

# def palidrone (n):
#     while True :
#         rev = 0 
#         copy = n 
#         while n > 0:
#             rev = rev * 10 + n %10 
#             n = n // 10 
#         if rev == copy :
#             print(f"{copy} is a palidrone number ")
#         else :
#             print(f"{copy} is not palidrone number ")

# palidrone(121)
# palidrone(143)
# palidrone(12123)
 

''' for an palidrone checker of True and false '''
# a = 121
# print(str(a) [::-1] == str(a))



# def primechecker(a):
#     for i in range(2, a):
#         if a % i == 0 :
#             return "Not a prime number "
#     return "prime number  "

# print(primechecker(33))

# def twosum(self , num : list[int] , Target: int):
#     num , Target , self = int(input("Enter the number"))
#     for i in range (len(sum)):
#         for j in range(i+1, len(sum)):
#             if (num[i] +num[j] == Target):
#                 return [i,j]

# twosum()

# def twosum(self , num : list[int], target : int ):
#     for i in range(len(sum)):
#         need = target - num[i]
#         if (need in num  and num.index(need)):
#             return num [i] , num.index(need)

# twosum()






# import random
# computer= random.choice([1, -1 , 0])
# youstr = input("Enter your choice : ")

# youdict = {"r" : 1 , "p" : -1 , "s" : 0} 
# revdict = {1 : "r" , -1 : "p" , 0 : "s"}

# you = youdict[youstr]

# print(f"you chooce {revdict[you]}\n computer chooce {revdict[computer]}\n ")

# if you == computer :
#     print("YOU BOTH CHOOCE SAME DRAW ! ")
# else:
#     if (computer - you ) == -2 or (you - computer) == 1 :
#         print("you won ! ")    
#     else:
#         print("you lose !")



# import random
# computer = random.choice([1, -1 , 0])

# youstr = input("Enter your choice :- ")

# youdict = {"r" : 1 , "p" :-1 , "s" : 0}
# revdict = {1:"r" , -1 :"p" , 0 : "s"}

# you =  youdict[youstr]

# print(f"YOU CHOOSE {you}\n COMPUTER CHOOSE {computer}\n ")

# if computer == you :
#         print(" Both choose the same game must be draw ! ")
    
# else:
#      if computer - you == -2 and computer - you == 1:
#             print("  YOU LOSE BROO 🤦‍♂️ ") 
            
#      else:
#       print("  YOU WIN 😁👍 ")
        



