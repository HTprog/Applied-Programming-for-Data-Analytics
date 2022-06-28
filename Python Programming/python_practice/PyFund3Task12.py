password=input("Enter a password: ")
upper=0

for i in range(0,len(password)):
    if password[i].isupper():
        upper=upper+1

if upper>1:
    print("Password Accepted!")
else:
    print("Password Denied!")