class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
    if root is None:
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    return max(leftAns, rightAns) + 1
 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(40)
 
print("Height of the binary tree is: " + str(height(root)))