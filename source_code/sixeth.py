# st = "season 1 has only 12 episodes go and check it out "
# f = open("myfile.txt", "rt")
# f.close()


# f = open ("file.txt")
# lines = f.readlines()
# print(lines , type(lines ))

# line1 = f.readline()
# print(line1 , type(line1 ))

# line2 = f.readline()
# print(line2 , type(line2 ))

# line3 = f.readline()
# print(line3 , type(line3 ))

# line4 = f.readline()
# print(line4 , type(line4 ))

# line5 = f.readline()
# print(line5 == "")  # represent an empty string

# line = f.readline() # using " line = f.readlines() " this move can run the program ifinitely 
# while(line != ""):
#     print(line )
#     line = f.readline() # using " lines = f.readlines() " this move can run the program ifinitely 
# f.close()


# f = open("file.txt")
# print(f.read())

# f.close()

# The same can be written using with statement like this :
# with open("file.txt") as  f:
#     print(f.read())
# You don't have to explicity close the file    


# Write a program to read the text from a given file 'poems.txt' and find out whether it
# contains the word 'jujutsu'.


# with open("porem.txt") as f:
#     if "jujutsu" in f.read():
#         print("jujutsu is present in the file ")
#     else:
#         print ("jujutsu is  not present in the file ")

'''
The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
previous Hi-score. You need to write a program to update the Hi-score whenever the
game() function breaks the Hi-score.

'''



# import random 
# def game():
#     print("You are playing the game.. ")
#     score = random.randint(1, 92 ) # for generting random value b/w the 1 , 92
#     # fetch the Hiscore 
#     with open("Hiscore.txt") as f:
#         Hiscore = f.read()  # at this point all upto at string now 
#         if (Hiscore != ""): #  an empty str "" then convert the whole part in int terms 
#             Hiscore = int (Hiscore)
#         else: #  else there is an str so the f^n is return 0 becoz if condition does'nt work at this point and it return 0 there is no new hiscore 
#             Hiscore =0

#     print(f"Your score : {score}")
#     if (score> Hiscore ):# score becomes the new Hiscore 
#         # write this Hiscore to the file 
#         with open("Hiscore.txt","w") as f:
#             f.write(str(score)) # write f^n consider str only 
#     return score 

# import random
# def game():
#     print("You are playing game .. ")
#     score = random.randint(1 , 95)
#     # fetch the score 
#     with open("Hiscore.txt") as f : # always first at read and check the file or else we can applying conditions during this process 
#         Hiscore = f.read() # this f^n consider at str form 
#         if (Hiscore != ""): 
#             Hiscore = int(Hiscore) # after reading and check the emptiness they will convert it into int form 
#         else:
#             Hiscore = 0
#     print(f"Hiscore is : {score }")
#     if (score>Hiscore): # if scores is greater than hiscore then store it in the "Hiscore.txt" file 
#         with open("Hiscore.txt", "w")as f:
#             f.write(str(score))
    

# game()

# write a program to genrate a multiplication table from 2 to 20 and write it to the different files . palce this file in the  folder for 13 year old ;

# def Generatetable(n):
#     table =""
#     for i in range(1 , 11 ):
#             table += f"{n} X {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt","w")as f:
#           f.write(table)

# for i  in range(2,21):
#     Generatetable(i)
    


# A file contain a word "Donkey " multiple times .You need to write a program which repalce this word with ##### by updating the same file .

 # solving this with if else stat:

# word = "Donkey"
# with open ("file.txt", "r") as f:
#     f.read()
# newlines = []
# for line in newlines :

#  if "Donkey" in line:
#   with open ("file.txt", "w") as f:
#           line = line.replace("Donkey", "######") 

#  else : line = line 
#  print("word not found")

# word = "Donkey"
# with open("myfile.txt", "r")as f:
#     content = f.read()
# contentnew = content.replace(word, "######")
# with open ("myfile.txt" ,"w") as f:
    # f.write (contentnew) 



# Repeat program 4 for a list of such word to be consored.


# words = ["Donkey", "bad ", "joker"]
# with open("file.txt", "r")as f:
#     content = f.read()

# for word in words:
#  content= content.replace(word, "#" * len(word))

#  with open ("file.txt" ,"w") as f:
#     f.write (content)


# write a program to mine a log file and find out wheather it contain "python" .

# word = "python"

