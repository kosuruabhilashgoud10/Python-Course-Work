#syntax
'''
def func():
     if basecond1:
        return
     fumc()
'''
#to print 5,4,3,2,1
'''def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    #print(num,end=' ')
func(5)
'''
#to print 1,2,3,4,5
'''def func(num):
    if num==0:
        return
    #print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)
'''
#sum of n numbers
'''def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))
'''
#product of n numbers
'''def sumofdigits(n):
    if n==0:
        return 1
    return n*sumofdigits(n-1)
print(sumofdigits(5))
'''
#power
'''def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))
'''
#reverse of a string
def reverseofstr(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="Python Programming"
print(reverseofstr(l,len(l)-1))



    
                
    
