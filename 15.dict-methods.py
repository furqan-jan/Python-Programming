student={
    "name":"Furqan",
    "marks":{
        "phy":90,
        "chem":95,
        "math":100
    }
}
a=student.keys()     # Returns all the keys.
print(a)
print(student.values())     # Returns all the values.
#print(list(student.keys()))
#print(len(list(student.keys())))
#print(list(student.values()))
print(student.items())      # Returns all key,value pairs as tuples.
#b=list(student.items())
#print(b[0])
print(student.get("name"))     # Returns the key according to value.
#print(student["name1"])     # The difference between this and get() method is that it gives error if key is not correct
#print(student.get("name1"))     #It does'nt give error.
student.update({"age":20})  # Inserts the specified item to the dictionary.
print(student)
student.update({"name":"Mohd Furqan"})     
print(student)

