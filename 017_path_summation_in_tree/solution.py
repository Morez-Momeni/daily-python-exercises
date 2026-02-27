class binTree:
    class treeNode:
        def __init__(self,data):
            self.key = data
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root = None
        self.size = 0
    def isEmpty(self):
        return self.root is None
    
    def treeSize(self):
        return self.size
    def insertNode(self,newNode):
        if self.isEmpty():
            self.root = newNode
            self.size += 1
        else:
            ptr = self.root
            while ptr:
                if newNode.key > ptr.key :
                    if ptr.right != None:
                        ptr = ptr.right 
                    else:
                        ptr.right = newNode
                        break
                else:
                    if ptr.left != None:
                        ptr = ptr.left 
                    else:
                        ptr.left = newNode
                        break
            self.size += 1
            
            