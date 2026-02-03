 # Dictionary are used to store data values in key:value pairs.
 # They are unordered,mutable(changeable) and don,t allow duplicate keys .

# dict = {            #"key":value
#     "name":"Furqan",
#     "age":20,
#     "course":"python",
#     "marks":[90,80,70,60],
# }
# print(dict)
# print(type(dict))
# print(dict["name"])
# dict["course"]="Python programming"     # overwrite
# print(dict)
# nulldict={}
# print(nulldict)
                # Nested Dictionary:
student={
    "name":"Furqan",
    "marks":{
        "phy":90,
        "chem":95,
        "math":100
    }

} 
print(student)
print(student["marks"])
print(student["marks"]["math"])