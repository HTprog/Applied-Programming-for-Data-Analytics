password=input("Please input a valid pasword(6-12 characters)")
passlen=len(password)
if passlen<6 or passlen>12:
    print("Invalid password")
else:
    print("Password accepted")
