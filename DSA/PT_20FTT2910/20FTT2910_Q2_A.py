List1=[8,7,12,4]
List2=[8,5,2,12]

def multiply(list1,list2):
    newlist=[]
    if len(list1)!=len(list2):#QAPART4
        return print('ERROR lists are not of same size')
    count=0
    while count!=len(list1):
        item1=list1.pop(0)
        item2=list2.pop(0)
        if item1>item2: #QAPART1
            newlist.append(item1*item2)
        elif item1<item2:#QAPART2
            newlist.append(item1+item2)
        else:#QAPART3
            newlist.append(0)
    print(newlist)
    return    

multiply(List1,List2)
