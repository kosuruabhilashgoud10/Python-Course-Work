Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[10,20,30,40,890,6]
sorted[l]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sorted[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
sorted(l)
[6, 10, 20, 30, 40, 890]
l.sort()
l
[6, 10, 20, 30, 40, 890]
min(l)
6
max(l)
890
l.reverse()
l
[890, 40, 30, 20, 10, 6]
sorted(l,reverse=True)
[890, 40, 30, 20, 10, 6]
l
[890, 40, 30, 20, 10, 6]
l=[6,8,10,5,8]
sorted(l,reverse=True)
[10, 8, 8, 6, 5]
l.index(8)
1
l.index(88)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.index(88)
ValueError: 88 is not in list
l.count(8)
2
l.count(6)
1
l
[6, 8, 10, 5, 8]
0.0.
SyntaxError: invalid syntax
0
0























l
[6, 8, 10, 5, 8]
l=m
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l=m
NameError: name 'm' is not defined
m=l
m
[6, 8, 10, 5, 8]
m.append(90)
m
[6, 8, 10, 5, 8, 90]
l
[6, 8, 10, 5, 8, 90]
m=l.copy()
m
[6, 8, 10, 5, 8, 90]
m.append(60)
m
[6, 8, 10, 5, 8, 90, 60]
l
[6, 8, 10, 5, 8, 90]
len(l)
6
sum(l)
127
any([1,2,4,5,6,0,0,0,0])
True
all([1,2,3,4,5,0,0,0])
False
any([0,0,0,0])
False
all([1,2,3,4])
True
