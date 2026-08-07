# def printlen(a):
#     print(len(a))
#     print(a)


# list=[2,4,6,3,8]

# printlen(list)

def findFactorial(n):
    i=1
    fact=1
    # while i<=n:
    #     fact*=i
    #     i+=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

# findFactorial(6)

def convertUsdToBdt(t):
    print(t*123.58)

# convertUsdToBdt(5)

list=[2,4,6,3,8]

def print_list(list):
    for i in list:
        print(i,end=" ")

# print_list(list)

def find_odd_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

find_odd_even(4)



