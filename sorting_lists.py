from random import random

def test(function):
	"""
	Tests a sorting list function that sorts in increasing order. The tests
	cases are all in the "tests" list, feel free to change it if you want
	more complex tests.

	@function: The function that you want to test.

	@return: None (everything is printed).
	"""
	num_fails = 0															# Number of fails the function got
	tests = [[],															# Test 0: Empety list
			 [1, 2, 3, 4, 5, 6],											# Test 1: Even size ordered list
			 [1, 2, 3, 4, 5, 6, 7],											# Test 2: Odd size ordered list
			 [6, 5, 4, 3, 2, 1],											# Test 3: Even size reversed list
			 [7, 6, 5, 4, 3, 2, 1],											# Test 4: Odd size reversed list
			 [2, 2, 3, 4, 1, 7, 20]]										# Test 5: List with repetition

	print "------ Starting test ------"
	for i, test in enumerate(tests):										# Iterates over the tests in the tests list
		given_answer = function(test)										# Gets the answer from the given function
		correct_answer = sorted(test)										# Gets the answer from the built-in Python sorting funciton
		if given_answer == correct_answer:
			print "Test " + str(i) + ": Gave " + str(test) + " got " + str(given_answer) + " Passed!"
		else:
			print "Test " + str(i) + ": Gave " + str(test) + " got " + str(given_answer) + " should be " + str(correct_answer) + " Found a problem!"
			num_fails += 1
	
	# Shows a final result
	if num_fails == 0:
		print "Got all correct!"
	else:
		print "Got " + str(num_fails) + " incorrect"
	print "------ Test finished ------\n"


def mergeSort(unsorted_list):
	"""
	Merge Sort
	Time Complexity:    O(n log(n))
	Memory Complexity:  O(n)
	"""
	len_unsList = len(unsorted_list)										# Gets the size of the list
	
	# Returns the list itself if the size is smaller or equal to 1
	if len_unsList <= 1:
		return unsorted_list
	
	# Reverses the list if the second value is smaller than the first
	elif len_unsList == 2:
		return unsorted_list if unsorted_list[0] < unsorted_list[1] else unsorted_list[::-1]
	
	else:
		list1 = mergeSort(unsorted_list[:int(len_unsList/2)])				# Calls mergeSort for the first half part of the list
		list2 = mergeSort(unsorted_list[int(len_unsList/2):])				# Calls mergeSort for the second half part of the list
		sorted_list = list()

		while True:
			if len(list1) == 0:												# If the first list is empty, appends the second list
				return sorted_list + list2
			if len(list2) == 0:												# If the second list is empty, appends the first list
				return sorted_list + list1

			# Append the smaller first element of the two lists
			sorted_list.append(list1.pop(0) if list1[0] < list2[0] else list2.pop(0))


def bubbleSort(sortingList):
	"""
	Bubble Sort
	Time Complexity:    O(n^2)
	Memory Complexity:  O(1)
	"""
	swapped = True
	len_sortingList = len(sortingList)										# Gets the size of the list

	while swapped:
		swapped = False

		for i in range(len_sortingList-1):
			# If the actual element is bigger than the next, swaps them
			if sortingList[i] > sortingList[i+1]:
				sortingList[i], sortingList[i+1] = sortingList[i+1], sortingList[i]
				swapped = True
		
		# If we passed through the list without making any swaps, breaks the loop
		if not(swapped):
			break
	return sortingList


def quickSort(sortingList, start_point=None, end_point=None):
	"""
	Quick Sort
	Time Complexity:    O(n^2)
	Memory Complexity:  O(log(n))
	"""
	# Sets start point and end point if not given
	if start_point == None and end_point == None:
		start_point = 0
		end_point = len(sortingList) - 1

	if start_point == end_point or len(sortingList) == 0:
		return sortingList

	i = start_point															# Sets the first index to the start point
	j = end_point															# Sets the secont index to the end point
	piv = sortingList[(start_point+end_point)/2]							# Sets the pivot to the middle value

	while (i < j):															# Goes making the two indexes closer
		while i < j and sortingList[i] < piv:								# until the first index finds a value greater then the pivot
			i += 1
		while i < j and sortingList[j] >= piv:								# and the second index finds a value smaller then the pivot
			j -= 1

		sortingList[i], sortingList[j] = sortingList[j], sortingList[i]		# then it is swapped and goes back to getting the indexes close

	if i-1 > start_point:													# Makes sure the index is in the list scope (greater than the start point)
		quickSort(sortingList, start_point, i-1)							# Sorts the first half
	if i+1 < end_point:														# Makes sure the index is in the list scope (smaller than the end point)
		quickSort(sortingList, i, end_point)								# Sorts the second half

	return sortingList


# Tests the functions
test(mergeSort)
test(bubbleSort)
test(quickSort)