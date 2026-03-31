import os
import numpy as np
# import pyttsx3
# engine = pyttsx3.init()


# print("Numnber a is :", a)
# print("Numnber b is :", b)
# print("sum of a and b is ", a+b)

# # --- NumPy Arithmetic Example ---
# # Create two NumPy arrays
# array1 = np.array([1, 2, 3, 4])
# array2 = np.array([10, 20, 30, 40])

# # Add the arrays element-wise
# sum_array = array1 + array2

# print("--- NumPy Example ---")
# print(f"Array 1: {array1}")
# print(f"Array 2: {array2}")
# print(f"Sum of arrays: {sum_array}")



# path = "/New folder"  # use your desired path
# try:
#     entries = os.listdir(path)
#     print("Contents of directory:", entries)
# except FileNotFoundError:
#     print(f"Error: Directory '{path}' not found.")
# except PermissionError:
#     print(f"Error: Permission denied to access '{path}'.")
# except OSError as e: 
#     print("OS error:", e)




# a =  int(input("Enter the number of finding the type :")
# print(type(a))

# a = int(input("Enter the number 1 :")
# b = int(input("Enter the number 2 :")

# print("a is greter than b ", a>b)

# a = int(int(input("Enter the number :"))
# print("The square of the no is",a**2)


# here  = "print "
# nameshort = here  [0:2]
# print (nameshort)
# character1 = here [1]
# print(character1)

# here  = "printhhh"
# print here  [0:2])
# print here  [2:3])
# print here  [0:4]) # IF st start ie none then 0 there 
# print here  [-5:0])# if last is none then length be there

# here  = "printhh"
# print here [1:3:5])

# print
# a = int( int(input("Enter the number 1 : "))
# b =  int (int(input("Enter the number 2 :"))
# print("Numnber a is :", a)
# print("Numnber b is :", b)
# print("sum of a and b is ", a+b)

# --- NumPy Arithmetic Example ---
# Create two NumPy arrays
# array1 = np.array([1, 2, 3, 4])
# array2 = np.array([10, 20, 30, 40])

# Add the arrays element-wise
# sum_array = array1 + array2

# here  =  int(input("Enter your here  : ")
# print(f" hello you are MVP ,  here }")

# print("--- NumPy Example ---")
# print(f"Array 1: {array1}")
# print(f"Array 2: {array2}")
# print(f"Sum of arrays: {sum_array}")


# here  = ''' Dear <|NAME|> you are the strongest scorccer in modern age <|DATE|>'''
# print here .replace ("<|NAME|>","yuji").replace("<|DATE|>", "08 April 2025"))

# here  = "print is a good boy"
# print here .find("  "))
# here  = "print is a good  boy"
# print here .replace ("  ", " "))# does not change the main string they will change in new stirng  and print 

# print here )# string are immutable which mean you can not change them  during ruinnning function on  them   

# letter = "Dear yuji\n\t you are  the user of \"domain expansion."  
# print(letter)
# print = 

'''             LIST '''

'''# lists like arr can be change called muitable 
# list are mutable called change 
# string are non mutable called no change 
# stored elements in Hetrogenous form'''

friend = ["print", "satoru", 0 , 0.254 , False  ]  # lists like arr can be change called muitable 
print (friend) #  if the change is they don't create a new list # list are mutable called change 
friend[0] = "satoru" #  if Change  apply they create a new string # string are non mutable called no change 
print(friend[0])
friend.append ( "gojo") 

L1 = [2, 4, 6,1,8,5 ]
L1.sort()
print(L1)
L1.reverse()
print(L1)
L1.append(95)
print(L1)
L1.pop(5)
print(L1)
value = L1.pop(5)
print(value)
L1.insert(4 , 95)
print(L1)
L1.remove(95)
print(L1)

a = (1,2, 4564, 653, ":", "print")
print(type(a))
a[0] = 445
print(a) # tuple function  can not be change as same as string

