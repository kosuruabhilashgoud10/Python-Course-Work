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
    print("You can go for park")
else:
    print("take rest")
