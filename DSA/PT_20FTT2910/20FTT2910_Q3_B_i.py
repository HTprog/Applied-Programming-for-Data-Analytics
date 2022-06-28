List_1=[1,2,3,4,5]
# for i in List_1:
#     current=i
#     nextindex=List_1.index(i)+1
#     out=i*List_1[nextindex]
output=0
for i in range(0,len(List_1),1):
    current=i
    next=i+1
    if i==len(List_1)-1:
        break
    else:
        # item1=List_1.pop(current)
        # item2=List_1.pop(next)
        # output=output+(item1*item2)
        output=output+(List_1[current]*List_1[next])
print(output)