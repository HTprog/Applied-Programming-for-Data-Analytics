
Run=True
confirm1=True
confirm2=True

def calculate(a,b):
     c=float((a**2+b**2)**0.5)
     print("\nHypotenuse(c) of the triangle=",c)

while Run:
    a=0
    b=0
    c=0
    print("\na=height of triangle\
           \nb=base of triangle\
           \nc=hypotenuse")

    a=float(input("\nPlease enter the height of the triangle= "))
    b=float(input("\nPlease enter the base of the triangle= "))
    calculate(a,b)
    
    while confirm1:
        question=input("\nRe-enter values?(yes/no) ").lower()
        if question=="yes":
            break
        
        elif question=="no":
            while confirm2:
                question2=input("\nConfirm end program?(yes/no) ").lower()
                if question2=="yes":
                    Run=False
                    confirm1=False
                    break

                elif question2=="no":
                    confirm1=True
                    break

                else:
                    print("\nPlease enter either (yes/no)")
                    confirm2=True
        else:
            print("\nPlease enter either (yes/no)")
            confirm1=True
print("\nprogram ended")



