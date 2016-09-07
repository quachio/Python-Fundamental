# Creating variable
my_string = "This is string stored in the my_string variables"
my_num = 5 # an integer stored in a variable
my_tuple = (1, 2, 3, 4, 5) # a tuple store in a variable
my_dictionary = {'name': 'Michael Choi', 'fave_lang': 'Python', 'level': 'Sensei'} # a dictionary stored in a variable

#Data Types
# Boolean Values - Assesses the truth value of something. It has only two values: True and False
# Numbers - Integers, floating point numbers, and complex numbers
# Strings - A text literal. Most pages in the web work with strings quite often
# Tuples - A type of data that is immutable and can hold a group of values. Tuples can contain mixed data types
# Lists -  A type of data that is mutable and  can hold a group of values. Usually meant to store a collection of related data
# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values
# Sets - An unordered collection of data with no duplicate elements supporting operations like union, intersection, and difference

#User input
# create variable called greeting that holds the value of a string
greetings = "Hello Ninja!"
print greetings
# you can use single or double quotes for strings
print 'What is your name?'
# we use raw_input()to get user input and set it to a variable
name = raw_input()
print "How old are you?"
# we can also use input() to get user input
age = input()
# adding of variables to a string to be printed is like this:
print "Your name is", name
print "You are", age, "years old"
# you can also add the variable in between strings just like the above
raw_input("\n\nPress the enter key to exit.")
# the line above would make the app not close or exit out automatically.