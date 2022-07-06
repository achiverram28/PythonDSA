###FIRST IMPLEMENTATION OF LINKED LIST###
class Node:##Node creation
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedList:##List Operations
    def __init__(self):
        self.headval=None
    def display(self):##Display the list
        curr=self.headval
        while curr is not None:
            print(curr.dataval)
            curr=curr.next
    def pushFront(self,item):##Insert element at the front
        NewNode=Node(item)
        NewNode.next=self.headval
        self.headval=NewNode
    def pushLast(self,item):##Insert element at the last
        NewNode=Node(item)
        curr=self.headval
        while curr.next is not None:
            curr=curr.next
        curr.next=NewNode
        NewNode.next=None
    def pushMiddle(self,item,pos):##Insert element in the Middle at a given position
        NewNode=Node(item)
        count=1
        curr=self.headval
        while count<pos-1:
            curr=curr.next
            count=count+1
        NewNode.next=curr.next
        curr.next=NewNode
    def removeFront(self):##Remove element at the front
        curr=self.headval
        self.headval=curr.next
        curr=None
        return
    def removeLast(self):##Insert element at the last
        curr=self.headval
        while curr.next.next is not None:
            curr=curr.next
        temp=curr.next.next
        curr.next=None
        temp=None
        return
    def removeMiddle(self,pos):##Insert element in the Middle from a given position
        curr=self.headval
        count=1
        while count<pos-1:
            curr=curr.next
            count=count+1
        temp=curr.next
        curr.next=curr.next.next
        temp=None
        return
list1=SLinkedList()
list1.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list1.headval.next=e2
e2.next=e3
list1.display()
print()
list1.pushFront("Ext")
list1.display()
print()
list1.pushLast("End")
list1.display()
print()
list1.pushMiddle("Mid",2)
list1.display()
print()
list1.removeFront()
list1.display()
print()
list1.removeLast()
list1.display()
print()
list1.removeMiddle(2)
list1.display()
print()


