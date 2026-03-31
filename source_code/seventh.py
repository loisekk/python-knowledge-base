l = [ 1 ,2 ,1 , 1 , 3 , 3,4 ,1,2 , 3, 4]
new_l = []
for i in l :
    if i not in new_l:
       new_l.append(i)
print(new_l)


l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
max = l[0]
s_max = l[0]

for i in range (1,len(l)):
    if l[i] > max :
        s_max = max
        max = l[i]

print(f"max value is {max} and second max is {s_max}")



''' finding second max number in list'''

l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
max = float('-inf')
s_max = float('-inf')

for i in l:
    if i > max :
        s_max = max 
        max = i 
    elif max > i > s_max:
        s_max = i

print(f"max value is {max} and second max is {s_max}")

''' for indexing same que '''


l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
max = float('-inf')
s_max = float('-inf')  # assuming  -inf value for fake value assign
index_max = 0
index_smax = 0

for i in range(len(l)): # st from o index 
    if l[i]> max :
        s_max = max 
        index_smax = index_max
        max = l[i] 
        index_max = i
    elif max > l[i] > s_max:
        s_max = l[i]
        index_max = i

print(f"max value is {max} and second max is {s_max} and it's index is {index_smax}")

''' finding second lowest value '''
l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
max = float('inf') #  for - infinte value must be removed ' -inf '
s_max = float('inf')
index_max = 0
index_smax = 0

for i in range(len(l)):
    if l[i]< max :
        s_max = max 
        index_smax = index_max
        max = l[i] 
        index_max = i
    elif max < l[i] < s_max:
        s_max = l[i]
        index_max = i

print(f"min value is {max} and second min is {s_max} and it's index is {index_smax}")

l = [2 , 3 , 15 , 15 , 3 , 2 ]
# print(list (l)[::-1])
# if the original list and reverse list are same then it is palidrone

rev_l = []
# if len(l) % 
for i in range(len(l)-1,-1, -1):
    rev_l.append(l[i])
print(rev_l)

if l == l[::-1]:
    print("palidrone number")
else:
    print("not a palidrone number")

''' Bubble sort '''

l = [10 , 2 , 4 , 9 , 6 , 5 , 3 , 7 , 8 , 1 ]
for j in range(len(l)):
    for i in range(len(l)-1): # for the last element we take -1 to not go out of the index 
        if l[i] > l[i+1]:
            l[i] , l[i+1] = l[i+1] , l[i]
print(l)

'''rev order sorting '''
l = [10 , 2 , 4 , 9 , 6 , 5 , 3 , 7 , 8 , 1 ]
for j in range(len(l)):
    for i in range(len(l)): # for the last element we take -1 to not go out of the index 
        if l[i] > l[j]:
            # l[i] , l[j] = l[j] , l[i]
            l[i] , l[j] = l[j] , l[i]
print(l)

'''selection sort '''


import random 
top_of_range = input("TYPE A NUMBER -> ") # it takes as str 

if top_of_range.isdigit(): # need to convert into this 
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("please choose number larger than '0' next time !:" )
        quit()
else:
    print("please type a number  next time !:" )
    quit()

random_number = random.randint(0 , top_of_range)
guesses = 0 

while True :
   guesses +=1
   user_guess = input("make a guess buddy !: ")
   if user_guess.isdigit(): 
    user_guess = int(user_guess)
   else:
    print("please type a number  next time !:" )
    continue
   
   if user_guess == random_number:
      print("YOU GOT IT BROO 😜")
      break
   elif user_guess > random_number:
         print("you were above the number ⬆️")
   else:
         print("you were below the number ⬇️")

print(f"YOU GOT it in {guesses} guesses pretty much hilirious 😵‍💫")
