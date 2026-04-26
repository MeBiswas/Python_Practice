"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
N = int(input())
    
my_list = []
    
for _ in range(N):
    command_line = input().split()
    command = command_line[0]
    
    match command:
        case 'insert':
            my_list.insert(int(command_line[1]), int(command_line[2]))
        case 'print':
            print(my_list)
        case 'remove':
            my_list.remove(int(command_line[1]))
        case 'append':
            my_list.append(int(command_line[1]))
        case 'sort':
            my_list.sort()
        case 'pop':
            my_list.pop()
        case 'reverse':
            my_list.reverse()