import Node
class unsorted_DCLL:

    def __init__(self):
        self.head = None    
        self.tail = None
        self.limit= 0
        self.len=0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        if self.len<self.limit:
            self.len+=1
        elif self.limit==0:
            self.len+=1
        else:
            print('\nSize limit reached')
            return

        temp = Node.Node(item)
        if self.head==None:
            self.head=temp
            self.tail=temp
            temp.set_next(self.head)
            temp.set_prev(self.tail)
            self.tail.set_next(temp) #or self.head
            self.head.set_prev(temp)

        else:

            temp.set_next(self.head)
            temp.set_prev(self.tail)  
            self.head.set_prev(temp)
            self.tail.set_next(temp)
            self.head=temp


    def delete(self,item):
        current = self.head
        previous = self.tail
        found = False
        while not found:
            if current.get_data() == item:
                found = True

            elif current.get_next()==self.head:
                if current.get_data()==item:
                    break
                else:
                    print('\nItem not found')
                    return
            else:
                previous = current
                current = current.get_next()
                
        previous.set_next(current.get_next())
        current.set_prev(previous)
            

    def deleteall(self,item):

        current = self.head
        previous= self.tail
        while current.get_next()!=self.head:
            if current.get_data() == item:
                if current.get_prev()==self.tail:
                    self.head=current.get_next()
                    self.tail.set_next(self.head)
                    current=current.get_next()
                    
                else:
                    previous.set_next(current.get_next())
                    current=current.get_next()
            else:
                previous=current
                current = current.get_next()
        if current.get_data() == item:
            previous.set_next(current.get_next())
            print('\ndelete all item '+"'"+str(item)+"'"+' finished')
        else:
            print('\ndelete all item '+"'"+str(item)+"'"+' finished')

    def deletebyindex(self,index):
        current=self.head
        previous=self.tail
        pos=1
        if index>self.len:
            print('\nIndex',index,'does not exist')
            return
        else:
            while pos!=index:
                pos=pos+1
                previous=current
                current=current.get_next()
            if current==self.head:
                self.head=current.get_next()
                self.tail.set_next(self.head)
            else:
                previous.set_next(current.get_next())
                current.set_prev(previous)
            
    def addtofront(self,item):
        if self.len<self.limit:
            self.len+=1
        elif self.limit==0:
            self.len+=1
        else:
            print('\nSize limit reached')
            return
        current=self.head
        previous=self.tail

        temp=Node.Node(item)
        
        previous.set_next(temp)
        temp.set_prev(previous)
        temp.set_next(current)
        current.set_prev(temp)

        self.tail=previous.get_next()
        

    def search(self,item):
        current=self.head
        previous=self.tail
        while current.get_next()!=self.head:
            if current.get_data()==item:
                print('')
                return print(True)
            else:
                previous=current
                current=current.get_next()
        if current.get_data()==item:
            print('')
            return print(True)
        else:
            return print(False)

    def searchindex(self,item):
        current=self.head
        previous=self.tail
        index=1
        while current.get_next()!=self.head:

            if current.get_data()==item:
                print('')
                return print(item,'is found at index',index)
            else:
                index=index+1
                previous=current
                current=current.get_next()
        if current.get_data()==item:
            print('')
            return print(item,'is found at index',index)
        else:
            return print('Item not found')

    def searchbyindex(self,index):
        current=self.head
        previous=self.tail
        pos=0
        if index>self.len:
            print('\nIndex',index,'does not exist')
            return
        else:
            while current.get_next()!=self.head:
                pos=pos+1
                if pos==index:
                    return print(current.get_data(),'was found at position',pos)
                else:
                    previous=current
                    current=current.get_next()
            pos=pos+1
            if pos==index:
                print(current.get_data(),'was found at position',pos)
            else:
                return print('Index is not found')


    def size(self):
        return print('\nSize=',self.len)

    def sizelimit(self):
        return print('\nSizelimit=',self.limit)

    def setsizelimit(self,number=10):
        self.limit=number

    def checkends(self):
        head=self.head
        tail=self.tail
        print('Head=',head.get_data())
        print('Tail=',tail.get_data())

    def PrintList(self):
        temp = self.head
        if temp != None:
            print("\nThe list contains:", end=" ")
            while True:
                print(temp.get_data(), end=" ")
                temp = temp.get_next()
                if temp == self.head:
                    break
                    
        else:
            print("The list is empty.")


mylist = unsorted_DCLL()
mylist.setsizelimit()#sets default size limit 10
mylist.sizelimit()#returns size limit 
mylist.add(80)
mylist.add(50)
mylist.add(40)
mylist.add(60)
mylist.addtofront(24)
mylist.addtofront(26)
mylist.addtofront(28)

# #these items will not be added because of sizelimit
mylist.add(30)
mylist.add(50)
mylist.add(10)
mylist.add(60)
mylist.add(10)

# mylist.PrintList()#prints all items within the list
# mylist.size()#returns current size of the list

# mylist.delete(60)#deletes value 60 from the list
# mylist.PrintList()

mylist.deleteall(10)#delete all values equal to 10 from the list
mylist.PrintList()

# mylist.deletebyindex(3)#delete the value at index 3
# mylist.PrintList()

# mylist.search(50)#returns true if item 50 is found
# mylist.searchindex(26)#Finds and returns 26 if found in the list
# mylist.searchbyindex(4)#Returns value at index 4

# mylist.PrintList()


# mylist.add(30)
# mylist.add(50)
# mylist.add(10)
# mylist.add(60)
# mylist.add(10)

