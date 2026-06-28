#syntax-lambda
'''var=lambda arg:exp'''
'''add=lambda a,b:a+b
print(add(12,13))
print(add(15,13))
'''
#example
'''wish=lambda name: f" Welcome to the python course {name}"
print(wish('revathi'))
'''
#to print GST
'''gst=lambda price: price+price*0.18
print(gst(1000))
print(gst(600))
print(gst(1800))
'''
# greatest
'''greatest=lambda a,b:a if a>b else b
print(greatest(18,19))
print(greatest(20,5))
print(greatest(2,1))
'''
#conditional statements
#even or odd
'''iseven=lambda a:f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(9))
print(iseven(10))
'''
#delivery charges
'''bill=lambda charge: charge if charge>99 else charge+30
print(bill(1300))
print(bill(88))
print(bill(15))
'''
#sales -nested if
'''login=True
instock=True
status=lambda login,instock:("You can buy product" if instock else "product is out of stock") if login else "login to buy a product"
print(status(login,instock))
'''
#loops
'''l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)'''
#title
'''names=['aishu','revathi','usha']
t=list(map(lambda i:i.title(),names))
print(t)
'''
#filter
'''l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%2==0,l))
print(res)
'''

l=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda i:i>5,l))
print(res)

'''l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%3==0,l))
print(res)
'''
#function
'''from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p)
'''
'''from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda max,i:max if max<i else i,l)
print(s,p,m,mi)
'''
d={'aishu':80,'revathi':40,'usha':60,'abhi':92}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))







