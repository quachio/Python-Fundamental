students = [
	{'first_name': 'Michael', 'last_name': 'Jordan'},
	{'first_name': 'John',    'last_name': 'Rosales'},
	{'first_name': 'Mark',    'last_name': 'Guillen'},
	{'first_name': 'KB',      'last_name': 'Tonel'}
]

# Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
#
# Instead: use dict.items(), dict.keys(), and dict.values() respectively.

# for name in students:
# 	for data in name.items():
# 		print(data)


#
# for key, data in students.items():
# 	print(key, " = ", data)


for name in students:
	first = name["last_name"]
	last = name["first_name"]
	print(first, last)


users = {
	'Students': [
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	],
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'}
	]
}

print("Student")
for i, name in enumerate(users["Students"]):
	first = name["last_name"]
	last = name["first_name"]

	fullname = first + last
	# print(len(fullname))

	print("{} - {} {} - {} ".format(i + 1, first, last, len(first + last)))

print("Instructor")
for i, name in enumerate(users["Instructors"]):
	first = name["last_name"]
	last = name["first_name"]

	fullname = first + last
	# print(len(fullname))

	print("{} - {} {} - {} ".format(i + 1, first, last, len(first + last)))






