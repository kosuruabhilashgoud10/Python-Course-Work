data={
    'aishu':{'status':True,'python':98,'mysql':95,'flask':94},
    'revathi':{'status':True,'python':88,'mysql':55,'flask':74},
    'usha':{'status':True,'python':78,'mysql':75,'flask':84},
    'abhi':{'status':False,'python':None,'mysql':None,'flask':None},
    'harika':{'status':True,'python':13,'mysql':25,'flask':24},
    }
    
name=input("Enter the name:")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg>90:
            print(f"congrats {name},you got first class!!!")
        elif avg>70:
            print(f"good {name},keep it up!!!")
        elif avg>35:
            print(f'better {name},work hard next time!')
        else:
            print(f"{name},you have failed the exam.Bring your parents")
    else:
        print(f'{name} did not write the exam.Bring your parents')
            
else:
    print(f"{name}'s data not found")
#budget
budget=int(input("Enter the budget:"))
if budget>50000:
    print("You can go for trip")

elif budget>30000:
    print("You can go for shopping")

elif budget>10000:
    print("You can go for pub")

elif budget>5000:
    print("You can go for cafe")

elif budget>3000:
    print("You can go for movie")
    
elif budget>2000:
    print("You can go for trip")
else:
    print("take rest")


    
           
           
