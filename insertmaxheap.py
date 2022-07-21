def heapify(arr,n,i):
    parent=int((i-1)/2)
    if arr[parent]>0:
        if arr[parent]<arr[i]:
            arr[i],arr[parent]=arr[parent],arr[i]
            heapify(arr,n,parent)
def insertNode(arr,key):
    global n
    n=n+1
    arr.append(key)
    heapify(arr,n,n-1)
    
    
def printheap(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print    
if __name__=="__main__":
    arr=[30,25,17,3,19,7,1,2]
    n=len(arr)
    key=27
    insertNode(arr,key)
    printheap(arr,n)

