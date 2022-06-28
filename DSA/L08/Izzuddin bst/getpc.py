def findParent(node : Node,
               val : int,
               parent : int) -> None:
    if (node is None):
        return
 
    # If current node is
    # the required node
    if (node.data == val):
       
        # Print its parent
        print(parent)
    else:
       
        # Recursive calls
        # for the children
        # of the current node
        # Current node is now
        # the new parent
        findParent(node.left,
                   val, node.data)
        findParent(node.right,
                   val, node.data)
                
#getchild
def numberOfChildren( root, x):
 
    # initialize the numChildren as 0
    numChildren = 0
 
    if (root == None):
        return 0
 
    # Creating a queue and appending the root
    q = []
    q.append(root)
 
    while (len(q) > 0) :
        n = len(q)
 
        # If this node has children
        while (n > 0):
 
            # Dequeue an item from queue and
            # check if it is equal to x
            # If YES, then return number of children
            p = q[0]
            q.pop(0)
            if (p.key == x) :
                numChildren = numChildren + len(p.child)
                return numChildren
             
            i = 0
             
            # Enqueue all children of the dequeued item
            while ( i < len(p.child)):
                q.append(p.child[i])
                i = i + 1
            n = n - 1
 
    return numChildren