#Question 2 part ii
def count(input):
    count=0
    Alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    text=input
    for i in text:
        if i in Alpha:
            count+=1

    return print(count)


List=['A',2,'D','H']

count(List)