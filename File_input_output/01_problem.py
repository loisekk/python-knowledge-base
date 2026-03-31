'''f = open("file.txt" , "r")
# data = f.read()
print(f)
f.close()'''


'''st = "season 1 has only 12 episodes go and check it out "
f = open("myfile.txt", "rt")
f.close()
'''

'''f = open ("file.txt")
lines = f.readlines()
print(lines , type(lines ))

line1 = f.readline()
print(line1 , type(line1 ))

line2 = f.readline()
print(line2 , type(line2 ))

line3 = f.readline()
print(line3 , type(line3 ))

line4 = f.readline()
print(line4 , type(line4 ))

line5 = f.readline()
print(line5 == "")  # represent an empty string

line = f.readline() # using " line = f.readlines() " this move can run the program ifinitely 
while(line != ""):
    print(line )
    line = f.readline() # using " lines = f.readlines() " this move can run the program ifinitely 
f.close()'''


'''f = open("file.txt")
print(f.read())

f.close()'''

# The same can be written using with statement like this :

'''with open("file.txt") as  f:
    print(f.read())'''
# You don't have to explicity close the file    


'''Write a program to read the text from a given file 'poems.txt' and find out whether it
contains the word 'jujutsu'. '''


'''with open("porem.txt") as f:
    if "jujutsu" in f.read():
        print("jujutsu is present in the file ")
    else:
        print ("jujutsu is  not present in the file ")
'''

'''
The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
previous Hi-score. You need to write a program to update the Hi-score whenever the
game() function breaks the Hi-score.

'''



'''import random 
def game():
    print("You are playing the game.. ")
    score = random.randint(1, 92 )
    # fetch the Hiscore 
    with open("Hiscore.txt") as f:
        Hiscore = f.read()  # at this point all upto at string now 
        if (Hiscore != ""): #  an empty str "" then convert the whole part in int terms 
            Hiscore = int (Hiscore)
        else: #  else there is an str so the f^n is return 0 becoz if condition does'nt work at this point and it return 0 there is no new hiscore 
            Hiscore =0

    print(f"Your score : {score}")
    if (score> Hiscore ):# score becomes the new Hiscore 
        # write this Hiscore to the file 
        with open("Hiscore.txt","w") as f:
            f.write(str(score)) # write f^n consider str only 
    return score '''


''''
import random
def game():
    print("You are playing game .. ")
    score = random.randint(1 , 95)
    # fetch the score 
    with open("Hiscore.txt") as f : # always first at read and check the file or else we can applying conditions during this process 
        Hiscore = f.read() # this f^n consider at str form 
        if (Hiscore != ""): 
            Hiscore = int(Hiscore) # after reading and check the emptiness they will convert it into int form 
        else:
            Hiscore = 0
    print(f"Hiscore is : {score }")
    if (score>Hiscore): # if scores is greater than hiscore then store it in the "Hiscore.txt" file 
        with open("Hiscore.txt", "w")as f:
            f.write(str(score))
    

game()
'''

# write a program to genrate a multiplication table from 2 to 20 and write it to the different files . palce this file in the  folder for 13 year old ;

'''def Generatetable(n):
    table =""
    for i in range(1 , 11 ):
            table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w")as f:
          f.write(table)

for i  in range(2,21):
    Generatetable(i)'''


# A file contain a word "Donkey " multiple times .You need to write a program which repalce this word with ##### by updating the same file .

 # solving this with if else stat:

'''word = "Donkey"
with open ("file.txt", "r") as f:
    f.read()
newlines = []
for line in newlines :

 if "Donkey" in line:
  with open ("file.txt", "w") as f:
          line = line.replace("Donkey", "######") 

 else : line = line 
 print("word not found")'''




'''word = "Donkey"
with open("myfile.txt", "r")as f:
    content = f.read()
contentnew = content.replace(word, "######")
with open ("myfile.txt" ,"w") as f:
    f.write (contentnew) 
'''


# Repeat program 4 for a list of such word to be consored.


'''words = ["Donkey", "bad ", "joker"]
with open("file.txt", "r")as f:
    content = f.read()

for word in words:
 content= content.replace(word, "#" * len(word))

 with open ("file.txt" ,"w") as f:
    f.write (content)'''


# write a program to mine a log file and find out wheather it contain "python" .

'''word = "python"

with open("html.index" , 'r') as f:
   content = f.read()

if ("python" in content ):
   print("word python is in the content")
   newcontent  = content.replace(word, "#" * len(word))

   with open ("html.index", "w") as f:
      f.write (newcontent)
else:
   print("word python is not in the content")'''

# write a program to find out the line number in where python is present form que 6


'''word = "python"

with open("html.index" ) as f:
   lines = f.readlines()

lineno = 1
for line in lines:
    if ("python " in line):
        print(f"python is present in the line : {lineno}")
        break
    lineno += 1

else:
   print("word python is not in the content")'''
   

# write a program to make a copy of text file "this .txt"

'''with open("this.txt") as f:
    content = f.read()

with open ("this_copy.txt", "w") as f:
    f.write (content )'''


# write a program to find out wheather a file is identical & matches the content of another file .

'''with open("myfile.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print(" Yes this file are identical")
else:
    print(" No this file are not identical")'''


# write a program to wipe out the content of file using python 

'''
with open ("this_copy.txt", "w") as f:
    f.write("")
'''

# write a program to rename file to "renamed_by_python.txt " .

'''with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
     f.write(content)''' # after making new copy of old file simple delete the old file this was made without using any module 


