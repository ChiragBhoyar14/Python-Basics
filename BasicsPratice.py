
# Python Basics.

# print("Hello, Python!")

# user = input("Enter Your Name:" )

# print( f"Hi {user}, Good Afternoon!")


# -----DATA STRUCTURE------

# No type declaration is needed.
# Variables should be initialized with a value, though None can be used if you want to initialize without a specific value.

#----1. Tuple ----------------

# Tuple :- It is same as List, tuples are immutable,
#            You cannot add, remove, or modify elements directly.
#            You can, however, create a new tuple by combining existing tuples.
#Example :-  

# Numbers = (1,2,3,4,5,6)
# print(Numbers)

# Tuple Operations

# Concatenation (+)
# Combine two tuples into one.

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# result = tuple1 + tuple2
# print(result)  
# # Output: (1, 2, 3, 4)

# Repetition (*)
# Repeat a tuple multiple times.

# my_tuple = (1, 2)
# result = my_tuple * 3
# print(result)  
# Output: (1, 2, 1, 2, 1, 2)

# Slicing
# You can extract parts of a tuple using slicing.

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1:4])  
# Output: (2, 3, 4)

# Membership (in, not in)
# Check if a value exists in a tuple.

# my_tuple = (1, 2, 3)
# print(2 in my_tuple)  
# Output: True

# print(5 not in my_tuple)  
# Output: True

# Length (len())
# Get the number of elements in a tuple.

# my_tuple = (1, 2, 3, 4)
# print(len(my_tuple))  
# Output: 4

# Min/Max (min(), max())
# Get the smallest/largest item in a tuple (only works for tuples containing comparable elements like numbers).

# my_tuple = (1, 2, 3, 4)
# print(min(my_tuple))  
# Output: 1

# print(max(my_tuple))  
# Output: 4

# Sum (sum())
# Get the sum of all the elements in a tuple (only works for numeric tuples).

# my_tuple = (1, 2, 3, 4)
# print(sum(my_tuple))
# Output: 10

# Nested Tuples
# Tuples can contain other tuples as elements.

# nested_tuple = ((1, 2), (3, 4))
# print(nested_tuple[0])  
# Output: (1, 2)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------2. List----------------

# List :-  Mutable: Lists are mutable, meaning you can add, remove, or modify elements directly.
#            Flexible: Lists allow changes in their size or content after creation.
#            Dynamic: You can easily add, remove, or update elements without creating a new list.
# Example :-

# Number = [1,2,3,4,5,6]
# print(Number)

# List Methods

# append(x)
# Adds an item x to the end of the list.

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# Output: [1, 2, 3, 4]

# extend(iterable)
# Adds all the elements of an iterable (e.g., another list) to the end of the list.

# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)  
# Output: [1, 2, 3, 4, 5]

# insert(i, x)
# Inserts an item x at a specific index i. The index is zero-based.

# my_list = [1, 2, 3]
# my_list.insert(1, 4)
# print(my_list)  
# # Output: [1, 4, 2, 3]

# remove(x)
# Removes the first occurrence of the item x from the list. If the item is not found, it raises a ValueError.

# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)  
# # Output: [1, 3, 2]

# pop([i])
# Removes and returns the item at index i. If no index is specified, it removes and returns the last item.

# my_list = [1, 2, 3]
# popped_item = my_list.pop(1)
# print(my_list)  
# # Output: [1, 3]

# print(popped_item)  
# # Output: 2

# clear()
# Removes all items from the list, leaving it empty.

# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)
# Output: []

# index(x)
# Returns the index of the first occurrence of item x. If x is not found, it raises a ValueError.

# my_list = [1, 2, 3]
# print(my_list.index(2))  
# Output: 1

# count(x)
# Returns the number of occurrences of item x in the list.

# my_list = [1, 2, 2, 3, 2]
# print(my_list.count(2))  
# Output: 3

# sort()
# Sorts the list in ascending order by default. It can also accept a custom sorting function.

# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  
# # Output: [1, 2, 3]

# reverse()
# Reverses the elements of the list in place.

# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  
# Output: [3, 2, 1]

# copy()
# Returns a shallow copy of the list.

# my_list = [1, 2, 3]
# new_list = my_list.copy()
# print(new_list) 
# Output: [1, 2, 3]

# join(iterable) (For lists containing strings)
# This is a method from the str class but often used with lists to join elements into a single string with a separator.

# my_list = ['Hello', 'World']
# result = ' '.join(my_list)
# print(result)  
# Output: Hello World

# List Operations (Common Operations)

# Concatenation (+)
# Combine two lists into one.

# list1 = [1, 2]
# list2 = [3, 4]
# result = list1 + list2
# print(result)  
# Output: [1, 2, 3, 4]

# Repetition (*)
# Repeat a list multiple times.

# my_list = [1, 2]
# result = my_list * 3
# print(result)  
# Output: [1, 2, 1, 2, 1, 2]

# Slicing
# Extract parts of a list using slicing.

# my_list = [1, 2, 3, 4]
# print(my_list[1:3])  
# Output: [2, 3]

# Membership (in, not in)
# Check if a value exists in a list.

# my_list = [1, 2, 3]
# print(2 in my_list)  
# Output: True

# print(5 not in my_list)  
# Output: True

# Length (len())
# Get the number of elements in the list.

# my_list = [1, 2, 3]
# print(len(my_list))  
# Output: 3

# Min/Max (min(), max())
# Get the smallest/largest item in the list.

# my_list = [1, 2, 3, 4]
# print(min(my_list))  
# Output: 1

# print(max(my_list))  
# Output: 4

# Sum (sum())
# Get the sum of all the elements in the list (only works for numeric lists).

# my_list = [1, 2, 3, 4]
# print(sum(my_list))  
# Output: 10

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------3. Dictionaries---------

