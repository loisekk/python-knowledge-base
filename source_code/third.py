i = [ 1,2,3,4,5]

for item in i :
        print(item)
else:
        print("done") # This is printed when the loop is exhausts !

for i in range (100):
        if(i == 34):
         break #  Exit the loop right now 
        print(i)

for i in range (100):
        if(i == 34):
          continue # Skip this itration (only skiping that perticular value )
        print(i)

for i in range(955):
     pass # Without pass , the program will throw an error


''' while loops '''



i = 10    # '''Initilization'''
while(i<=10): #'''condition'''
     print(i)
     i-= 1  #'''Increment'''
     break

n = 153
copy = n
sum = 0
while n > 0  :
    digit =  n % 10 
    power = digit ** 3 
    sum = sum + digit ** 3 
    n = n // 10
    print("armstrong number" ) if copy == sum else print( " not an amrstrong nunber")



'''write a program to print multiplication tabel of a given number using for loop .'''

n = int( input ( "Enter the number :"))

for i in range (1 , 101):
    print(f"{n} X {i} = {n*i}")  # using f 'str' for using variables inside the function 

''' another way '''
n = int( input ( "Enter the number :"))
for i in range (n,(n*10)+1,n):
    print(i)    

 Write a program to greet all the person names stored in a list 'l' and which starts.
 with S.


l =["Awasthi", "Soham", "Sachin", "harsh"]

for name in l : # before printing if having a statement needs then it use with 'if'
  if(name.startswith("S")):
    print(f"hello {name}")
  
'''       # write a program to print multiplication tabel of a given number using for loop  " using while loop  ".'''

n = int( input ( "Enter the number :"))

i =0
while (i<101):
  
    print(f"{n} X {i} = {n*i}")
    i+= 1 


'''    # write a program to find whether a given number is prime or not .'''

n = int( input ( "Enter the number :"))

for i in range(2,n):
    if(n%i) ==0:
        print("Given number is not prime ")
        break 
else:
    print("Given number is prime ")

'''# Write a program to find the sum of first n natural numbers using while loop.'''

n = int(input ("Enter the number :"))
i = 1
sum1 = 0
sum2 = 0
while (i<=n):
    if (i%2==0):-
       sum1 +=i
       i+=1  
    else:
        sum2 +=i
        i+=1

print(sum1,sum2)
        
''' for printing the factorial problem '''

a = int(input("tell your factorial number :-"))
fact = 1
for i in range (1 , a+1):
    fact = fact*i
print(fact)

''' for chechking the divisibility for number '''

a = int(input(" starting range  :-"))
n = int(input("tell your factorial number :-"))

for i in range (1,a+1):
    if i %3 == 0 and i %5 == 0 :
        print(i)


n = int(input("tell your  number :-"))
for i in range (1 ,n+1):
    if n % i == 0 :
        print(i)

''' in a factorial state at end sum of that factorial number '''

n = int(input("tell your  number :-"))
sum = 0
for i in range (1 ,n+1):
    if n % i == 0 :
        sum = sum + i
print(sum)

i = 1 
while i <= 10:
    print(i)
    i += 1

i = 10
while i >=1:
    print(i)
    i -= 1
    break


while True :
    n = int(input(" give the number "))
    print(n)
    if n == 0 :
       print(f"{n}")
       break 

''' you have to take input untill you found a 
number which is divisible by both 3 and 5 '''

while True :
 n = int(input(" give the number "))
 if n % 3 ==0 and n % 5 == 0 :
    print(f" found it {n} is required number ")
    break
