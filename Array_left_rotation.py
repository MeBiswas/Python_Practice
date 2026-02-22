#  A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left. The elements that fall off the left end reappear at the right end. Given an integer d, rotate the array that many steps to the left and return the result.

def rotateLeft(d, arr):
    while d > 0:
        arr.append(arr.pop(0))
        d -= 1
    return arr

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

result = rotateLeft(d, arr)

print(result)