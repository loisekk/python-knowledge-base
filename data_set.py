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



# l = [ 1 ,2 ,1 , 1 , 3 , 3,4 ,1,2 , 3, 4]
# new_l = []
# for i in l :
#     if i not in new_l:
#        new_l.append(i)
# print(new_l)


# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
# max = l[0]
# s_max = l[0]

# for i in range (1,len(l)):
#     if l[i] > max :
#         s_max = max
#         max = l[i]

# print(f"max value is {max} and second max is {s_max}")



''' finding second max number in list'''

# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
# max = float('-inf')
# s_max = float('-inf')

# for i in l:
#     if i > max :
#         s_max = max 
#         max = i 
#     elif max > i > s_max:
#         s_max = i

# print(f"max value is {max} and second max is {s_max}")

''' for indexing same que '''


# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
# max = float('-inf')
# s_max = float('-inf')  # assuming  -inf value for fake value assign
# index_max = 0
# index_smax = 0

# for i in range(len(l)): # st from o index 
#     if l[i]> max :
#         s_max = max 
#         index_smax = index_max
#         max = l[i] 
#         index_max = i
#     elif max > l[i] > s_max:
#         s_max = l[i]
#         index_max = i

# print(f"max value is {max} and second max is {s_max} and it's index is {index_smax}")

''' finding second lowest value '''
# l = [2 , 95 , 69 , 77 , 145 ,787788 ,  20, 966 ]
# max = float('inf') #  for - infinte value must be removed ' -inf '
# s_max = float('inf')
# index_max = 0
# index_smax = 0

# for i in range(len(l)):
#     if l[i]< max :
#         s_max = max 
#         index_smax = index_max
#         max = l[i] 
#         index_max = i
#     elif max < l[i] < s_max:
#         s_max = l[i]
#         index_max = i

# print(f"min value is {max} and second min is {s_max} and it's index is {index_smax}")

# l = [2 , 3 , 15 , 15 , 3 , 2 ]
# # print(list (l)[::-1])
# # if the original list and reverse list are same then it is palidrone

# rev_l = []
# # if len(l) % 
# for i in range(len(l)-1,-1, -1):
#     rev_l.append(l[i])
# print(rev_l)

# if l == l[::-1]:
#     print("palidrone number")
# else:
#     print("not a palidrone number")

''' Bubble sort '''

# l = [10 , 2 , 4 , 9 , 6 , 5 , 3 , 7 , 8 , 1 ]
# for j in range(len(l)):
#     for i in range(len(l)-1): # for the last element we take -1 to not go out of the index 
#         if l[i] > l[i+1]:
#             l[i] , l[i+1] = l[i+1] , l[i]
# print(l)

'''rev order sorting '''
# l = [10 , 2 , 4 , 9 , 6 , 5 , 3 , 7 , 8 , 1 ]
# for j in range(len(l)):
#     for i in range(len(l)): # for the last element we take -1 to not go out of the index 
#         if l[i] > l[j]:
#             # l[i] , l[j] = l[j] , l[i]
#             l[i] , l[j] = l[j] , l[i]
# print(l)





'''                                       Dicitionary '''
             
'''# Dicitionary -> key :value pairs
# # mutable 
# Hetrogenous
# Ordered
# We can access any values using keys 
'''


d = {'a' : 10 , 'b' : 20 , 'c' : 30 }
# print (d)
# d['a'] = 95


# 1. REMOVING VALUES -> remove a value present at the key and if the key is not present returns a defaults value.

# d.pop('c',0)
# print(d)

# 2. popitem()
# d.popitem()
# print(d)

# 3. -> Clear a dicitionay 

# d.clear()
# print(d)

# 4. -> delete 

# del d 
# print(d)

# 5. -> 

# dict = {'Name' : 'yash' , 'age' : 29 , 'score' : 95.5} 
# # we can access all keys 
# a = dict.keys()
# b = dict.values()
# print(a)
# print(b)

# for  loop always apply on keys 
# for i in dict : # i -> keys 
#     print(i, dict[i])


