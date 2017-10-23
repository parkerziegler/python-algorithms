"""
function to find the index of the smallest element
in an array
"""
def findSmallest(arr):

    # start at 0
    smallest_index = 0
    smallest_item = arr[0]

    # loop over all elements in array
    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i
    
    return smallest_index

# selection sort algorithm    
def selectionSort(arr):

    # initialize an empty array
    newArr = []

    """
    run findSmallest on the subsection of the passed
    in array returned from the loop
    """
    for i in len(arr):
        smallest = findSmallest(arr)

        """
        remove smallest from the passed in array
        and append it to newArr
        """

        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, 10, 2, 4, 16, 7])

# runtime: O(n^2)
    