a={1,2,3}
a.add(4)    # Adds an element.
a.add((1,2,3))
print(a)
a.remove((1,2,3))
print(a)
b={2,3,4,5,6}
print(b)
b.clear()   # Empties the set.
print(b)
c={"a","b","c","d"}
print(c.pop())  # Removes a random value.
print(c.pop())
d={1,2,3,4}
e={3,4,5,6}
print(d.union(e))   # Combines both set values and returns new.
print(d.intersection(e))   # Combines common elements and returns new