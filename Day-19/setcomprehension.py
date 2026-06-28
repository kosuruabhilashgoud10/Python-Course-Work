#set comprehensions
'''s=set()
for i in range(1,11):
    s.add(i)
#using list comprehension
s1={i for i in range(1,11)}
print(s)
print(s1)
'''
#dict comprehension
'''d={}
for i in range(1,11):
    d[i]=i*i
print(d)
#dict comp
res={i:i*i for i in range(1,11)}
print(res)
'''
'''res={input("Enter the name:"):int(input("Enter the mark:"))
     for i in range(5)}
print(res)
'''
#generators
def display():
    l=['1..50','51..100','101..150','151..200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
scroll=display()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))




    


