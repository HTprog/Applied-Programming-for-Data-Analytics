def calculate(a, b, c):
    list=[a,b,c]
    list.sort()
    place1=len(list)/2
    place2=int(place1)
    print("Median=",list[place2])
    
    #if isinstance(place,float):
        #location=int(place)
        #print("Median= ",list[location])
    #else:
        #median=float(((list[place])+(list[place+1]))/2)
        #print("Median=",median)

run=True
while run:
    question=input("State the 3 values: ")
    answer=question.split()
    
    if len(answer)<3:
        print("Please enter 3 values.")
        continue
    elif len(answer)>3:
        print("Please enter only 3 values.")
    elif len(answer)==3:
        calculate(answer[0],answer[1],answer[2])
        continue
    else:
        print("Invalid output")
        continue
