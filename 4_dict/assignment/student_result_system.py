students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45

}

#1. Find Topper name
topper = max(students, key = students.get)
print("topper: ", topper)

# 2. Find failded student (marks < 50)
failed_students = [ name for name, marks in students.items() if marks < 50]
print("Failed students: ", failed_students)

#3. Find students with same marks
same_marks = {}
for name, marks in students.items():
    if marks not in same_marks:
        same_marks[marks] = [name]
    else:
        same_marks[marks].append(name)
print("Students with same marks: ", same_marks)

# 4. Print grades : 
grades = {}
for name, marks in students.items():
    if marks >= 90:
        grades[name] = 'A'
    elif marks >= 80:
        grades[name] = 'B'
    elif marks >= 70:
        grades[name] = 'C'
    elif marks >= 60:
        grades[name] = 'D'
    elif marks >= 50:
        grades[name] = 'E'
    else:
        grades[name] = 'F'

print("Grades: ", grades)    