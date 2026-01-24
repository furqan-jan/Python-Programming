            # List methods: 
list=[2,6,5,8,7,4,9,3]
list.append(10)         # Adds the element at the end.
print(list)
list.sort()             # Sorts in ascending order.
print(list)
list.sort(reverse=True)
print(list)             # Sorts in descending order.
list.reverse()          #Reverses the list.
print(list)
list.insert(0,1)        #Inserts 1 at index 0.
print(list)
list2=[1,2,3,1,4]
list2.remove(1)         #Removes the first occurence of the element.
print(list2)            #Remaining list:[2, 3, 1, 4]
list2.pop(3)            #Removes element at index 3
print (list2)