for count in range(0, 5):
	print ("looping - ", count)

# Looping Through a List
# create a new list
# rememeber lists can hod many data-types, even lists!
my_list = [4, 'dog', 99, ['list', 'inside', 'another'],'hello world!']
for element in my_list:
	print(element)


# While Loops
# While loops are often used when we don't know how many
# times we have to repeat a block of code but we know we have to
# do it until a certain condition is met.
for count in range(0, 5):
	print(count)

#  while loop version of the for loop above
count = 0
while count < 5: # notice the colon!
	print('looping - ', count)
	count += 1


# Example of break

for val in "string":
	if val == "i":
		break
	print(val)


# Example of continue
for val in "string":
	if val == "i":
		continue
	print(val)

# Else
x = 3
y = x

while y > 0:
	print(y)
	y = y - 1
else:
	print("Final else statement")


x = 3
y = x
while y > 0:
	print(y)
	y = y - 1
	if y == 0:
		break
else:
	print("Final else statement")
