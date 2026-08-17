# f=open("practise.txt","w")

# f.write("Hi everyone \nWe are learning File I/O\nusing Java\nI like programming in java")

# print(f.read())




# f.close()

# i=open("practise.txt","r")

# # print(i.read())

# str="using java i like java"

# str1=str.replace("java","python")

# print(str1)

# with open("practise.txt","r") as f:
#     data=f.read()

# newData=data.replace("java","python")

# print(newData)

# with open("practise.txt","w") as f:
#     f.write(newData)

# new=data.find("learning")

# # print(new)
# if new :
#     print("found")
# else:
#     print("not found")


# def check_line(word):
    
#     with open("practise.txt","r") as f:
#         data=True
#         line_no=1

#         while data:
#             data=f.readline()
#             if(word in data):
#                 return line_no
#             else:
#                 line_no+=1
#         return -1


# output=check_line("learning")

# print(output)


# f=open("num.txt","w")

# for i in range(10):
#     f.write(str(i))
#     f.write(",")

with open("num.txt","r") as d:
    stl=d.read()

    # print(stl)
    ctn=0

    newList=list()

    for i in stl:
        # print(i)
        if(i!=","):

            intn=(int(i))
            if(intn%2==0):
                ctn+=1

            # print(intn)
            # newList.append(intn)

    # print(newList)
    print(ctn)



        


    