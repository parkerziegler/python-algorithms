# an implementation of the quicksort algorithm

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:

        # define a pivot
        pivot = arr[0]

        # define subarrays on either side of the pivot
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]

        """
        call quicksort recursively on the subarrays,
        concatenating them with the pivot
        """
        return quicksort(left) + [pivot] + quicksort(right)

print quicksort([10, 24, 56, 34, 9])
print quicksort([200, 201, 6734, 65, 7234, 21, -45])

"""
runtime - depends on the selection of the pivot.
in the worst case, quicksort runs at O(n^2).
in the average case, quicksort runs at O(n log n).

pivots selected from the middle of the array will reach
the base case fastest (minimize recursive calls),
resulting in a stack of O(log n).

opting for the first or last element in the array will
take the longest to reach the base case, since you'll
always be working with already sorted empty arrays as
either your left or right subarrays. The resulting stack
will be of height O(n).

ultimately, however, choosing a random element in the array
will result in the average case, giving an O(n log n) runtime.
"""