# Dictionaries :- A dictionary is a collection of key-value pairs in Python that is mutable.
#                   Meaning it can be changed after creation.
#                   Each key in a dictionary must be unique and acts as an identifier for its corresponding value.
#Example :-

#Emp_Info={"Name":"Chirag","Age":23,"Desg":"SDE"}
# print(Number.keys())
# print(Number.get("Name"))

# Dictionaries Methods

# clear()
# Removes all items from the dictionary.

# my_dict = {'a': 1, 'b': 2}
# my_dict.clear()
# print(my_dict)  
# Output: {}

# copy()
# Returns a shallow copy of the dictionary.

# my_dict = {'a': 1, 'b': 2}
# copied_dict = my_dict.copy()
# print(copied_dict)  
# Output: {'a': 1, 'b': 2}

# fromkeys(keys, value)
# Returns a new dictionary with keys from the given iterable keys and sets the value for all keys to value (default is None).

# my_dict = dict.fromkeys(['a', 'b', 'c'], 1)
# print(my_dict)  
# Output: {'a': 1, 'b': 1, 'c': 1}

# get(key, default)
# Returns the value for the specified key if the key is in the dictionary; otherwise, it returns default (default is None).

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.get('a'))  
# Output: 1

# print(my_dict.get('c', 'Not Found'))  
# Output: Not Found

# items()
# Returns a view object that displays a list of dictionary's key-value tuple pairs.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.items())  
# Output: dict_items([('a', 1), ('b', 2)])

# keys()
# Returns a view object that displays all the keys in the dictionary.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.keys())  
# Output: dict_keys(['a', 'b'])

# pop(key, default)
# Removes the key and returns its value. If the key is not found, it returns default (raises a KeyError if default is not provided).

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.pop('a'))  
# Output: 1

# print(my_dict.pop('c', 'Not Found'))  
# Output: Not Found

# popitem()
# Removes and returns the last key-value pair as a tuple (in Python 3.7+ it removes the last inserted item). Raises a KeyError if the dictionary is empty.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.popitem())  
# Output: ('b', 2)

# setdefault(key, default)
# Returns the value of key if it exists in the dictionary. If not, inserts key with a default value and returns default.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.setdefault('a', 10))  
# Output: 1

# print(my_dict.setdefault('c', 3))  
# Output: 3

# update([other])
# Updates the dictionary with the key-value pairs from other, which can be another dictionary or an iterable of key-value pairs.

# my_dict = {'a': 1, 'b': 2}
# my_dict.update({'c': 3})
# print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}

# values()
# Returns a view object that displays all the values in the dictionary.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.values())  
# Output: dict_values([1, 2])

# Dictionary Operations (Common Operations)
# Accessing values by keys
# You can access a dictionary’s value using its key.

# my_dict = {'a': 1, 'b': 2}
# print(my_dict['a'])  
# Output: 1

# Adding or updating a key-value pair
# You can add a new key-value pair or update the value for an existing key.

# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3  # Adding a new key-value pair
# my_dict['a'] = 10  # Updating the value of key 'a'
# print(my_dict)  
# Output: {'a': 10, 'b': 2, 'c': 3}

# Deleting a key-value pair
# You can delete a key-value pair using del or pop().

# my_dict = {'a': 1, 'b': 2}
# del my_dict['a']  # Deletes the key 'a'
# print(my_dict) 
# Output: {'b': 2}

# Checking for key existence (in and not in)
# You can check if a key exists in a dictionary.

# my_dict = {'a': 1, 'b': 2}
# print('a' in my_dict)  
# Output: True

# print('c' not in my_dict)  
# Output: True

# Length (len())
# Get the number of key-value pairs in the dictionary.

# my_dict = {'a': 1, 'b': 2}
# print(len(my_dict))  
# Output: 2

# Iterating through a dictionary
# You can iterate through a dictionary to access keys, values, or both.

# my_dict = {'a': 1, 'b': 2}
# for key, value in my_dict.items():
# print(key, value)
# Output:
# a 1
# b 2

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Class & Method 

# Class 
# Syntax to create class is class Class_Name: 
# Syntax to create constructor is _inti_(self)

# Example : 1. I create class Animal.
#           2. And define constructor. 
#           3. call thi class with its name()

# class  Animal:

#  def __init__(self):
#    print("Its a CLass")

# Animal()

# *____Instance class___*

# class Animal:
    
#     def Name(self, Name):
#         print(f"Its a {Name}")

# animal = Animal()
# animal.Name("Dog")


# *___Static Class___*

# class Animal:
#     @staticmethod

#     def Name(Name):
#         print(f"Its a {Name}")

# Animal.Name("Dog")

#                       ----------------Class Declearation and Calling-----------------------
#------------------------------------------------------------------------------------------------------------------------------
# Method Type	  |     Used for	                     |  First Parameter	         |  Can Access
#------------------------------------------------------------------------------------------------------------------------------
# Instance Method |     Operates on instance data        |     self                  |  Instance variables and methods
#                 |     and modifies instance state      |                           |
#------------------------------------------------------------------------------------------------------------------------------
# Static Method   |     Independent of instance          |    None (No self or cls)  |   No instance or class variables
#                 |     or class state                   |                           | 
#------------------------------------------------------------------------------------------------------------------------------
# Class Method    |     Operates on class-level data,    |     cls                   |   Class variables and other class methods
#                 |     modifies class state             |                           |
#------------------------------------------------------------------------------------------------------------------------------


# Project Structure 

# project/                -- Main folder (your project root)
# │
# ├── animals/            -- Subfolder containing related files
# │   └── animal.py       -- Python file containing the Animal class
# │
# └── main.py             -- Entry point of your project (main script)


