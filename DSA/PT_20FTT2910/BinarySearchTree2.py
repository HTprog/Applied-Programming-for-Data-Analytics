class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

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

    def minValueNode(self):
        current = self

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current


    def deleteNode(self, value):

        root = self
        # Base Case
        if root is None:
            return root

        # If the value to be deleted
        # is smaller than the root's
        # value then it lies in left subtree
        if value < root.value:
            root.left = root.left.deleteNode(value)

        # If the value to be delete
        # is greater than the root's value
        # then it lies in right subtree
        elif(value > root.value):
            root.right = root.right.deleteNode(value)

        # If value is same as root's value, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = root.right.minValueNode()

            # Copy the inorder successor's
            # content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = root.right.deleteNode(temp.value)

        return root

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value)
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

    

root = BinarySearchTree(100)
root.insert(50)
root.insert(20)
root.insert(55)
root.insert(53)
root.insert(115)
root.insert(105)
root.insert(200)
root.insert(119)
root.insert(220)
root.insert(1)
root.insert(7)

root.PrintTree()

root.deleteNode(100)
print("After Delete:")
root.PrintTree()
     
