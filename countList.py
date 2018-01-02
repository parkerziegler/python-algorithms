"""
a function to count the number of items in a list.
implemented using recursion.
"""

def countList(arr):
    if arr == []:
        return 0

    return 1 + countList(arr[1:])

print countList([6, 7, 9, 10, 4, 5])
print countList([1, 17391321, 85])
print countList([])

# runtime O(n)

"""
a function to find the max number in a list.
implemented using recursion.
"""

def maxList(arr):

    # define a pivot
    pivot = arr[0]

    # define subarrays on either side of the pivot
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    if len(right) == 0:
        return pivot
    else:
        return maxList(arr[1:])

print maxList([15, 14, 27, 9])
print maxList([101, 100, 99, 98, 97, 96])
