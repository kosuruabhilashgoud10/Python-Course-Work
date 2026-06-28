Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l=list()
type()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type(l)
<class 'list'>
type()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type
<class 'type'>
l=[1,2,3,4,5]
m=[6,7,8,9,7]
l+m
[1, 2, 3, 4, 5, 6, 7, 8, 9, 7]
l*4
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l=[10,20,30,40,50]
l
[10, 20, 30, 40, 50]
l[1]
20
l[:3]
[10, 20, 30]
l[:2]
[10, 20]
l[1:4]
[20, 30, 40]
l[1:4:2]
[20, 40]
l[-1]
50
l[-3]
30
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-2:-3:-2]
[40]
l[-3::-1]
[30, 20, 10]
30 in l
True
90 in l
False
l
[10, 20, 30, 40, 50]
id(l)
2965204158080
l[4]
50
l[4]=1000
l
[10, 20, 30, 40, 1000]
l.append(120)
l
[10, 20, 30, 40, 1000, 120]
l.append(400)
l
[10, 20, 30, 40, 1000, 120, 400]
l.insert(2,40)
l
[10, 20, 40, 30, 40, 1000, 120, 400]
l.insert(1,50)
l
[10, 50, 20, 40, 30, 40, 1000, 120, 400]
l.extend([180,90,9])
l
[10, 50, 20, 40, 30, 40, 1000, 120, 400, 180, 90, 9]
l.pop()
9
l
[10, 50, 20, 40, 30, 40, 1000, 120, 400, 180, 90]
l.pop()
90
l
[10, 50, 20, 40, 30, 40, 1000, 120, 400, 180]
l.pop(3)
40
l
[10, 50, 20, 30, 40, 1000, 120, 400, 180]
l.pop(2)
20
l
[10, 50, 30, 40, 1000, 120, 400, 180]
l.remove(40)
l
[10, 50, 30, 1000, 120, 400, 180]
l.remove(180)
l
[10, 50, 30, 1000, 120, 400]
del l[1]
l
[10, 30, 1000, 120, 400]
del l[3]
l
[10, 30, 1000, 400]
l.clear()
l
[]
id(l)
2965204158080