# with open("html.index" , 'r') as f:
#    content = f.read()

# if ("python" in content ):
#    print("word python is in the content")
#    newcontent  = content.replace(word, "#" * len(word))

#    with open ("html.index", "w") as f:
#       f.write (newcontent)
# else:
#    print("word python is not in the content")

# write a program to find out the line number in where python is present form que 6


# word = "python"

# with open("html.index" ) as f:
#    lines = f.readlines()

# lineno = 1
# for line in lines:
#     if ("python " in line):
#         print(f"python is present in the line : {lineno}")
#         break
#     lineno += 1

# else:
#    print("word python is not in the content")
   

# write a program to make a copy of text file "this .txt"

# with open("this.txt") as f:
#     content = f.read()

# with open ("this_copy.txt", "w") as f:
#     f.write (content )



# p = 10000
# r  = 15 
# t=    3
# print ((p*r*t)/100)
# print( int(p*(1+(r/100)))**t - p)
# print( (p*(1+(r/100)))**t)
# result = (p*(1+(r/100)))**t - p

# print ("the final result is {result}")


# gen = input("Enter your age :- ")
# gen1= input("Enter your age :- ")

# if gen == "m" or  gen == "f":
#     print("huh you are safe ")
    

# elif gen1 == "g" or gen1 == "f":
#     print("why are you gay ")
# else :
#     print(" what is your gen broo ")


# int = int(input ("enter your choice : "))
# if int % 2 == 0:
#     print("even")

# else:
#     print("odd")

# marks =int(input("tell your marks:-"))

# if marks >= 40:
#     print("pass")

# else:
#     print("fail")

# age = int(input("apni age batao:-"))

# if age<13:
#     print("you are a child")

# elif age >= 13 and age <= 19:
#     print("you are a teenager")
# else:
#     print("you are an adult")
    

# a = int(input ("tell your first number :-"))
# b = int(input ("tell your second number :-"))
# c = int(input ("tell your third number :-"))
# if a ==b and b==c:
#     print("all three are equal ")
# elif a > b and a >c :
#     print(f"{a} is the largest number ")
# elif b > a and  b >c :
#     print(f"{b} is the largest number ")
# elif c > b and c>a :
#     print(f"{c} is the largest number ")
# elif  a == b or b==c or a==c:
#     print(f"{c},{a},{b} is the equal number ")

# year = int(input ("Tell your year :-"))
# if year % 100 == 0 and year % 400 == 0 :
#     print("Your year is leap year ")
# elif year % 100 != 0 and year % 4== 0 :
#     print(" leap year ")

# else:
#     print("not a leap year")
    

# char = input("so what's your char :-")

# if char in "aeiouAEIOU":
#       print("vowel")
# else:
#      print("consonent")


'''' loops '''

# for i in range(1,101,1):
#       print("Hello yooo", end = "  ")

# a = int(input("what tabel you want "))
# for i in range (a , (a*10)+1,a):
#       print(i)



# n = int(input ("Tell your number :-"))

# for i in range (1,n+1):
#      if i%2 != 0:
#           print(i)


''' List '''

# s = int (input(" How many elements you want :- "))
# l = []
# for i in range(s):
#     z = int(input(" Tell the element :- "))
#     l.append(z)

# print(l)


# a = [ 10 , 20, 30, 40, 50]
# sum = 0
# even = 0 
# odd = 0
# for i in (a):
#     input("index number : ")
#     if int (i % 2 == 0) :
#         print(f"even number {i}")
#         evem = even +i 
#     else :
#         print("odd number {i}")
#         odd = odd +i 
#     print(f" your even sum is {even},your odd sum is {odd}")
    
#     print(sum)

# a = [ 10 , 20, 30, 40, 50]

# for i in range(len(a)-1):
#     c = ( len(a[i]-a[i+1]))

#     print(c[i])
#     print(a[i])

# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20,966 ]
# max = l[0]
# for i in range(1 ,  len(l)):
    
#     if max < l[i] : ''' does't required index to be define " < " exception operator '''
#         max  = l [i]
#         index = i
# print(f" The max number is {max} and it's index is {index} ")

# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
# min = l[0]
# index = 0
# for i in range(1 ,  len(l)):
    
#     if min > l[i]: # ''' required index to be define for " > " related to prev garbage value '''
#      min  = l [i]
#      index = i
# print(f" The min number is {min} and it's index is {index} ")

