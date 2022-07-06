#Reversing a stack using recursion
#This is using recursion
#driver code
def insertAtBottom(stack,item):
    if isEmpty(stack):
        push(stack,item)
    else:
        temp=pop(stack)
        insertAtBottom(stack,item)
        push(stack,temp)
def reverse(stack):
    if not isEmpty(stack):
        temp=pop(stack)
        reverse(stack)
        insertAtBottom(stack,temp)


def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def pop(stack):
    if(isEmpty(stack)):
        print("Underflow")
        exit()
    return stack.pop()
def prints(stack):
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=' ')
    print()
stack=createStack()
push(stack,str(4))
push(stack,str(3))
push(stack,str(2))
push(stack,str(1))
prints(stack)
reverse(stack)
print("reversed stack")
prints(stack)



