print('Please enter your scores:')
scores=input()
scoreslist=scores.rsplit(',')

for item in scoreslist:
    TestScore=int(item)
    if TestScore>90:
        print('Your Grade is A')
    elif TestScore>80:
        print('Your Grade is B')
    elif TestScore>70:
        print('Your Grade is C')
    elif TestScore>60:
        print('Your Grade is D')
    else:
        print('Your Grade is F')    