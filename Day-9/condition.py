#simple if
s='python programming'
if 'python' in s:
    print('python found')


if s[0]=='p':
    print("string is starting with p")


#if-else
data=('abc','1234')
username,password=input("Enter the username and password:").split()
if data==(username,password):
    print("Login Successful")
else:
    print("invalid login")

    
#if-elif-else
n=int(input("Enter the number:"))

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("zero")

#Nested if
products={
    'laptop':0,
    'mouse':10,
    'charger':5,
    'phones':30,
    'keyboard':0
}
product=input("Enter the product:")
if product in products:
    if products[product]!=0:
        print(f"you can buy this {product}")
    else:
        print(f"{product} is out of stock")
else:
    print(f"{product} is not available")
    





        
