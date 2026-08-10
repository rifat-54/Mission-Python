def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END",n)


# show(10)

def fact(n):
   
    if(n==0 or n==1):
        return 1
    else:
       p= fact(n-1)
       return n*p
    
    


m=fact(0)

print(m)