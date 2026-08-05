element=[1,4,9,16,25,36,47,64,81,100]

# for val in element:
#     print(val)


# find=int(input("enter the value to find: "))

# for val in element:
#     if(val==find):
#         print("found value:",find)
#         break
# else:
#     print("not found")


# n=int(input("enter the last digit for sum: "))

# i=0
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1

# print("sum : ",sum)


n=int(input("enter the faltorial last digit: "))

fact=1
for i in range(1,n+1,1):
    fact=fact*i

print(n," factorial =",fact)