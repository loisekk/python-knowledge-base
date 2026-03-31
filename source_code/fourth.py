''' HCF '''

''' you have to find hcf for and 2 input number '''

n1 = int(input(" enter your first number "))
n2 = int(input(" enter your first number "))

smaller = 0 # for finding at first the smaller value to find hcf 
if n1 >n2 : # must be value if n1 and n2 are smaller 
    smaller = n1
else : # to store the value in container 
    smaller = n2 

hcf = 1 # put 1 becoz - is also 1
for i in range(1,smaller+1):
    if n1 % i == 0 and n2 % i == 0 :
        hcf = i # putting i hcf at the end 
print(hcf)

n1 = int(input(" enter your first number "))
n2 = int(input(" enter your first number "))

smaller = 0 # for finding at first the smaller value to find hcf 
if n1 >n2 : # must be value if n1 and n2 are smaller 
    smaller = n1
else : # to store the value in container 
    smaller = n2 

hcf = 1 # put 1 becoz - is also 1
for i in range(smaller , 0 , -1):
    if n1 % i == 0 and n2 % i == 0 :
        hcf = i # putting i hcf at the end 
        break
print(hcf)

''' using while loops for finding hcf'''

while True :
    n1 = int(input(" enter your first number "))
    n2 = int(input(" enter your first number "))
    num = 1
    hcf = 1
    if n1>n2  and n1 % num == 0 :
        smaller = n1    
    elif n2 >n1  and n2 % num == 0:
        smaller = n2 
    elif n1 % num  != 0 and n2 % num != 0 :
        hcf = num 
        break
    hcf = num  
    print(hcf)

''' lOWEST COMMON FACTOR '''

n1 = int(input(" enter your first number "))
n2 = int(input(" enter your first number "))

smaller = 0 
hcf = 1 # put 1 becoz - is also 1
for i in range(smaller , 1, -1):
    if n1 % i == 0 and n2 % i == 0 :
        hcf = i
        break 
print(hcf)

'''  using loops printing even and odd statement '''

n = int(input ("Enter the number :"))
even_sum = 0
odd_sum = 0
for i in range (1,n+1):
    if i%2 == 0:s
     even_sum = even_sum +1
    else:
     odd_sum = odd_sum +1

print(f"your even sum is {even_sum}\n your odd sum is {odd_sum}")

'''# Write a program to calculate the factorial of a given number using for loop'''

n = int(input ("Enter the number :"))
product = 1    # if we intilize in add or sum then it itilize by "0" and in multiplication or product it itilize by "1"
for i in range(1,n+1):
    product = product* i
print(f"The factorial of {n} is {product}")

'''# Write a program to print the following star pattern
# *
# ***
# ***** for n=3'''

n = int(input ("Enter the number : "))
for i in range (1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end ="")
    print("") # it added by default new line that's why we are not using "\n "    

    Write a program to print the following star pattern:

for n=3

*****
***
*
n = int(input ("Enter the number : "))
for i in range (1, n+1):
    print("*"* i, end ="")
    print("") 

'''
 ***
 * *  n =3 
 ***
'''

n = int(input ("Enter the number : "))
for i in range (1, n+1):
     if (i == 1 or i == n ): # for rectangular or square like this is for first and last line 
           print("*"* n, end ="") # only true for first and last condition 
     else:  # middle values 
           print("*", end="") # for 2nd row first star 
           print(" "*(n-2) , end="") # 2nd row of space b/w stars
           print("*", end="") # for 2nd row last star
     print("")

Write a program to print multiplication table of n using for loops in reversed order.


n = int( input ( "Enter the number :"))

for i in range (1 , 101):
    print(f"{n} X {101- i} = {n*(101-i)}") 


''' FUNCTIONS AND RECURISIONS '''

def addition ():
    a = int(input("enter first number :-"))
    b = int(input("enter second number:- "))
    avg = a+b/2
    print(avg)
addition()
addition()
addition()
addition()
addition()
