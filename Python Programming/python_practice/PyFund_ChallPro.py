salary=int(input("What is your annual salary? "))
mortgage=salary*4
price=int(input("What is the house price?"))
if mortgage>=price:
    print("You can afford the price")
    deposit=input("Do you have a deposit to put towards the house?").title()
    if deposit=="Yes":
        print("you can pay the rest of the house price now")
    else:
        print("You can pay the full house price ")
else:
    print("You can't afford the house")