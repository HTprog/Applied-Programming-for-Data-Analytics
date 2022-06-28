from platform import node


class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    #Deletion cases:
    # 1. Node deleted is leaf node
    # 2. Node deleted only have 1 Child or no child
    # 3. Node deleted has 2 children - smallest value in the right subtree - use inorder

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

    # def postorder(tree):
    # if tree != None:
    #     postorder(tree.get_left_child())
    #     postorder(tree.get_right_child())
    #     print(tree.get_root_val())

    # def inorder(tree):
    #     if tree != None:
    #         inorder(tree.get_left_child())
    #         print(tree.get_root_val())
    #         inorder(tree.get_right_child())

root = BinarySearchTree(100)
root.insert(50)
root.insert(50)
root.insert(55)
root.insert(60)
root.insert(20)
root.insert(52)
root.insert(101)
root.insert(102)


root.PrintTree()
print("Preorder")
root.preorder()
print("inorder")
root.inorder()
print("postorder")
root.postorder()
root        