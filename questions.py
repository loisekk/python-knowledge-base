''' FUNCTIONS AND RECURISIONS '''

# def addition ():
#     a = int(input("enter first number :-"))
#     b = int(input("enter second number:- "))
#     avg = a+b/2
#     print(avg)
# addition()
# addition()
# addition()
# addition()
# addition()

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
        








# def count(n):
#     if n == 100:
#         return 
#     print(n)
#     count(n+1)
    
# count(1)

# def hello1():
#     hello2()
#     print("hello1")
# def hello2():
#     hello3()
#     print("hello2")
# def hello3():
#     hello4()ddef
#     print("hello3")
# def hello4():
#     hello5()
#     print("hello4")
# def hello5():
   
#     print("hello5")

# hello1()

''' Recursion is when a function calls itself to solve a problem.
It's like asking a smaller version of yourself to do part of the job until it becomes so small and easy that no help is needed.'''

'''
 Factorial (1) =  1
 Factorial (2) =  2 X 1
 Factorial (3) =  3 X 2 X 1
 Factorial (4) =  4 X 3 X 2 X 1
 Factorial (5) =  5 X 4 X 3 X 2 X 1
'''

# def factorial(n):
#     if(n == 1 or n ==0) :
#         return 1 
#     return  n * factorial(n-1)

# n = int(input("Enter the number :" ))
# print( f"The factorial of this number is : {factorial(n)}")

# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)


# def factorial(n):
#     n = int(input("Enter the number :" ))
#     if(n == 1 or n ==0) :
#         return 1 
#     return  n * factorial(n-1)

# print( f"The factorial of this number is : {factorial(n)}")

# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)
# factorial(n)

# def factorial(n):
#     n = int(input("Enter the number: "))
#     def compute(n):


#       if n == 0 or n == 1:
#         return 1 
#     return  n * factorial(n-1)
# print(f"The factorial of this number is: {compute(n)}")

# # Call the function

# factorial()
# factorial()
# factorial()
# factorial()
# factorial()


# def factorial():
#     n = int(input("Enter the number: "))

#     def compute(num):
#         if num == 0 or num == 1:
#             return 1
#         return num * compute(num - 1)

#     print(f"The factorial of this number is: {compute(n)}")

# # Call the function
# factorial()
# factorial()
# factorial()
# factorial()
# factorial()
# factorial()


# Write a program using function to find the greatest of three numbers  
# def greatest(a ,b ,c ):
#    if (a>b and a>c ):
#       return a 
#     #   print( "Greater number is a " )
#    elif (b>a and b>c):
#       return b 
#     #   print( "Greater number is b ")
#    elif (c>a and c>b):
#       return c 
#     #   print( "Greater number is c ")
# a = int(input("Enter the number 1 :" ))
# b = int(input("Enter the number 2 :" ))
# c = int(input("Enter the number 3 :" ))
   
# print(greatest(a ,b ,c ))


# greatest(a ,b ,c )

# write a program using function to convert ferhrenheit to celsius

# def f_to_c(f):
#     return 5*(f-32)/9 

# f = int(input("Enter the temperature in fahrenheit : "))
# c = f_to_c(f)
# print(f"{round(c , 2 )}°c")

# for celsius to ferhrenheit 

# def c_to_f(c):
#     return 9*c/5 + 32
      
# c = int(input("Enter the temperature in celsius : "))
# f = c_to_f(c)
# print(f"{round(f , 2 )}°f")


# How do you prevent a python print() function to print a new line at the end.

# a  = "print"
# b= "gojo"
# c = "goku"
# d = "naruto"
# print(a )
# print(b )
# print(c , end ="" )
# print(d , end ="" ) # end function avoid to take a new a line 
 
 #Write a recursive function to calculate the sum of first n natural numbers.

'''
 sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n ) = 1 + 2 + 3 + 4 + 5 .... (n-1 ) + n 

'''

# def sum(n):
#     if (n==1):
#      return 1 
#     return sum (n-1 ) + n #  return (n-1 ) + n 

    

# print(sum(99)) # if " return (n-1 ) + n " not using sum f^n inside it  then it will  return's only the sum of its previous number 


# def pattern (n):
#     if(n==0):
#      return  
#     print("*" * n )
#     pattern(n-1)    

# pattern(9)

# def multi (n):
#    for i in range (1,11):
#      print(f"{n} X {i} = {n*i}")
# multi(9)


# te = "ABCDEFGHIJ"
# print( te [::-1])

''' fibonacci series '''

# a = 0
# b = 1
# n = int(input(" Enter your series : "))
# for i in range(n):
#  print(a)
#  a,b = b ,a+b


''' for the range of the loops and continue with "n+1 " thenn output must always be 0 '''
# a = 0 
# b = 1
# n = int(input("enter your series : "))
# for i in range (n, n+1):
#  print(a)
#  a,b = b, a+b

''' armstorng number'''

# n = 145
# while n > 0:
#     digits = n % 10 # digits extract 
#     print(digits)
#     n=  n // 10

# n = int(input("enter your number"))
# copy = n
# sum = 0
# while n > 0:
#     digits = n % 10 # digits extract 
#     sum = sum +digits **3 
#     n=  n // 10 # remove digits 
#     print(digits)
# if sum ==copy :
#     print("Armstrong number")
# else :
#     print("Armstrong number")


# n = int(input("enter your number : "))
# copy = n 
# sum = 0 
# while n >0 :
#     digits = n % 10 
#     sum = sum +digits ** 3
#     # print(n)
#     n = n //10 
# if sum == copy :
#     print("Arm Strong number ")
# else:
#     print(" not an armstrong number ")

