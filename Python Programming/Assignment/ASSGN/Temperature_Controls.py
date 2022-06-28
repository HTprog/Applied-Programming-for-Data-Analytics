def controltemp(currenttemp):
    changetemp = True
    temp=currenttemp
    while changetemp:
        print("\nCurrent temp =", temp)
        #'inc' means increase temperature by 1 #'dec'means decrease temperature by 1
        question = input("\nincrease or decrease temperature?\nType 'inc'to increase.\
            \nType 'dec' to decrease.\nType 'quit' to return to homepage.\n\n").lower()

        if question=="inc":                     
            temp+=1
            print("\n\nNew temperature =",temp,"\n**Filtering the odor to keep the food fresh.**\n") 

        elif question=="dec":
            temp-=1
            print("\nNew temperature =",temp,"\n**Reduce the time of opening door, to keep food fresh and remove odor.**\n")

        #if the user types quit he could either save current temperature and return to home screen or continue changing temp
        elif question=="quit": 
            question2=input("Save current temperature and return to home screen?(yes/no)\n").lower()
            if question2=="yes": 
                return temp 

            elif question2=="no":
                continue #When 'no'is answered the loop continues
            
            else:
                print("Invalid input")

        else:
            print("\nInvalid input")




