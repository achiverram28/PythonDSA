##Find the min and max element of the array using recursion
def sortStackMin(stack,n):
    if n==1:
        return stack[0]
    return min(stack[n-1],sortStackMin(stack,n-1))    
def sortStackMax(stack,n):
    if n==1:
        return stack[0]
    return max(stack[n-1],sortStackMax(stack,n-1))    
    
    
t=int(input("Enter the number of elements"));
stack=[]
for i in range(t):
    stack.append(input())
print("Original Stack:")
print(stack)
minr=sortStackMin(stack,len(stack))
maxr=sortStackMax(stack,len(stack))
print("Minimum is "+minr)
print("Maximum is "+maxr)
