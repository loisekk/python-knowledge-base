# can we have a set with 18 (int) and '18' (str) as a value in it 
s = set()

s.add(18)
s.add("18")
print(s)
 
 What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s) # becoz py has consider the value as same digits does'nt effect by data type 
print(len(s)) 

s{}
what is the type of 's'?

s = {}
print ( type (s))

# Create an empty dictionary . Allow 4 friends to enter their favourite language as value and use key as their names . Assume that the name are unique 

dict = {}

names = input ( "Enter the person name :")
Lang = input ( "Enter their fav. language :")
dict.update({names: Lang})

names = input ( "Enter the person name :")
Lang = input ( "Enter their fav. language :")
dict.update({names: Lang})

names = input ( "Enter the person name :")
Lang = input ( "Enter their fav. language :")
dict.update({names: Lang})

names = input ( "Enter the person name :")
Lang = input ( "Enter their fav. language :")
dict.update({names: Lang}) # if having a same name person then it will be update from previous 

print(dict)

Can you change the value inside a list which is contained in set S?
 s = {8, 7, 12, "Harry", [1,2]}

 # you can not change list inside a set even you can not make a list inside a set or opposite for list 
 # they are non mutable and non hasble 


 # chapter 6 = Conditional Expression 

 # Write  a program to find a greatest of four numbers entered by the user 

a1 = int(input("Enter the number 1 :" ))
a2 = int(input("Enter the number 2 :" ))
a3 = int(input("Enter the number 3 :" ))
a4 = int(input("Enter the number 4 :" ))

if (a1>a2 and a1>a3 and a1>a4):
    print( "Greater number is a1 ", 1)
     
elif (a2>a1 and a2>a3 and a2>a4): # puting same operator like elif is valid for syntax 
    print( "Greater number is a2 ", 2)
elif (a3>a1 and a3>a2 and a3>a4):
    print( "Greater number is a3 ", 3)
elif (a4>a1 and a4>a2 and a4>a1):
    print( "Greater number is a4 ", 4)


# write a program to find out whether a student has passed or failed if 
#  it requires a total of 40% and atleast 33% in each subject to pass . Assume 3 subjects and take masks as an input from the user .


marks1 = int(input ("Enter subject 1 marks:"))
marks2 = int(input ("Enter subject 2marks:"))
marks3 = int(input ("Enter subject 3 marks:"))

# check for total percentage 
total_percentage = (100*(marks1+marks2+marks3)/300)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("Congratultion You are passed ", total_percentage)

else:
    print("You are failed !  try again next year ",total_percentage)

# A spam comment is defind as a text containing following keywords :
# "mark a lot of money ", "buy now ", "subscribe this ", " click this ", write a program to detect these spams .

p1 = "make a lot of money "
p2 = "buy now "
p3 = "subscribe this "
p4 = " click this "

message = input ( "Enter your message : ")

if((p1 in message ) , (p2 in message), (p3 in message), (p4 in message)):
    print("This is a spam comment !")
else:
    print("This is not a spam comment ")



# write a program to find wheather a given username contains less than 10 character or not .
 
username = input ( " Enter your user name ") 
if(len(username)<=10):
    print("your username should have less than 10 characters ")
else:
    print("your username should have more than 10 characters")


# write a program which finds out wheather a giiven name present in a list or not 

l1 = [ "print", "gojo", "satoru", "goku", "naruto"," harsh"]

name = input("Enter your name :")
if(name  in l1):
    print("Your name is in the list good for you :")
else:
    print("your name is not in the list try other name :")



# write a program to calculate the grades of a student from his marks from the following scheme:
90 100 >Ex
80-90 => A
70-80 => B
60-70 =>C
50-60 => D
<50 => F

marks = int(input("Enter your marks :"))

if (marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50 ):
    grade = "F"
print("your grade is :", grade)

# write a program to find out wheather a given post is talking abt "print" or not .

post = "hey print bro how's you day going "
post = input ("Enter your psot : ")


if ("print".lower() in post.lower()  ):
    print("This post is talking abt print")
else:
    print("This post is not talking abt print ")

'''# loops '''

i = 0
while i<100:
    print("  bankai  ")
    i+=1
    
'''#     # write a program to print the content of list using while  loop '''

l = [ "print", False , 1, 45.46 , "goku", "bleach", "naruto" ]
i = 0 
while (i<len(l)):
    print(l[i])
    i+= 1


'''# for loop '''

l = [ "print", False , 1, 45.46 , "goku", "bleach", "naruto" ]
for i in l:
    print(l)
for i in range(0,100):
        print(i)
