# Given a 6x6 2D array, arr, an hourglass is a subset of values with indices falling in the following pattern:
# a b c
#   d
# e f g
# There are 16 hourglasses in a 6x6 array. The hourglass sum is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

def hourglassSum(arr):
    print(arr)

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)