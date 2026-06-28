#list comprehension
#---syntax---
#l=[val for var in seq

#to print 1 t0 11
'''res1=[]
for i in range(1,11):
    res1.append(i)
#using list comprehension
res2=[i for i in range (1,11)]
print(res1)
print(res2)
'''
#to print 3 multiples
'''res3=[]
for i in range(3,31,3):
    res3.append(i)
#using list comp
res4=[i for i in range(3,31,3)]
print(res3)
print(res4)
'''
#to print even
'''res5=[]
for i in range(2,51,2):
    res5.append(i)
res6=[i for i in range(2,51,2)]
print(res5)
print(res6)
'''
#list comprehension using if
#----syntax---
#l=[val for var in seq if condition

'''a='Python Programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)
#using list comprehension
l1=[i for i in a if i in 'aeiouAEIOU']
print(l1)
'''
#list comprehension using if-else
#---syntax---
#l=[val if condition else val for var in seq]
'''a=[1,2,3,4,5,6,7,10,11,13,14,15,16,45,67,80]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)
#using list comprehension
l1=[i if i%2==0 else 0 for i in a]
print(l1)
'''
#to take 10 numbers from user
'''l=[int(input(f"Enter the number-{i+1}:")) for i in range(10)]
print(l)'''
#nested loops
'''l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)
#using list comprehension
l1=[j for i in range(3)for j in range(1,4)]
print(l1)
'''
'''l=[[j for j in range(1,4)] for i in range(3)]
print(l)
'''


    






