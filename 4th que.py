# Define a tuple
my_tuple = (1, 2, 3)

# Trying to modify an element in the tuple
try:
    my_tuple[0] = 4
except TypeError as e:
    print(e)


#What is immutability ?

# A general definition of an immutable object is one whose state cannot be changed after creation.
# This means that once an immutable object is created, its contents or properties cannot be changed. 
# Tuples, integers, and strings are a few examples of immutable objects in Python.
# Mutable objects, on the other hand, are those whose state can be changed after they are formed.
# In Python, mutable objects include dictionaries, sets, and list   