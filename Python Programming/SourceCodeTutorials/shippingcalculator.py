
def calculate(items):
    cost=float(((items-1)*2.95)+10.95)
    charge="$"+str('{0:.2f}'.format(cost))
    print("Shipping Charge= ",charge)

question=int(input("Number of items in order? "))
calculate(question)