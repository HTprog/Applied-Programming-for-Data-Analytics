List_1=[1,2,3,4,5]

def multiplyrec(list,index=0,current=-1):
    current+=1
    if current+1==len(list):
        return *list[]
    return list[index]*multiplyrec(list,index+1,current)

print(multiplyrec(List_1))
    