""" 
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
records = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

# Original List    
print('Original List: ', records)
# Grades
grades = []
for student in records:
    grades.append(student[1]) 

unique_grades = sorted(list(set(grades)))
print('Grades: ', unique_grades)

# Second Lowest Grade
s_low_grade = unique_grades[1]

# Output List
final_records = []
for std in records:
    if (std[1] == s_low_grade):
        final_records.append(std[0])

final_records.sort()    

# Output
for name in final_records:
    print(name)