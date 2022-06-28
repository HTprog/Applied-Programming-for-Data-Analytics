z=0
Changetemp=True

while Changetemp:
    question=input("Increase?")
    if question=="Yes":
        z+=1
        print(z)
    elif question=="Quit":
        break

    else:
        print("Invalid input")
else:
    print("current z is",z)
    print("End of loop")
print("Here")