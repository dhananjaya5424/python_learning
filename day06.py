# #append()
# l = ['a', 'b', 'c']          adds a single element to the very end of an existing list.                                   
# l.append(34)                      
# l.append(34.3)                       # Applicable to int, float, complex nos, list, tuple, set, dict, str, range
# l.append(4+3j)                              # NOTE : IN Set we cannot get the same sequence it can change 
# l.append(True)
# l.append(None)
# l.append([0,1,2])
# l.append((3,4,5))
# l.append({6,7,8})
# l.append({9:'a', 10:'b', 11:'c'})
# l.append('rakesh')
# l.append(range(12,15))
# print(l)                     #O/P : ['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3, 4, 5), {8, 6, 7}, {9: 'a', 10: 'b', 11: 'c'}, 'rakesh', range(12, 15)]




# # extend()               is a built-in list function used to add all elements from an iterable 
# l = ['a', 'b', 'c']             (such as a list, tuple, set, dictionary, or string) to the end of the current list
#                               # NOTE :IN THIS ALL elements placed in sequence cnsidering as single element  wthether it is tuple, list, set,dict
#                                          # This method cannot be used for int, float, complex, bool, none  which  raises error 
# #l.extend(34)
# #l.extend(34.3)
# #l.extend(4+3j)
# #l.extend(True)
# #l.extend(None)           
# l.extend((3,4,5))                
# l.extend([0,1,2])
# l.extend({6,7,8})
# l.extend({9:'a', 10:'b', 11:'c'})
# l.extend('rakesh')                              # adds str into each char
# l.extend(range(12,15))                            # and also for range O/P: [12, 13, 14]
# print(l)                          # O/P :  ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 'r', 'a', 'k', 'e', 's', 'h', 12, 13, 14]       



# # insert()                 inserts an element into a list at a specified index, but it is diffrent from append() in this it is assigned to specific index 
# #positive index
# l = ['a', 'b', 'c', 'd']
# l.insert(2, 'hi')
# print(l)                          # O/P: ['a', 'b', 'hi', 'c', 'd'] 
# l.insert(10, 'hi')
# print(l)                          # O/P:  ['a', 'b', 'hi', 'c', 'd', 'hi']       index >= len(l),then Python does not throw an "IndexError"     

# #negative index
# l = ['a', 'b', 'c', 'd', 'e']
# l.insert(-2, 'hi')
# print(l)                              # O/P:  ['a', 'b', 'c', 'hi', 'd', 'e']
# l.insert(-100, 'hi')
# print(l)                    #O/P:  ['hi', 'a', 'b', 'c', 'd', 'e'],    index <= len(l) then it is placed at beginning of the list 



# #pop()                  removes an element from a list and returns the removed element., Without any use Index 
# l = [1, 2, 3, 4, 5]                 like example refer print(a,l)     NOTE: returns removed element
# a = l.pop()
# print(a, l)                            # 5 [1,2,3,4]
# b = l.pop(2)
# print(b, l)                             # 3 [1,2,4]
# #c = l.pop(7)                                 # INDEX ERROR FOR INVALID index :  raises error
# del l[0]
# print(l)                             # [2,4]         Note : l.pop()-->> removes last element, l.pop(0) -->> Removes the first element
                                               # l.pop(-1) -->> removes last element , l.pop(100) -->>Raises IndexError if the index is out of range


# remove()             remove() method removes the first matching value from a list
# l = [1, 2, 3, 4]                                                                   # NOTE: returns NONE after removed element
# a  = l.remove(3)
# print(a, l)                                # NONE[1,2,4]
# #print(l.remove(5))                # VALUE ERROR FOR MISSING value : raises error


 
# clear()                     clear() method removes all elements from a list, leaving an empty list.
# l = [1, 2, 3, 4, 5]
# l.clear()
# print(l)                                    # [] 



# # reverse()             reverses the order of elements in a list in place (it modifies the original list). returns None
# l = [1, 2, 3, 4, 5]                                    # NOTE: returns NONE , when reversed also the id function remains same for value 
# print(id(l))                       # 2379872821376 : id function returns a unique identity number for an object during its lifetime.
# a = l.reverse()
# print(a, l)                        # None [5, 4, 3, 2, 1]
# print(id(l))                             #  2379872821376



# sort()                     method arranges the elements of a list in ascending order by default. It modifies the original list.
# l = [1,4,2,6,5,3]                                                                    # NOTE:  returns NONE
# print(id(l))               # 2229002461312
# a = l.sort() 
# print(a, l)                 # None [1,2,3,4,5,6]
# print(id(l))                     # 2229002461312
# l = [50,10,40,20,30]
# print(l.sort(reverse=True))
# print(l)                               # [50, 40, 30, 20, 10]




# # index()                    index() is a list method that finds the position of a value in a list.
# l = [1, 2, 1, 4, 6, 1, 7]
# print(l.index(1))                        # 0
# print(l.index(1, 3))                          #5
# #print(l.index(1, 3, 5))                            # error 
# #print(l.index(9))                                        # error 



# # count()                         In Python, the count() method counts how many times a value appears in a list.
# l = [1, 2, 1, 4, 1, 6, 7, 1]
# print(l.count(1))                                # 4
# print(l.count(9))                                       # 0


# # index() 
# l = (1, 2, 1, 4, 6, 1, 7)
# print(l.index(1))
# print(l.index(1, 3))
# # print(l.index(1, 3, 5))
# # print(l.index(9))

# # count() 
# l = (1, 2, 1, 4, 1, 6, 7, 1)
# print(l.count(1))
# print(l.count(9))
