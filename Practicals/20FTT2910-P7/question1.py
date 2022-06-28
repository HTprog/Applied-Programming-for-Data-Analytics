from requests import delete


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

        print(self.value,end=" ")

        if self.right:
            self.right.inorder()
    
    def search(self,item):
        if self.value==item:
            return print(True)
        
        if self.value>item:
            if self.left:
                return self.left.search(item)

            else:
                return print(False)
        
        else:
            if self.right:
                return self.right.search(item)

            else:
                return print(False)

        return print(False)
            

    def minValueNode(node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    def maxValueNode(node):
        current = node

        # loop down to find the leftmost leaf
        while(current.right is not None):
            current = current.right

        return current

    def delete(self,value):

        # Base Case
        if self is None:
            return self

        # If the value to be deleted
        # is smaller than the root's
        # value then it lies in left subtree
        if value < self.value:
            self.left.delete(value)

        # If the value to be delete
        # is greater than the root's value
        # then it lies in right subtree
        elif(value > self.value):
            self.right.delete(value)

        # If value is same as root's value, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp=self.right.minValueNode()

            # Copy the inorder successor's
            # content to this node
            self.value = temp.value

            # Delete the inorder successor
            self.right = delete(self.right, temp.value)

        return self

root = BinarySearchTree(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)
root.inorder()

print('\npart B')
root.search(30)
root.search(90)

print('\npart C')
root.delete(20)
root.inorder()

print('\npart D')
print((root.minValueNode()).value)

print('\npart E')
print((root.maxValueNode()).value)

print('\npart F')
# root.PrintTree()
# print("Preorder")
# root.preorder()
#print("inorder")
#root.inorder()
# print("postorder")
# root.postorder()
# root        