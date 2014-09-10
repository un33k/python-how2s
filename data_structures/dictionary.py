>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
>>> vowels
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}


>>> {x:x*x for x in (1, 2, 3)}
{1: 1, 2: 4, 3: 9}


>>> dict([(1,'a'), (2,'e'), (3,'i'), (4,'o'), (5,'u')])
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}


>>> dict(a=1, e=2, i=3, o=4, u=5)
{'i': 3, 'u': 5, 'e': 2, 'a': 1, 'o': 4}

>>> dict(1=a, 2=e, 3=i, 4=o, 5=u)
  File "<stdin>", line 1
SyntaxError: "keyword can't be an expression"


>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
>>> vowels[1]
'a'
>>> vowels[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 10
>>>


>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
>>> del(vowels[1])
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> del(vowels[10])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 10
>>>


>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
>>> vowels.keys()
[1, 2, 3, 4, 5]
>>> vowels.values()
['a', 'e', 'i', 'o', 'u']


>>> for k, v in vowels.iteritems():
...     print k, v
...
1 a
2 e
3 i
4 o
5 u
>>> for v in vowels.itervalues():
...     print v
...
a
e
i
o
u
>>>

