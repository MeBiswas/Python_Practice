# An array is a data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .
# Your task is to reverse an array of integers.

def reverseArray(a):
    # Write your code here
    return a[::-1]
    
arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

res = reverseArray(arr)
print(res)