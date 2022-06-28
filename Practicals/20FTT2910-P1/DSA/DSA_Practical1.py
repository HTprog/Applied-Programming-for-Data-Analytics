#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS

def gcd(a,b):
    DivisorA=[]
    DivisorB=[]
    ComDiv=[]

    for i in range(1,a+1):
        A=a%i
        if A==0:
            DivisorA.append(i)
        else:
            continue
    DivisorA.sort()
    print('The divisors of',a,'=',DivisorA)

    for i in range(1,b+1):
        B=b%i
        if B==0:
            DivisorB.append(i)
        else:
            continue
    DivisorB.sort()
    print('The divisors of',b,'=',DivisorB)

    for i in DivisorA:
        for y in DivisorB:
            if i==y:
                ComDiv.append(y)
    ComDiv=list(dict.fromkeys(ComDiv))
    print('The common divisors of',a,'&',b,'=',ComDiv)

    gcd=1
    for i in ComDiv:
        if gcd<i:
            gcd=i
    print('gcd =',gcd)

gcd(100,150)

