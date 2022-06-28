day=int(input("Please enter the date(dd) "))
month=int(input("Please enter the month(mm) "))
if day==25 and month==12:
    print("Hooray! It's Christmast Day!")
elif day<25 and month==12:
    print("Christmast is just around the corner!")
else:
    print("You've still got a while to go until Christmast")
