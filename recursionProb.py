def sum(n):
    if(n==0):
        return n
    p=sum(n-1)
    return n+p


# print(sum(10))

l=[1,2,3,4,5]

def printList(a,n):

    if(n==-1):
        return
    printList(a,n-1)
    print(a[n],end=" ")


printList(l,len(l)) 
