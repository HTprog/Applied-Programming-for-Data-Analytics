pw=input("Please input a password between 6-12 characters long: ")
lenpw=len(pw)
if lenpw < 6:
    print("Your password is too short!.")
elif lenpw > 12 :
    print("Your password is too long!.")
else:
    print("Password accepted.")
