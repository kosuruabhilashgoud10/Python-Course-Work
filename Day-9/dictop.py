Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d=dict()
d
{}
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[2]='float'
d
{1: 'int', 2: 'float'}
d[3]='revathi'
d
{1: 'int', 2: 'float', 3: 'revathi'}
d[4]='3+2j'
d
{1: 'int', 2: 'float', 3: 'revathi', 4: '3+2j'}
d['demo']='str'
d
{1: 'int', 2: 'float', 3: 'revathi', 4: '3+2j', 'demo': 'str'}
d[2+3j]='complex
SyntaxError: unterminated string literal (detected at line 1)
d['2+3j']='complex'
d
{1: 'int', 2: 'float', 3: 'revathi', 4: '3+2j', 'demo': 'str', '2+3j': 'complex'}
d[(1,2,3)]='tuple'
d
{1: 'int', 2: 'float', 3: 'revathi', 4: '3+2j', 'demo': 'str', '2+3j': 'complex', (1, 2, 3): 'tuple'}
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
d[{1,2,3}]='str'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d[{1,2,3}]='str'
TypeError: unhashable type: 'set'
d[False]='bool'
d
{1: 'int', 2: 'float', 3: 'revathi', 4: '3+2j', 'demo': 'str', '2+3j': 'complex', (1, 2, 3): 'tuple', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[2]=23.4
d[3]='fgthhy'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,2,3}
d[8]={1:2,2:2}
d[9]=False
d
{1: 1, 2: 23.4, 3: 'fgthhy', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 2}, 9: False}
d={}
d
{}
d[1]=1

d[2]=2
d[3]=2
d[4]=2
d
{1: 1, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'revathi':78,'aishu':89,'usha':80}
d
{'revathi': 78, 'aishu': 89, 'usha': 80}
d['aishu']
89
d['revathi']
78
d['usha']
80
d['harika']
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d['harika']
KeyError: 'harika'
 d.get('harika)
       
SyntaxError: unexpected indent
d.get('harika')
       
d.get('aishu')
       
89
d.get('harika','user not found')
       
'user not found'
d.get('revathi','user not found')
       
78
'revathi' in d
       
True
'aishu' in d
       
True
'harika' in d
       
False
'revathi'not in d
       
False
d.values()
       
dict_values([78, 89, 80])
d.items()
       
dict_items([('revathi', 78), ('aishu', 89), ('usha', 80)])
d.sorted()
       
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.sorted()
AttributeError: 'dict' object has no attribute 'sorted'
sorted(d)
       
['aishu', 'revathi', 'usha']
max(d)
       
'usha'
min(d)
       
'aishu'
len(d)
       
3
d['aishu']
       
89
d['aishu']=100
       
d
       
{'revathi': 78, 'aishu': 100, 'usha': 80}
d['revathi']=89
       
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80}
d.upadte({'harika':50,'subha'=69})
       
SyntaxError: ':' expected after dictionary key
d.update({'harika':50,'subha':56})
       
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50, 'subha': 56}
d.popitem()
       
('subha', 56)
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50}
d.popitem()
       
('harika', 50)
d.popitem()
       
('usha', 80)
d
       
{'revathi': 89, 'aishu': 100}
d.pop('aishu')
       
100
d
       
{'revathi': 89}
del d['revathi']
       
d
       
{}
d.clear()
       
d
       
{}
d={'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50, 'subha': 56}
       
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50, 'subha': 56}
d.setdefault('maha',0)
       
0
d.setdefault('revathi',0)
       
89
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50, 'subha': 56, 'maha': 0}
d.get('abhi',0)
       
0
d
       
{'revathi': 89, 'aishu': 100, 'usha': 80, 'harika': 50, 'subha': 56, 'maha': 0}



