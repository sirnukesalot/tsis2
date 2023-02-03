#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.

#Condition
#The condition is like a filter that only accepts the items that valuate to True.

#Example
#Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:

#Example
#With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)
#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.

#Example
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

print(newlist)
#Same example, but with a condition:

#Example
#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
#Expression
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

#Example
#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
#You can set the outcome to whatever you like:

#Example
#Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

#Example
#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
#The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange"

