Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='  hello  world  '
s
'  hello  world  '
s.strip()
'hello  world'
s.rstrip()
'  hello  world'
s.lstrip()
'hello  world  '
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s,startswith('gfh')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s,startswith('gfh')
NameError: name 'startswith' is not defined
s.startswith('gfh')
False
s.endswith('py')
True
s.endswith('kj')
False
'sdfyul'.isaplpha()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    'sdfyul'.isaplpha()
AttributeError: 'str' object has no attribute 'isaplpha'. Did you mean: 'isalpha'?
'sdfghi'.isalpha()
True
'sgh123k'.isalpha()
False
'serhthu@123%'.isalpha()
False
'234567'.isnum()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    '234567'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
'2345667'.isalnum()
True
'12safg567'.isalnum()
True
'12345fgyy@uji'.isalnum()
False
'ewrhsty'.islower()
True
'ERhyju'.islower()
False
'EFJYNMK'.isupper()
True
'ADN6@THHY'.isupper()
True
''.isspace()
False
'hello        '.isspace()
False
'py prg lana'.istitle()
False
'Py Prg Lana'.istitle()
True
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
