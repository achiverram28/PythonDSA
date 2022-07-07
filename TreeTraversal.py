class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
    def insert(self,item):
        if self.item:
            if item<self.item:
                if self.left is None:
                    self.left=Node(item)
                else:
                    self.left.insert(item)
            elif item>self.item:
                if self.right is None:
                    self.right=Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item=item
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.item)
        if self.right:
            self.right.PrintTree()
    def inorder(self,root):
        res=[]
        if root:
            res=self.inorder(root.left)
            res.append(root.item)
            res=res+self.inorder(root.right)
        return res    
    def preorder(self,root):
        res=[]
        if root:
            res.append(root.item)
            res=res+self.preorder(root.left)
            res=res+self.preorder(root.right)
        return res    
    def postorder(self,root):
        res=[]
        if root:
            res=self.postorder(root.left)
            res=res+self.postorder(root.right)
            res.append(root.item)
        return res    
root=Node(12)
root.insert(6)
root.insert(14)
root.PrintTree()
print("Inorder traversal is {}".format(root.inorder(root)))
print("Preorder traversal is {}".format(root.preorder(root)))
print("Postorder traversal is {}".format(root.postorder(root)))
