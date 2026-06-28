Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name=input()
hari
name
'hari'
name=input("enter your name:")
enter your name:Revathi
name
'Revathi'
age=input("enter your age:")
enter your age:21
age
'21'
cgpa=float(input("enter your cgpa:"))
enter your cgpa:8.1
cgpa
8.1
type(cgpa)
<class 'float'>
'revathi','aishu','usha'
('revathi', 'aishu', 'usha')
revathi','aishu','usha'
SyntaxError: unterminated string literal (detected at line 1)
'revathi','aishu','usha'
('revathi', 'aishu', 'usha')
'revathi','aishu','usha'
('revathi', 'aishu', 'usha')
'revathi aishu usha '
'revathi aishu usha '
'revathi,aishu,usha'.splilt(' ')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    'revathi,aishu,usha'.splilt(' ')
AttributeError: 'str' object has no attribute 'splilt'. Did you mean: 'split'?
revathi,aishu,usha'.splilt(',')
SyntaxError: unterminated string literal (detected at line 1)
revathi,aishu,usha'.split('')
SyntaxError: unterminated string literal (detected at line 1)
'revathi,aishu,usha'.split(',')
['revathi', 'aishu', 'usha']
names=input("enter the names:").split
enter the names:revathi aishu usha
names
<built-in method split of str object at 0x00000276E208B500>
names=input("enter the names:").split
enter the names:revathi aishu usha
enter the names:revathi aishu usha
names
<built-in method split of str object at 0x00000276E2129660>
555555555555444444444444444444444444444444444444444444444444444444444444
555555555555444444444444444444444444444444444444444444444444444444444444
ames=input("enter the names:").split()
enter the names:revathi aishu usha
enter the names:revathi aishu usha
names
<built-in method split of str object at 0x00000276E2129660>
ames
['revathi', 'aishu', 'usha']
topics=tuple(input("enter your topics:").split())
enter your topics:token statement
topics
('token', 'statement')
op=set(input('enter your oper:").split())
             
SyntaxError: unterminated string literal (detected at line 1)
op=set(input("enter your oper:").split())
             
enter your oper:in  not in is is not and or not
op
             
{'is', 'and', 'in', 'or', 'not'}
list(map(int,input("enter your readings:").split()))
             
enter your readings:3 4 5 6
[3, 4, 5, 6]
prices=tuple(map(int,input("enter your readings:").split()))
             
enter your readings:456 789 234
prices
             
(456, 789, 234)
rating=set(map(int,input("enter your readings:").split()))
             
enter your readings:3 4 5 6
rating
             
{3, 4, 5, 6}
percentage=list(map(float,input('enter your percentage:").split()))

             
SyntaxError: unterminated string literal (detected at line 1)
percentage=list(map(float,input("enter your percentage:").split()))
                                
enter your percentage:76 8.99 91.2
percentage
                                
[76.0, 8.99, 91.2]
prices=tuple(map(float,input("enter your prices:").split()))
                                
enter your prices:60.1 65 87
prices
                                
(60.1, 65.0, 87.0)
a,b=10,20
                                
a
                                
10
b
                                
20
a,b=[10,20]
                                
a
                                
10
b
                                
20
username,password=input("enter the username&password:").split()
                                
enter the username&password:revathi revs@123
username
                                
'revathi'
password
                                
'revs@123'
a,b,c,d=list(map,(int,input("enter the 4 sides:").split()))
                                
enter the 4 sides:4 5 6 7
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a,b,c,d=list(map,(int,input("enter the 4 sides:").split()))
TypeError: list expected at most 1 argument, got 2
a,b,c,d=list(map(int,input("enter the 4 sides:").split()))
                                
enter the 4 sides:4 5 6 7
a
                                
4
b
                                
5
c
                                
6
d
                                
7
prices,discount=list(map(float,input("enter the prices&discounts:").split()))
                                
enter the prices&discounts:3456 67 8
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    prices,discount=list(map(float,input("enter the prices&discounts:").split()))
ValueError: too many values to unpack (expected 2)
prices,discount=list(map(float,input("enter the prices&discounts:").split()))
                                
enter the prices&discounts:3456 8
price
                                
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'prices'?
prices
                                
3456.0
discount
                                
8.0
a=eval(input())
                                
34456
a
                                
34456
a=eval(input())
                                
4567.89
a
                                
4567.89
a=eval(input())
                                
(1,2,3)
a
                                
(1, 2, 3)
a=eval(input())
                                
{3:9,4:16}
a
                                
{3: 9, 4: 16}
a=eval(input())
                                
a
a
                                
{3: 9, 4: 16}
