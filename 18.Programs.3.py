# # Store the following word meanings in python dictionary:
# # table:"a piece of furniture" , "list of facts and figures"
# # cat: "a small animal"
# dict={
#     "table":["a piece of furniture" , "list of facts and figures"],
#     "cat": "a small animal" 
# }
# print(dict["table"])
# print(dict)

# You are given a list of subjects .Assume one classroom is required for 1 subject.How many classrooms are needed 
# by all students:"python",“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
# set={"python","java","C++","python","javascript","java","python","java","C++","C" }
# print(len(set))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

# dict={}
# a=int(input("Enter marks of English :" ))
# dict.update({"English":a})
# b=int(input("Enter marks of Math :" ))
# dict.update({"Math":b})
# c=int(input("Enter marks of Science :" ))
# dict.update({"Science":c})
# print(dict)


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
a={"9.0",9} #OR
set={ ("int",9) , ("float",9.0)}
print(a)
print(set)
print(type(set))