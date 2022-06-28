def calculate(kilometers):
    meters=kilometers*10**3
    extra=int(meters/140)
    fare=float(4.0+(0.25*extra))
    total="$"+'{:.2f}'.format(fare)
    print("Total Fare=",total)

question=float(input("Distance travelled in kilometers? "))
calculate(question)
