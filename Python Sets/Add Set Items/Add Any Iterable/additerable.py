#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#Example
#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)