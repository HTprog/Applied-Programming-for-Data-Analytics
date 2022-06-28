temp=0
change=True

while change:
    print("Current temp =",temp)
    question=input("\ninc or dec?").title()
    if question=="Inc":
        temp+=1
        
    elif question=="Dec":
        temp-=1
       
    elif question=="Quit":

        question2=input("Stop changing temperature and go to other features?").title()
        
        if question2=="Yes":
            import LED
            print("Go to feature blah")
            change=False
        
        elif question2=="No":
            change=True

    else:
        print("\nInvalid input")
        

print("\nCurrent temperature =",temp)   #I guess the user choose to goto other features here. 
print("\nEnd of loop")          #If not it loops back to the begginning