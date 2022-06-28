import Node
class UnorderedList:

    def __init__(self):
        self.head = None    


    def is_empty(self):
        return self.head == None

    def add(self, item):    
        current = self.head
        previous= None
        kill=False
        while current != None and not kill:
            if current.get_data() > item:
                kill=True
            else:
                previous=current
                current=current.get_next()

        temp = Node.Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
    def search(self,item):
        current = self.head
        found = False
        previous= None
        while current != None and not found:
            if current.get_data() == None:
                break

            elif current.get_data() == item:
                found=True
            else:
                if current.get_data() > item:
                    break
                else:
                    current = current.get_next()
        return print(found)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def list(self):
        check=[]
        current = self.head
        while current != None:
            if current.get_data() == None:
                return print('New list =',check)
            else:
                check.append(current.get_data())
                current = current.get_next()
        return print('New list =',check)

    def SearchPosition(self,item):
        current = self.head
        found = False
        iterations=0
        previous= None
        while current != None and not found:
            iterations=iterations+1
            if current.get_data() == None:
                return print(item,'is not found after',iterations,'iterations')

            elif current.get_data() == item:
                return print(item,'is found after',iterations,'iterations')
            else:
                if current.get_data() > item:
                    return print(item,'is not found after',iterations,'iterations')
                else:
                    current = current.get_next()
        return print(item,'is not found after',iterations,'iterations')




mylist = UnorderedList()
mylist.add(60)
mylist.add(40)
mylist.add(37)
mylist.add(24)
mylist.add(23)
mylist.add(22) 
mylist.add(50) 
mylist.list()
mylist.search(38)
mylist.SearchPosition(38)
mylist.search(23)
mylist.SearchPosition(23) 