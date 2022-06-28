hero="Neymar".lower()
attempt=1
questioning=True
while questioning:
    question=str(input("Please guess my sporting hero\n")).lower()
    if question==hero:
        print("You are correct!")
        questioning=False

    elif question=="quit":
        break

    else:
        #match=question in hero
        noofmatch=0
        for i in range(len(question)):
            match=question[i] in hero[i]
            if match==True:
                noofmatch+=1

        print("You are incorrect but",noofmatch,"letters in your guess match the answer.")
        if attempt<len(hero):
            for i in range(attempt):
                print("Here is letter",str(i+1),"from the answer=",hero[i])
            attempt=attempt+1
            questioning=True

        elif attempt==len(hero):
            print("The answer is "+hero+". Please try again.")
            questioning=True

        else:
            print("You are incorrect, guess again")
            questioning==True
else:
    print("end of loop")
