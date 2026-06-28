#syntax
'''
def function_name(arg):
      #stmts
      return
function_name
'''
#example
'''def wish(name):
    print(f'welcome to python course {name}!')
wish("revathi")
wish("abhi")
wish("aishu")
'''
#to print even or odd

'''def iseven(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-odd number"
print(iseven(12))
print(iseven(13))
'''
#to print factorial
'''def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number:"))
print("Factorial:",factorial(num))
'''
#to print prime or not
'''def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not Prime Number"
    return f"{num}-Prime Number"
num=int(input("Enter the number:"))
print(isprime(num))
'''
#positional arguments
'''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display('revathi','revathi123@gmail.com','revs@123')
display('revathi123@gmail.com','revs@123','revathi')
display('revs@123','revathi','revathi123@gmail.com')
'''
#key word arguments
'''def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display(name='revathi',email='revathi123@gmail.com',pwd='revs@123')
display(email='revathi123@gmail.com',pwd='revs@123',name='revathi')
display(pwd='revs@123',name='revathi',email='revathi123@gmail.com')
'''
#default arguments
'''def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display('revathi','revathi123@gmail.com','revs@123')
display('revathi','revathi123@gmail.com')
'''
#variable arguments
def display(*names):
    print("Names:",names)
    
display('revathi','aishu','usha','harika')
display('revathi','aishu')
display('revathi','aishu','usha')

#keyword variables
def display(**names):
    print("Names:",names)
    
display(k1='revathi',k2='aishu',k3='usha')
display(k1='revathi')
display(k1='revathi',k2='aishu',k3='usha')



    
        


    
