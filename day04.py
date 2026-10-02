# # #Arithmetic 

# # + :  (this '+' operator works on only int , list , tuple , str data type only )
# a = 45 + 4.5
# b = True + False 
# c = 4+5j + 6+7j
# #d = None + 5 
# e = [1,2,3] + [4,5,6]
# f = (1,2,3) + (4,5,6)
# g = 'rak' + 'esh'
# #h = range(1,4) + range(4,7)
# #i = {1,2,3} + {4,5,5}
# #j = {1:'a', 2:'b'} + {3:'c', 4:'d'}
# #k = [1,2,3] + (1,2,3)
# #l = [1,2,3] + 'rak'
# print(a)                                     # 49.5
# print(b)                                  #1
# print(c)                            #(10+12j)
# #print(d)                                        #type error
# print(e)                                       # [1,2,3,4,5,6]
# print(f)                                  #(1,2,3,4,5,6)
# print(g)                                    #rakesh
# #print(h)                                        #(1,2,3,4,5,6)
# #print(i)              #{1,2,3,4,5}  #TypeError: unsupported operand type(s) for +: 'set' and 'set'
# #print(j)              # {1: 'a', 2: 'b', 3: 'c', 4: 'd'} #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# #print(k)            #TypeError: can only concatenate list (not "tuple") to list
# #print(l)         #TypeError: can only concatenate list (not "str") to list



# - :    (this '-'minus operator works on SET data type only)
# a = 45 - 5.5
# b = 4+5j - 3+2j 
# c = True - False 
# # d = [1,2,3] - [2,3]              
# #e = (1,2,3) - (2,3)
# f = {1,2,3,4} - {2,1}
# #g = {1:'a', 2:'b', 3:'c'} - {2:'b', 3:'c'}
# print(a)                                            # 40.5
# print(b)                                                 #(1+3j)
# print(c)                                               # 1
# #print(d)                 # TypeError: unsupported operand type(s) for -: 'list' and 'list'     
# #print(e)                   # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'                          
# print(f)                    
# #print(g)              #TypeError: unsupported operand type(s) for -: 'dict' and 'dict'         



# #* : 
# a = 4 * 5.4                   
# b = True * False 
# c = (4+5j) * (3+2j)
# #d = [1,2,3] * (2,3)
# e = [1,2,3] * 3 
# #f = [1,2,3] * 3.0
# g = (1,2,3) * 3 
# h = 'rakesh' * 3 
# #i = {1,2,3} * 3 
# #j = {1:'a', 2:'b', 3:'c'} * 3
# k = [1,2,3]
# l = range(1,2,3)
# m = (4,5,6)
# print(a)                                        # 21.6
# print(b)                                 # 0
# print(c)           #  (2 + 23j)
# # print(d)            #TypeError: can't multiply sequence by non-int of type 'tuple'
# print(e)              # [1,2,3,1,2,3,1,2,3]
# # print(f)                    #TypeError: can't multiply sequence by non-int of type 'float'
# print(g)                     #(1,2,3,1,2,3,1,2,3)
# print(h)                        #rakeshrakeshrakesh
# # print(i)          #TypeError: unsupported operand type(s) for *: 'set' and 'int'
# #print(j)         #TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# print(*k)      #  1 2 3 
# print(*l)      # 1 2 3 
# print(*m)         # 4 5 6 

# ** : power 
# a = 5 ** 2 
# b = 3 ** 2.3
# c = (3+4j) ** (1+2j)
# print(a)                     #  25
# print(b)           #  13.928756378655804
# print(c)              #(-0.4192275503281095-0.03392409290517046j)

# # # / : Division
# # a = 5 / 2        # 2.5
# # print(a)

# # # // : floor division
# # a = 5 // 2     
# # print(a)                 # 2 
# # a = 5.5 // 2   
# # print(a)           # 2.0

# # # % : Modulus
# # a = 5 % 2                   # 1 
# # print(a)


# # # #Relational Operators 
# # print(5 == 6.5)                 # False
# # print(1 == True)                # True
# # print(2 == None)                 #False
# # print(4+5j == 4+6j)                #False
# # print(5 > 6.5)                 # False
# # print(1 > True)                # False
# # print(2 > None)                 #False
# # print(4+5j > 3+2j)                #TypeError: '>' not supported between instances of 'complex' and 'complex'
# # print([1,2,3] == [1,2,4])              # False
# # print([1,2,3] > [1,3,4])               # False
# # print((1,2,3) > (1,3,4))               # False
# # print({1,2,3} > {1,2})                 # True
# # # print({1:2, 2:3} > {3:4, 4:5})         #TypeError: '>' not supported between instances of 'dict' and 'dict'
# # print({1:2, 2:3} == {1:2, 2:3})      # True
# # print([1,2,3] == (1,2,3))            # False
# # print([1,2,3] > (1,2,3))           #TypeError: '>' not supported between instances of 'list' and 'tuple'

# # # #True or False
# # print(bool(0))    #False
# # print(bool(4.5))  #True           # any non zero no is true
# # print(bool(''))   #False       # empty string 
# # print(bool('r'))  #True              # any non empty string is true
# # print(bool([]))   #False           # empty list
# # print(bool([1]))  #True             # any non empty list is true
# # print(bool(None)) # False             #  none means False

# print()
# print()
# # #Logical Operators
# print( 4 and 0 and 6 )   #0
# print( 4 and 1 and 6 )   #6              #    study and repeeat revison is needed 
# print( 4 or 0 or 6)      #4
# print(0 or '' or [])     #[]
# #mixed
# print(4 or 0 and 6)   
# #not reverse the bool value
# print(not False) 
# print(not True) 

# # #Assignment operators
# # a = 10          # 10
# # a += 20           # 30
# # a -= 10           # 0
# # a *= 2               # 20
# # a **= 2              #    100
# # a /= 2                  # 50.0
# # a //= 3                  # 16.0
# # a %= 3                    # 1
# # print(a)

# # #Identity Operators 
# # a = 34 
# # b = 34 
# # print(a is b)      # true
# # a = 3+4j 
# # b = 3+4j 
# # print(a is b)         # false
# # a = [1,2,3]
# # b = [1,2,3]
# # print(a is b)          # false
# # a = 'rakesh'
# # b = 'rakesh'
# # print(a is b)           # true
# # a = range(1,4)
# # b = range(1,4)
# # print(a is b)     # false
# # a = (1,2,3)
# # b = (1,2,3)
# # print(a is b)      # true
# # a = {1,2,3}
# # b = {1,2,3}
# # print(a is b)   # false
# # print()
# # print()

# # #Membership 
# # a = [1,2,3,4]
# # b = {1,2,3,4}
# # c = 'rakesh'
# # d = (1,2,3,4)
# # e = {1:'a', 2:'b', 3:'c'}
# # f = range(1,4)
# # print(5 in a)
# # print(3 in b)
# # print('r' in c)
# # print(4 in d)
# # print('b' in e)
# # print(3 in e)
# # print(4 in f)

# # #Walrus operator
# # # print(a = 4)
# # print(a := 4)
# # print(a)

#ternary operator 
a = 5 if 10 > 20 else 6 
print(a)
a = [1,2,3] if 5 < 10 else (1,2,3)
print(a)
