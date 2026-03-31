# n  = int(input("tell your product amount :-"))

# if n >5000 :
#     print("you got 25% discount ")

# elif n >= 3000 or n <= 5000:
#     print("you got 15 % discount")
# elif n >= 1000 or n <=3000 :
#     print("you got 10% discount")
# else:
#     print("there is no discount")


''' take three as in input representing triangle'''

# a = int(input("tell your first side's for triangle :-"))
# b = int(input("tell your second side's for triangle :-"))d
# c = int(input("tell your third side's for triangle :-"))

# if a== b or b ==c or a==c :
#     print("Equilateral Triangle")

# elif a==b or b ==c or a ==c :
#     print("Isoscaler Triangle")

# elif a==b or b==c or a==c :
#     print("Scalene Triangle")


# n = int(input("tell your number:-"))

# for i in range(1,n+1):
#     if i % 2 == 0  :
#      print(i)
#     elif(i % 2 != 0):
#      print(i) nbvn


''' URL = UNIFORM RESOURCE LOCATOR ''' 
 # http:// = SCHEME 
 # https:// = with lock 
 # www.gcflearnfree.org = DOMAIN NAME 
 # www. = SUB DOMAIN
 # .com = TOP_LEVEL DOMAIN 
 # www.quickcostumes.com/'''popular/burrito''' = FILE PATH 
 # en.wikipedia.org/w/index.php?'''title=Burrito'''#Breakfast_Burito = PARAMETER STRING
 # en.wikipedia.org/w/index.php?title=Burrito#'''Breakfast_Burito''' = ANCHOR
 


# n = int(input("tell your number:-"))
# for i in range (1,n):
#   if i > 1 or n % i ==0:
#     print(f" its a prime number and it's divisor number  is {n}")
#     break

#   else:
#     print("not a prime number")
#     break

# n = int(input("enter a number :-"))

# factor = 0
# for i in range (1,n+1):
#   if n %i == 0 :
#     factor +=1
    
#   if factor >2 :
#     print("Not a prime number ")
#     break
#   else:
#     print("prime number ")
#     break

n = int(input("Enter a prime :-"))
factor = 0 
for i in range(2,n):
  if n %i ==0:
    print("not prime number ")
    break
  else:
    print("prime")
    break
  