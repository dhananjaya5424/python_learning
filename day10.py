# for x in 'rakesh':     
#     print(x, end=' ')                          
# print()                                        # r a k e s h


# for x in range(2, 7):
#     print(x, end=' ')  
# print()                                        # 2 3 4 5 6


# for x in [1,2,3]:
#     print(x, end=' ')
# print()                                          # 1 2 3 


# for x in (4,5,6):
#     print(x, end=' ') 
# print()                                          # 4 5 6


# for x in {7, 8, 9}:
#     print(x, end=' ') 
# print()                                              # 8 9 7 



d = {1:'a', 2:'b', 3:'c'}
# for x in d:
#     print(x, end=' ')  
# print()                                              # 1 2 3 

# for x in d.keys():
#     print(x, end=' ')  
# print()                                              # 1 2 3 

# for x in d:
#     print(d[x], end=' ') 
# print()                                               # a b c 

# for x in d.values():   
#     print(x, end=' ')
# print()                                               # a b c

# for x in d.items():     
#     print(x, end=' ')
# print()                                               # (1, 'a') (2, 'b') (3, 'c')



# #index based for loop. 
# #       0 1 2 3 4
# list = [5,4,3,2,1]
# #iterate from left to right 
# for x in range(5):
#     print(list[x], end=' ')                            # 5 4 3 2 1
# print()

  # -5,-4,-3,-2,-1        
list = [5,4,3,2,1]
# #iterate from right to left 
# for x in range(len(list)-1, -1, -1):
#     print(list[x], end=' ')                              # 1 2 3 4 5
# print()

# #iterate from 3rd element 
# for x in range(2, len(list)):
#    print(list[x], end = ' ')                                # 3 2 1

# # #iterate in steps of 2
# for x in range(0, len(list), 2):
#     print(list[x], end = ' ')                                 # 5 3 1 


# #tricky                             When you remove an element, the remaining elements shift left by one position.
# l = [1, 2, 3, 4, 5, 6]                              But the loop still advances to the next index, so it skips elements
# for x in l:
#     print(x, end=' ')
#     l.remove(x)                                            # 1 3 5 
  
                                                    #   NOTE:  if u want to remove all the values just use this [:]
                                                    #                            for x in l[:]:
                                                    #                                l.remove(x)
# # #Homework
# t = (5,4,3,2,1)
# s = {5,4,3,2,1}
# d = {5:'e', 4:'d', 3:'c', 2:'b', 1:'a'}
# w = 'rakesh'
# r = range(5,0,-1)
# print()

# # #continue   ----->             skips the remaining code in the current loop iteration and moves to the next iteration. 
# for x in range(1,11):                   if true skips and  then moves to nxt iteration and if false prints it and moves to nxt iteration
#     if x % 3 == 0:
#         continue 
#     print(x,end=' ')    
# print()                                           # 1, 2, 4, 5, 7, 8, 10


# # #break           -->>            immediately stops the entire loop, even if there are more elements left to process.
# for x in range(1,11):                         if condn true stops there only and if false iterates and prints 
#     if x % 3 == 0:       
#         break 
#     print(x,end=' ')  
# print()                                                       # 1 2 



#pass                           pass is a statement that does nothing. 
# for x in range(1,11):                  
#     pass
# a = 21


# #else 
# for x in range(1,11):
#     if x % 3 == 0:
#         continue  
#     print(x, end=' ')                               
# else:
#     print('Loop completed successfully')
# print()                                                       # 1 2 4 5 7 8 10    Loop completed succesfully
# for x in range(1, 11):
#     if x % 3 == 0:
#         break 
#     print(x, end=' ')
# else:
#     print('Loop completed successfully') 
# print('\n')                                                   # 1  2   
#                                                   


# #assert                                  is used to check whether a condition is True. If the condition is False,
# n = 10                                        Python raises an AssertionError and stops normal execution unless the error is handled.
# # assert n > 5, 'N is not greater than 5' 
# # print('A')                                               # A
# assert n < 5, 'N is not lesser than 5' 
# print('B')                                                   # Assertion error 
