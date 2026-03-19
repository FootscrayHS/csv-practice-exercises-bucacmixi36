# Task 1 — Display All Students
# Read students.csv and display each student's details.

students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

# Your code below — use the students list
for student in students:
    print(', '.join(student))
# could also use print(student) but it would include the brackets and quotes