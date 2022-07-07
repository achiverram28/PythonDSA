##Very Basic Informative Code about Trees in Python
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
root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
                    
                
            
    
