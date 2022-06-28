import Node
class UnorderedList:

    def __init__(self):
        self.head = None    

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node.Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

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
        previous= None
        while current != None:
            if current.get_data() == None:
                found = True
            else:
                check.insert(0, current.get_data())
                current = current.get_next()
        return print(check)


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)    
print(mylist.search(17))    
#print(mylist.list())