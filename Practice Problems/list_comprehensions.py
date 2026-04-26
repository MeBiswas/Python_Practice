"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example




All permutations of  are:
.

Print an array of the elements that do not sum to .


Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
list_of_cordinates = []
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             cordinates = [i,j,k]
#             sum_of_cordinates = i+j+k
#             if (sum_of_cordinates != n): 
#                 list_of_cordinates.append(cordinates)


# nested loop shorthand form
# [expression for i for j for k if condition]
list_of_coordinates = [[i, j, k] 
                       for i in range(x + 1) 
                       for j in range(y + 1) 
                       for k in range(z + 1) 
                       if i + j + k != n]

print(list_of_coordinates)

print(list_of_cordinates)