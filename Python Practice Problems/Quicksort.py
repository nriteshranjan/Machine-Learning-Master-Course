import math
import random 

def val(): return int(input().rstrip())

def qsort(arr, start, end):
	if(start < end):
		idx = prand(arr, start, end)
		qsort(arr,start, idx - 1)
		qsort(arr, idx + 1, end)

def prand(arr, start, end):
	pivot = random.randrange(start, end)
	arr[start], arr[pivot] = arr[pivot], arr[start]
	return partition(arr, start, end)

def partition(arr,start, end):
	pivot, i = start, start + 1
	for j in range(start + 1, end + 1):
		if(arr[j] <= arr[pivot]):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
	pivot = i - 1
	return (pivot)

n = val()
arr = [int(x) for x in input().split()]
qsort(arr, 0, n - 1)
for i in arr:
   print(i, end=' ')
