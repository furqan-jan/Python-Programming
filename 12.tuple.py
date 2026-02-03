    # Tuple is a built in data type that lets us create immutable(cannot be changed) sequence of values.
tup=(1,2,3,8,1,5,3)
# print(type(tup))
# print(tup)
# tup1=(1,)    # For single element use " , " at last to make it as tuple data type.
# print(type(tup1))
# print(tup[3])
    # Tuple slicing:
print(tup[:2])
print(tup[:])
print(tup[3:])
print(tup[-5:-1])
    # Tuple  methods
print(tup.index(3))   #Returns the index of first occurence.
print(tup.count(3))    #Counts total occurences.