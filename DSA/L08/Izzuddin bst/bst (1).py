def search(self, value):
      if self.key == value:     #check if value is equal to the key val
        print("The node is present")
        return
      if value < self.key:    #Here left subtree can be empty or it can contain one or more nodes
        if self.leftchild:   #this condition is true if left subtree exists
            self.leftchild.search(value)
        else:
          print("The node is empty in the tree!")
      else:
        if self.rightchild:
            self.rightchild.search(value)   #search for all the values in the rightchild
            return true
        else:   
            print("The node is empty in the tree!")          #print out empty rightchild nodes in the tree