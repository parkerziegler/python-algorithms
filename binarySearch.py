def binarySearch(list, item):

    # initialize starting lowIndex at 0 and starting highIndex at
    # length of the array - 1
    lowIndex = 0
    highIndex = len(list) - 1

    # while loop to check each value against the input
    while lowIndex <= highIndex:

        # get the middle index
        mid = (lowIndex + highIndex) / 2

        # get the value at the middle index
        guess = list[mid]

        # if the guess is the item, return it
        if guess == item:
            return mid

        # if the guess is too high
        if guess > item:
            # decrement the upper limit
            highIndex = mid - 1
        else:
            # increment the lower limit
            lowIndex = mid + 1
    return None

exampleList = [1, 3, 5, 7, 11, 13, 18, 24, 30]
print binarySearch(exampleList, 18)



    
