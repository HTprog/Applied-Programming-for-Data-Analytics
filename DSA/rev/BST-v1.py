class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.divisible=False

    def insert(self, child):

        if self.value:
            if child < self.value: #value less than the parent
                if self.left is None:
                    self.left = BinarySearchTree(child)
                else:
                    self.left.insert(child)
            elif child > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(child)
                else:
                    self.right.insert(child)
        else:
            self.value = child

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.value)

        if self.right:
            self.right.inorder()

    def PrintTreeDiv(self):
        if self.left:
            self.left.PrintTreeDiv()
        print( self.value,'-',self.divisible),
        if self.right:
            self.right.PrintTreeDiv()

    def insertDiv(self, child):

        if self.value:
            if child%5==0 or child%3==0:
                self.divisible=True
            
            if child < self.value: #value less than the parent
                if self.left is None:
                    self.left = BinarySearchTree(child)

                else:
                    self.left.insertDiv(child)

            elif child > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(child)
                else: 
                    self.right.insertDiv(child)
        else:
            self.value = child
            self.divisible=True





root = BinarySearchTree(100)
# root.insert(50)
# root.insert(20)
# root.insert(55)
# root.insert(53)
# root.insert(115)
# root.insert(105)
# root.insert(200)
# root.insert(119)
# root.insert(220)

root.insertDiv(50)
root.insertDiv(20)
root.insertDiv(55)
root.insertDiv(53)
root.insertDiv(115)
root.insertDiv(105)
root.insertDiv(200)
root.insertDiv(119)
root.insertDiv(220)



# root.PrintTree()
# print("Preorder")
# root.preorder()
# print("inorder")
# root.inorder()
# print("postorder")
# root.postorder()
# root        
root.PrintTreeDiv()