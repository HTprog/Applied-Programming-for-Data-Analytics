
#Question 2 part i
def maxnum(list):
    count=0
    max=0 
    for i in list:
        count+=1
        if i>max:
            max=i
            mark=count
    print('max value is',max,'index is',mark)


list=[1,4,2,6,4,10]

maxnum(list)


