#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new tuple with the specified items.

#Example
#Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:

#Example
#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#By leaving out the end value, the range will go on to the end of the list:

#Example
#This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])