# d1 = {'a' : 10 , 'b' : 20 , 'c' : 30 }
# d2 = {'d' : 40 , 'e' : 50 , 'f' : 60 }

# for i in d2:
#     if i not in d1 :
#         d1[i] = d2[i]
# print(d1)
# print(d1 | d2)

# d1 = {'a' : 10 , 'b' : 20 , 'c' : 30 }
# sum = 0 
# for i in d1.values():
#     sum+= 1
# print(sum)
# l1 = [0 , 1 , 2 , 3 , 4 , 5]
# l2 = [10 , 20 , 30 , 40 , 50 ]

# l = l1 , l2
# for i in enumerate(l):
#     print(i)
    
# n = int(input("Enter the number :- "))
# if n % 3 == 0 :
#    print ("Weird")
# else :
#     for i in range (1 , 100):
#       if n % 3 == 0 :
#         print ("Weird")
#       elif n % 2 == 0 and n <=( 2, 5 ):
#         print ("Not Weird")
#       elif n % 2 == 0 and  n <= (6 , 20 ):
#         print("Weird in 6 , 20 ")
#       elif n % 2 == 0 and n > 20 :
#         print("NOt Weird")

# n = int (input("Enter the number :- "))
# if n % 3 == 0 :
#    print ("Weird")
# else :
#     for i in range (n):
#       if n % 2 == 0 or n <( 2, 5 ):
#         print ("Not Weird")
#       elif n % 2 == 0 or  n < (6 , 20 ):
#         print("Weird in 6 , 20 ")
#       elif n % 2 == 0 or n > 20 :
#         print("NOt Weird")

#       break 

# n = int(input().strip())

# if n % 2 == 1:
#     print("Weird")
# else:
#     if 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")

#     a = int(input())
#     b = int(input())
# c = a+ b 
# print (c)
# c1 = a-b
# print(c1)
# c2 = a * b 
# print(c2)




# l = [ 1 , 1, 1, 1, 2,3 , 2,  4, 5 ,4 , 4, 5 , 6 , 7, 7 , 8 , 8 ]
# d = {}
# for i in l :
#     if i not in d:
#         d[i] = 1 
#     else:
#         d[i]+= 1
# print(d)


# l= {'a' : 10 , 'b' : 20 , 'c' : 30 }
# l1 = {'d' : 40 , 'e' : 50 , 'f' : 60 }

# for i in (l1):
#      if i not in l:
#           l[i] = l1[i]
#      else:
#           l[i] += l1[i] 
# print(l)



''' SET '''
#01 : set is unordered
#02 : {} -> comma sepearated 
#03 : . UNIQUE ELEMENT STORE 
#04 : mutable

s = {}
l = [ 1 , 1, 1, 1, 2 , 2,  4, 5 ,4 , 4, 5 , 6 , 7, 7 , 8 , 8 ]
s = set(l) # BUILT - IN FUNCTON
print(s)

# # 1. .add()

s.add(3)
print(s)

# #2 . pop() -> remove first element
# s.pop()
# print(s)

# #3 . remove() -> need to give element 
s.remove(3)
print(s)


s1 = {1,2,3,4,5}
s2 = {3,4,5}

print(s1.intersection(s2))
# print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

''' TUPLES '''

'''
01. ordered -> indexing
02. immutable 
03. allow duplicacy

[] = flase , empty list
{} = empty dict
{1} = set()

we can't change tuple we can create a new one

01. .count() 
02. .index()
'''


''' # *args
 # **kwargs'''


'''# *args -> works on tuples'''

# def add(a , b , *number):
#   print(type(number))
#   print(sum(number))

# add(1,2,3,4,5,6,7,8,9)



'''# **kwargs -> ''' # it all depend on the '*' name must be anyoff

# def info(**sample):
#     for key,value in sample.items():
#         print(key,value)
#     print(sample['form'])
#     print(sample['age'])

# info (name = "yash" , age = 21 , form= "human" )


# augment ai coding 