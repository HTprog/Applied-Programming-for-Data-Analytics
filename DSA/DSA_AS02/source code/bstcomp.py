class binary_tree:
    def __init__(self, key):  
        self.leftchild = None 
        self.rightchild = None 
        self.key = key

#add
    def insert(self, value): 
        if self.key is None:
            self.key = data 
            return
        if self.key == value:   
            return              
        if value < self.key:  
            if self.leftchild:
                self.leftchild.add(value) 
            else:   
                self.leftchild = binary_tree(value)
        else:   
            if self.rightchild:    
                self.rightchild.add(value)  
            else:
                self.rightchild = binary_tree(value) 

    #search
    def search(self, value):
        if self.key == value:     
            print("The node is present")
            return
        if value < self.key:    
            if self.leftchild:   
                self.leftchild.search(value)
            else:
                print("The node is empty in the tree!")

        else:
            if self.rightchild:
                self.rightchild.search(value)   
                return true
            else:   
                print("The node is empty in the tree!")         

#inordertraversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 

#getHeight
def height(root):
    if root is None:
        
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
    return max(leftAns, rightAns) + 1
    
print("Height of the binary tree is: " + str(height(root)))

#getparent

def getParent(node : Node,
               val : int,
               parent : int) -> None:
    if (node is None):
        return
    if (node.data == val):
        print(parent)
    else:
        getParent(node.left,
                   val, node.data)
        getParent(node.right,
                   val, node.data)
                
#getchild
def numberOfChildren( root, x):
 
 
    numChildren = 0
 
    if (root == None):
        return 0
 
 
    q = []
    q.append(root)
 
    while (len(q) > 0) :
        n = len(q)
 
   
        while (n > 0):
 
       
            p = q[0]
            q.pop(0)
            if (p.key == x) :
                numChildren = numChildren + len(p.child)
                return numChildren
             
            i = 0
             
         
            while ( i < len(p.child)):
                q.append(p.child[i])
                i = i + 1
            n = n - 1
 
    return numChildren
    
#delete