my_tuple = (1,2,3,3,5)
no = my_tuple.count(3)
print(no)

no1 = my_tuple.index(3)
print(no1)
tuple1 = (1,2,3)
tuple2 = (4,5,6,)
concatinated = tuple1 + tuple2
print(concatinated)

tuple1 = (1,2,3)
tuple2 = (4,5,6,)
print(tuple1*3 , tuple2*3)

my_tuple = (2,3,4,5,6)
print(len(my_tuple))

my_tuple = (2,3,4,5,6)
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))

Write a program to stora seven marks in list entered by a user 

marks =[]

F1 = int(input("Enter the marks here  :" )
marks.append(F1)
F2 = int(input("Enter the marks here  :" )
marks.append(F2)
F3 = int(input("Enter the marks here  :" )
marks.append(F3)
F4 = int(input("Enter the marks here  :" )
marks.append(F4)
F5 = int(input("Enter the marks here  :" )
marks.append(F5)
F6 = int(input("Enter the marks here  :" )
marks.append(F6)
F7 = int(input("Enter the marks here  :" )
marks.append(F7)

print(marks)

write a program to accepts marks of 6 students and display them in a sorted manner

marks =[]

F1 = int(input("Enter the marks here  :" ))
marks.append(F1)
F2 = int(input("Enter the marks here  :" ))
marks.append(F2)
F3 = int(input("Enter the marks here  :" ))
marks.append(F3)
F4 = int(input("Enter the marks here  :" ))
marks.append(F4)
F5 = int(input("Enter the marks here  :" ))
marks.append(F5)
F6 = int(input("Enter the marks here  :" ))
marks.append(F6)



'''                                       Dicitionary '''
             
'''# Dicitionary -> key :value pairs
# # mutable 
# Hetrogenous
# Ordered
# We can access any values using keys 
'''


d = {'a' : 10 , 'b' : 20 , 'c' : 30 }
print (d)
d['a'] = 95


# 1. REMOVING VALUES -> remove a value present at the key and if the key is not present returns a defaults value.

d.pop('c',0)
print(d)

# 2. popitem()

# marks.sort()
# print(marks)
d = {} # empty dicitionary
ya = [3,4,5,6,6,]
print(sum(ya))

ya1 = [3,4,5,6,6,]
n = ya.count(6)
print(n)

marks =  {
 "print": 100,
 "goku" : 56,
 "satoru" : 100,
 "naruto" : 45,
 0: "mark "
}
print(type(marks))
print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"print":99})
print(marks)
print(marks.get("print1")) #print none # it returns the value of keys if keys if not in dict then return default 
print(marks["print1"]) # returns an  error

print(marks.clear())

new_marks = marks.copy() # for creating a new dict and prvious must be  copy and replaced with new
print(new_marks) 
keys = [ 'a','b','c']
new_marks = dict.fromkeys(keys) # for printing keys and it returns 0 
print(new_marks)

dict.popitem(new_marks) # follw LIFO means left in first out that removes and returns the ( keys ,values) and pair from the dictionary  
dict.pop(marks[ 0])
dict.setdefault() 

    # sets 
 
s = {3,4,5,6,7}
y = { 3,4,5,6,6 ,7,7} # Sets only consider one time value 
print(y)
s.add(566)
print(s ,type(s) ) 

e = set() # Don't use s ={} as it will create an empty dicitoinary
 

   # union and  intersection 
s1 = {3,4,5,6,7}
s2 = { 3,4,5,6,6 ,7,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

 # write a program to create a dicitinary of hindi words with  value as their english translastion . provide a user with an option to look it up 

words = {
    "kam " :" work",
    "madad": "help",
    "kitab": "book",
    "kela": "banana",
    "lakdi": "wood"

}
word = input("Enter the meaning of word you want :")
print(words[word])

write a program to input 8 numbers from the user and  display all the unique numbers (once)

s= set()

n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
n = int(input( "Enter the  number :"))
s.add(int(n)) 
print(s)
