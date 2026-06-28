Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,1,1,1,1}
s
{1}
s={78,98,800,567,890,090,567,43}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s={89,78990,67,89,345,6789}
s
{67, 6789, 345, 89, 78990}
s=set()
s
set()
s.add(1)
s
{1}
s.add(576.89)
s
{576.89, 1}
s.add('revathi')
s
{576.89, 1, 'revathi'}
s.add([11,23,45,76])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add([11,23,45,76])
TypeError: unhashable type: 'list'
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: unhashable type: 'set'
s.add((1,2,3,4))
s
{576.89, 1, 'revathi', (1, 2, 3, 4)}
s.add({2:4,3:2})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add({2:4,3:2})
TypeError: unhashable type: 'dict'
s
{576.89, 1, 'revathi', (1, 2, 3, 4)}
1 in s
True
2 in s
False
1 not in s
False
(1,2,3,4)in s
True
a={1,2,3,4,5,6,7}
b={6,7,8,9}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{6, 7}
a&b
{6, 7}
a-b
{1, 2, 3, 4, 5}
a^b
{1, 2, 3, 4, 5, 8, 9}
#subsets
a<={1}
False
a>={1}
True
a<={1,2,3,4,5}
False
a>={6,10,8}
False
a
{1, 2, 3, 4, 5, 6, 7}
b
{8, 9, 6, 7}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 17}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 17}
a.pop()
1
a.pop()
2
a.remove(6)
a
{3, 4, 5, 7, 11, 12, 13, 17}
a.discard(6)
a
{3, 4, 5, 7, 11, 12, 13, 17}
a.remove(6)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove(6)
KeyError: 6
a.discard(5)
a
{3, 4, 7, 11, 12, 13, 17}
a.clear()
a
set()
a={12,23,4,5,7}
b={1,2,3,4}
a.intersection(b)
{4}
a
{4, 5, 23, 7, 12}
b
{1, 2, 3, 4}
a.intersection_update(b)
a
{4}
b
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c=b
c.add(12)
c
{1, 2, 3, 4, 12}
b
{1, 2, 3, 4, 12}
d=c.copy()
d
{1, 2, 3, 4, 12}
b
{1, 2, 3, 4, 12}
c
{1, 2, 3, 4, 12}
len(C)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    len(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
len(c)
5
min(c)
1
max(c)
12
sorted(c)
[1, 2, 3, 4, 12]
sum(c)
22
