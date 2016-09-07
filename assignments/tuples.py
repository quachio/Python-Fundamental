tuple_data = ('physic', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5)
tuple_letters = "a", "b", "c", "d"


# Good for using as record
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# How to access data from a tuple
print(julia[2])

for data in julia:
	print(data)


# Like strings, tuples are immutable. Once Python has created a tuple in memory,
# it cannot be changed.  But we can add and slice tuples. See example below:

print("Before", julia)
julia = julia + ("Eat Pray Love", 2010)
print("After", julia)