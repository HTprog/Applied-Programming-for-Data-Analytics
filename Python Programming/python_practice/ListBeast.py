list=[0,1,2,3,4]
list[0]=int(input("First number? "))
list[1]=int(input("Second number? "))
list[2]=int(input("Third number? "))
list[3]=int(input("Fourth number? "))
list[4]=int(input("Fifth number? "))
print("\nCurrent Selection:\n",list)

list.pop(list.index(int(input("Which number do you want removed? "))))
length=len(list)
total=sum(list)

print("\nData currently stored in the list:\n",list,
"\n\nThe number of items in the list is ",length,
"\n\nThe total of all values in the list is ",total,"\n\n")
