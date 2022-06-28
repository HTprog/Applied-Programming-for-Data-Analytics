# A Binary Tree Node
class Node:
# Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.countSimilar=1

def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.value,end=" ")
		inorder(root.right)

def PrintTree(root):
	if root.left:
		PrintTree(root.left)
	print(root.value)
	
	if root.right:
		PrintTree(root.right)

def PrintTreewithCount(root):
	if root.left:
		PrintTreewithCount(root.left)
	print(root.value,'-',root.countSimilar)
	
	if root.right:
		PrintTreewithCount(root.right)

def insert(node, value):

	if node is None:
		return Node(value)

	if value < node.value:
		node.left = insert(node.left, value)

	else:
		node.right = insert(node.right, value)

	return node

def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current


def deleteNode(root, value):

	# Base Case
	if root is None:
		return root

	# If the value to be deleted
	# is smaller than the root's
	# value then it lies in left subtree
	if value < root.value:
		root.left = deleteNode(root.left, value)

	# If the value to be delete
	# is greater than the root's value
	# then it lies in right subtree
	elif(value > root.value):
		root.right = deleteNode(root.right, value)

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
		temp = minValueNode(root.right)

		# Copy the inorder successor's
		# content to this node
		root.value = temp.value

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.value)

	return root



root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)


print("Print Tree")
PrintTreewithCount(root)