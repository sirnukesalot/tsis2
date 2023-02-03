#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

#Example
#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

#Example
#Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)