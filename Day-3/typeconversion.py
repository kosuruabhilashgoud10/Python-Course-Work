Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
f=10.0
f
10.0
int(f)
10
complex(f)
(10+0j)
str(f)
'10.0'
list(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True
c=2+3j
int(C)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
float(C)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(C)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
dict(C)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
bool(c)
True
s='python'
s='12345'
s='34567.546780'
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '34567.546780'
a='12345'
b='3456.789'
int(a)
12345
int(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '3456.789'
float(s)
34567.54678
float(a)
12345.0
list(a)
['1', '2', '3', '4', '5']
list9s)
SyntaxError: unmatched ')'
list(s)
['3', '4', '5', '6', '7', '.', '5', '4', '6', '7', '8', '0']
list(b)
['3', '4', '5', '6', '.', '7', '8', '9']
tuple(s)
('3', '4', '5', '6', '7', '.', '5', '4', '6', '7', '8', '0')
tuple(a)
('1', '2', '3', '4', '5')
tuple(b)
('3', '4', '5', '6', '.', '7', '8', '9')
set(a)
{'4', '5', '2', '3', '1'}
set(b)
{'4', '5', '3', '8', '9', '6', '.', '7'}
set(c)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(s)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(b)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
complex(s)
(34567.54678+0j)
complex(b)
(3456.789+0j)
complex(b)
(3456.789+0j)
l=[1,2,3,4,5,6,7,8]
l
[1, 2, 3, 4, 5, 6, 7, 8]
int(L)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(L)
NameError: name 'L' is not defined. Did you mean: 'l'?
int(l)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5, 6, 7, 8]'
tuple(l)
(1, 2, 3, 4, 5, 6, 7, 8)
set(l)
{1, 2, 3, 4, 5, 6, 7, 8}
dict(l)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5,6,7)
t
(1, 2, 3, 4, 5, 6, 7)
int(t)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(1, 2, 3, 4, 5, 6, 7)'
complex(t)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
set(t)
{1, 2, 3, 4, 5, 6, 7}
bool(t)
True
s={1,2,3}
s
{1, 2, 3}
int(s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(S)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    float(S)
NameError: name 'S' is not defined. Did you mean: 's'?
string(s)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    string(s)
NameError: name 'string' is not defined
str(s)
'{1, 2, 3}'
list(S)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(S)
NameError: name 'S' is not defined. Did you mean: 's'?
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
dict(s)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
