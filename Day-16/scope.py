#local scope
'''def display():
    n=10
    print("Inside:",n)#inside:10
display()
print("Outside:",n)#error
    
'''
#global scope
'''n=10
def display():
    n=10
    print("Inside:",n)#inside:10
display()
print("Outside:",n)
'''

'''#global keyword
def display():
    global n
    n=10
    print("Inside:",n)#inside:10
display()
print("Outside:",n)
'''

'''def display(n):
    #global n
    n+=10
    print("Inside:",n)#inside:10
n=10
display(n)
print("Outside:",n)
'''

#using nonlocal
'''def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer function:",n)
outer()
'''

#mutable are pass by reference
#immutable pass by value
#int
def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outside:",n)

#float
'''def update(n):
    n+=10
    print("Inside:",n)
n=10.5
update(n)
print("Outside:",n)
'''
#complex
'''def update(n):
    n+=10
    print("Inside:",n)
n=3+5j
update(n)
print("Outside:",n)
'''
#bool
'''def update(n):
    n=False
    print("Inside:",n)
n=True
update(n)
print("Outside:",n)
'''
#string
'''def update(n):
    n="python"
    n+="lang"
    print("Inside:",n)
n="python"
update(n)
print("Outside:",n)
'''
#list
'''def update(n):
    n.append(9)
    print("Inside:",n)
n=[1,2,3,4,5]
update(n)
print("Outside:",n)
'''
#tuple
'''def update(n):
    n+=(6,9)
    print("Inside:",n)
n=(1,2,3,4,5)
update(n)
print("Outside:",n)
'''
#set
'''def update(n):
    n.add(9)
    print("Inside:",n)
n={1,2,3,4,5}
update(n)
print("Outside:",n)
'''
#dict
def update(n):
    n[4]=8
    print("Inside:",n)
n={1:1,2:4,3:6}
update(n)
print("Outside:",n)



    
    
    

