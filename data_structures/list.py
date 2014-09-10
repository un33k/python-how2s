>>> l = ['a', 'b', 123]
>>> l
['a', 'b', 123]


>>> l[0]
'a'
>>> l[10]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range


>>> l = ['a', 'b', 123]
>>> l[:]
['a', 'b', 123]
>>> new_l = l[1:]
>>> new_l
['b', 123]
>>> l
['a', 'b', 123]


>>> l.extend ([1, 2])
>>> l
['a', 'b', 123, 1, 2]
>>> l.sort()
>>> l
[1, 2, 123, 'a', 'b']
>>> l.reverse()
>>> l
['b', 'a', 123, 2, 1]

>>> l = ['a', 'b', 123]
>>> l.append(234) #inserts an element at the end of the list
>>> l
['a', 'b', 123, 234]
>>> l.insert(2, 'c') #inserts an element into the third position
>>> l
['a', 'b', 'c', 123, 234]
>>> l.insert(-1, 111) #inserts an element into the second from last position
>>> l
['a', 'b', 'c', 123, 111, 234]
>>> l.remove(111) #removes an element based on value
>>> l
['a', 'b', 'c', 123, 234]
>>> l.remove('does not exist in the list')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list


>>> last_element = l.pop() #returns the last element, modifying the list
>>> last_element
234
>>> l
['a', 'b', 'c', 123]
>>> third_element = l.pop(2) #returns the third element, modifying the list
>>> third_element
'c'
>>> l
['a', 'b', 123]
>>> l.index('a')
0
>>> l.index('does not exist in the list')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'does not exist in the list' is not in list
>>> l.count('a') #returns the number of occurrences of an element
1

>>> l.extend ([1, 2]) # concatenates a list on to the existing list
>>> l
['a', 'b', 123, 1, 2]
>>> l.sort()
>>> l
[1, 2, 123, 'a', 'b']
>>> l.reverse()
>>> l
['b', 'a', 123, 2, 1]


>>> l = [1, 2, 3]
>>> new_l = [x*2 for x in l]
>>> new_l
[2, 4, 6]
