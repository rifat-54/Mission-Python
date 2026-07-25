info={
    "key":"value",
    "name":"rifat",
    "leaning":"python",
    "subject":["python","c","c++"],
    "marks":(233,34,5465,6456),
    34.34:5675   #KEY can be also integer and float value
}

# print(type(info))

# info["name"]="mashur"
# info["sureName"]="rifat"

# print(info["name"])

null_dict={}

null_dict["name"]="rifat"

# print(null_dict)

student={
    "name":"rifat",
    "subject":{
        "phy":34,
        "math":34,
        "c":64
    }
}

# print(student["subject"]["math"])

# ! dictionary method

# print(student.keys())

# print(list(student.keys()))  # convert output and store in list

# print(len(student.keys()))

# print(len(list(student.keys())))

# print(student.values())

# print(list(student.values()))

# print(student.items())

# print(list(student.items()))

# pair=list(student.items())

# print(pair[1])

# print(student["name2"])    # !return error if not key exit
# print(student.get("name2"))   #! return none if not key exit. not return error

# student.update({"name":"mashur","city":"Dhaka","age":34})

new_dict={
    "name":"mashur",
    "city":"dhaka"
}

student.update(new_dict)

print(student)