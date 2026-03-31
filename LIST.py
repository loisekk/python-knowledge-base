
'''             LIST '''

'''# lists like arr can be change called muitable 
# list are mutable called change 
# string are non mutable called no change 
# stored elements in Hetrogenous form'''


# l =  [2, 4, 6,1,8,5 ]
# l.pop()
# print(l)
'''it bydefault removes last element''' # like an stack LIFO 


# friend = ["yash", "satoru", 0 , 0.254 , False  ]  
# print (friend) 
# friend[0] = "satoru" 
# print(friend[0])
# friend.append ( "gojo") 

# L1 = [2, 4, 6,1,8,5 ]
# L1.sort()
# print(L1)
# L1.reverse()
# print(L1)
# L1.append(95)
# print(L1)
# L1.pop(5)
# print(L1)
# value = L1.pop(5)
# print(value)
# L1.insert(4 , 95)
# print(L1)
# L1.remove(95)
# print(L1)


''' LAMBDA  FUNCTION '''



# def sample(param): # function define -> parameter 

#     print("hello world ")
# sample("yash") # function call -> arugment 


# syntax 
# lambda PARAMETER : CODE TO BE EXECUTED IF 
# PARAMETER ARE THERE .
# lambda -> keyword 
#

# add up 2 number 
# sample = lambda a ,b : a + b
# print(sample(10 , 10 )) # sample is a fun not a variable 


''' Accept a  number as a parameter and check whether the number is even or odd '''


# check = lambda  n : "even " if n % 2 == 0   else ("odd")
# print(check(12 , 33))


# index = lambda l , i : l[i] 
# print(index ([ 10 , 20 , 30 , 40 ],2))

# # default parameters - > funtions define a - 10 
# # keyword arguments - > function define (parametes)

# sample = lambda name , gender : print(name , gender )
# sample(name = "yash" , gender= "male")



dic = {'a' : 100 , 'b' : 50 , 'c' : 200}
l1 = list(dic)
l=  [l1]
for i in l:
  l.sort()
  l.append([i , l[i]])

print(l)
     