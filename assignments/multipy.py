# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:

a = [2, 4, 10, 16]



def multiply(arr, v):
	for i, number in enumerate(arr):
		arr[i] = arr[i] * 5
	return arr

b = multiply(a, 5)
print(b)