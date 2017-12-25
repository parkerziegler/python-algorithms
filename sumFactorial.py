"""
function to add an array of numbers, returning the sum.
mimics the behavior of reduce, but uses recursion to achieve
the desired result.
"""

def sum(arr):
    if arr == []:
        return 0
    
    return arr[0] + sum(arr[1:])

print sum([1])
print sum([1, 5, 132])
print sum([76, 40, 97, 2])

"""
function to return the factorial of a given number.
implements the same recursive technique as sum
"""
def factorial(num):
    if num == 0:
        return 1
    
    return num * factorial(num - 1)

print factorial(3)
print factorial(5)
print factorial(10)
