# #strip, lstrip, rstrip
# a = '   python   '
# b = a.strip()       
# c = a.lstrip()
# d = a.rstrip()
# print(a, len(a))        # python      12     #3 spaces before python, 6 letters in python, 3 spaces after python
# print(b, len(b))        # 'python'     6      # strip() removes spaces from both side   
# print(c, len(c))        # 'python   '  9[ 3 Right_spaces + 6 letters] -->  lstrip() means left strip. It removes spaces only from the left side.
# print(d, len(d))        # '   python' 9[ 3 left_spaces +6 letters] --> rstrip() means right strip. It removes spaces only from the right side 
 
# #replace
# a = 'python is simple, python is easy to learn, python is all rounder'
# b = a.replace('python', 'java')
# print(a)                                          # python is simple, python is easy to learn, python is all rounder'
# print(b)                                           # java is simple, java is easy to learn, python is all rounder

# # #upper, lower, swapcase, title, capitalize
# a = 'PYTHON is simple, PYTHON is easy to LEARN'
# b = a.lower()
# c = a.upper()
# d = a.swapcase()
# e = a.title()       
# f = a.capitalize()   
# print('original', a)                                   # original PYTHON is simple, PYTHON is easy to LEARN
# print('lower:', b)                                       # 
# print('upper:', c)         
# print('swapcase:', d)      
# print('title:', e)         
# print('capitalize:', f)    

# #count, startswith, endswith
# s = 'python is python'
# print(s.count('th'))                 # 2
# print(s.startswith('py'))                      # True
# print(s.endswith('onn'))               # False
 
# # #find, index: 
# # #    0123456789           # find()--->> first occurrence, index()-->> first occurrence, but error if missing
# # s = 'abdcdefdgh'
# # print(s.find('d'))                   # 3     # find() searches for 'd' from the beginning
# # print(s.find('d', 5))              # 7          # means start searching from index 5.The first d after index 5 is at index 7
# # print(s.find('d', 5, 7))   # -1          # Search for 'd' from index 5 up to, but not including, index 7.There is no d.There is no d.find() returns -1 when char no found 
# # print(s.index('d'))        # 3             # index() also searches from the beginning.   # 3
# print(s.index('d', 5))           #Python cannot find d between indexes 5 and 7.unlike find(), index() does not return -1
# print(s.index('d', 5, 7))    #
# print()
# print()

# #rfind, rindex
# #    0123456789 
# s = 'abdcdefdgh'
# print(s.rfind('d'))                # 7                     # rfind()-->> Search for the rightmost occurrence, if not found -1 
# print(s.rfind('d', 5))            # 7                      # rindex()-->> Search for the rightmost occurrence, if not found error 
# print(s.rfind('d', 5, 7))              # -1 
# print(s.rindex('d'))              # 7
# print(s.rindex('d', 5))            # 7
# #print(s.rindex('d', 5, 7))   
# print()   
 

# #isalpha: 
# a = 'aBcD'                # isalpha() -- >> checks for whether a string contains only alphabet letters (A-Z or a-z).
# b = 'abc1'                                  # NOT for numbers, special char, spaces
# c = ''
# print(a.isalpha())           # True
# print(b.isalpha())         #  False
# print(c.isalpha())                    # False
# print() 
# print()

# #isdigit                               # checks whether a string contains only digits (0–9)
# a = '123'                               # NOT for alphabets(A-Z),(a-z), spaces,-ve no's, decimals
# b = '12.3'              
# c = '-123'
# print(a.isdigit())              # True
# print(b.isdigit())                # False
# print(c.isdigit())            # False
# print() 
# print()

# #isalnum:              #isalnum(): means "Is Alphabet + Number"
# a = 'Abc123'              # It checks whether a string contains only letters and/or numbers             
# b = 'Abc@123'
# c = ' '
# print(a.isalnum())            # True
# print(b.isalnum())        # False 
# print(c.isalnum())             # False
# print()                                                       # NOT for spaces , @, !, ., only numbers, only alpahbet
# print()

#isupper:            # isupper()-->>checks whether all the alphabetic characters in a string are uppercase (capital letters)
# a = 'ABC@123'                    #also for numbers , symobols in between
# b = '123'
# c = 'ABC123a'
# print(a.isupper())       # True
# print(b.isupper())       #False
# print(c.isupper())       #False
# print()
# print()

# #islower:                           #checks whether all the alphabetic characters in a string are lowercase (small letters)
# a = 'abc@123'
# b = '123'
# c = 'abc123A'
# print(a.islower())                     # True
# print(b.islower())                   # False
# print(c.islower())               # False

# #split
# s = 'abaca'
# print(s.split('a'))             #  ['', 'b', 'c', '']
# s = '   '
# print(s.split(' '))                # ['', '', '', '']
# print(s.split())                           # []
  
# # #join
# a = [1,2,3,4]
# b = ['1', '2', '3']             # only if u take it as char then only u can join  that '@'
# #print('@'.join(a))  
# print('@'.join(b))   

























