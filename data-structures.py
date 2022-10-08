import numpy as np
import pandas as pd

print("Hello world.")

# Quicksort
def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			(array[i], array[j]) = (array[j], array[i])
	(array[i+1], array[high]) = (array[high], array[i+1])
	return i+1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, pi-1)
		quickSort(array, low, high, pi-1)
		quickSort(array, pi+1,high)

