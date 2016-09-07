ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# Accessing Value
drawer = ['documents', 'envelops', 'pens']
print(drawer[0])
print(drawer[1])
print(drawer[2])

# Manipulating Lists

# Append
x = list([1, 2, 3, 4, 5])
x.append(99)
print(x)

# Insert
x = list([1, 2, 3, 4, 5])
x.insert(2, 99)
print(x)

# Remove
x = list([1, 2, 3, 4, 5])
x.remove(3)
print(x)

# Pop
x = list([1, 2, 3, 4, 5])
x.pop()
print(x)

# Sort
x = list([99, 4, 2, 5, -3])
x.sort()
print(x)

# Slicing
x = list([99, 4, 2, 5, -3])
print(x[:])
print(x[1:])   # Start the slicing at index 1
print(x[:4])   # End the slicking at index 4
print(x[2:4])  # Start the slicking at index 2 and end at 4

# List Build-in Functions

# len() -> return the number of items in sequence
my_list = [1, 'Zen', 'hi']
print (len(my_list))

# max() -> returns the largest item in the sequence
my_list = [1, 7, 3]
print(max(my_list))

# min() -> Returns the smallest item in the sequence.
# When comparing boolean to numbers, True == 1 and False == 0.
# Comparing items of differing types are quite uncommon,
# but if you ever do this, note that all numbers < all dictionaries < all lists < all strings < all tuples.
my_list = [1, 7, 3]
print(min(my_list))



# any() Returns True if there exists any item in the sequence which is True.
my_list = [0, 'hi', '']
print(any(my_list))
# the output would be True since a string would equate to true in this case
my_list = [0, '']
# the output would be False since 0 (zero) and an empty string will both be false
print(any(my_list))


my_list = [0, 'Zen', '']
print(all(my_list))
# the output would be False
my_list = [4, 'hi']
print(all(my_list))
# the output would be True


# http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html go here to
# learn more


names = ['KB', 'Oliver', 'Mikey', 'John', 'Michael']

print('\n'.join(names))

x = [5, 34, 10, 1, 6]

# x.append(2)
# print(x)

x = x + [2]
print(x)


