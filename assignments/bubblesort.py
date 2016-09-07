import random
import datetime
import timeit

# arr = [5, 3, 2, 1]
#
# # Bubble sort
#
# for i in range(0, len(arr) - 1):
# 	for k in range(0, len(arr) - 1):
# 		if arr[k] > arr[k + 1]:
# 			temp = arr[k]
# 			arr[k] = arr[k + 1]
# 			arr[k + 1] = temp
# 	print(i, arr)
#
#

def bubbleSort(arr):

	for i in range(0, len(arr) - 1):
		for k in range(0, len(arr) - 1):
			if arr[k] > arr[k + 1]:
				temp = arr[k]
				arr[k] = arr[k + 1]
				arr[k + 1] = temp
	end_time = datetime.time()
	return arr

arr = []

for i in range(0, 100):
	arr.append(random.randint(0, 10000))
print(arr)
print(bubbleSort(arr))




