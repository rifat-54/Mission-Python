# f=open("demo.txt","r")

# print(f)
# print(type(f))

# data=f.read()
# print(data)

# print(type(data))

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# f=open("demo.txt","a")

# f.write("\nwhere you go")

# f=open("sample.txt","w")

# f.close()

# f=open("demo.txt","r+")
# f=open("demo.txt","w+")
# f=open("demo.txt","a+")

# print(f.read())
# f.write("z")

# f.close()

with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")