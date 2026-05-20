python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

# 1. Students in both Python and SQL
both_python_sql = python_students & sql_students
print("Students in both Python and SQL:", both_python_sql)

# 2. Students in all 3 courses
all_three = python_students & sql_students & aws_students
print("Students in all 3 courses:", all_three)

# 3. Students only in Python
only_python = python_students - sql_students - aws_students
print("Students only in Python:", only_python)

# 4. Total unique students
total_unique = python_students | sql_students | aws_students
print("Total unique students:", total_unique)
print("Count of unique students:", len(total_unique))

# 5. Students not enrolled in AWS
not_in_aws = (python_students | sql_students) - aws_students
print("Students not enrolled in AWS:", not_in_aws)

# 6. Students in more than 2 courses.
all_students = list(python_students) + list(sql_students) + list(aws_students)

more_than_two = set()
for student in all_students:
    if all_students.count(student) > 2:
        more_than_two.add(student)

print("Students in more than 2 courses:", more_than_two)


# 7. Students whose name starts with 'Ra'
students_starting_ra = []
for student in total_unique:
    if student.startswith("Ra"):
        students_starting_ra.append(student)
print("Students whose name starts with 'Ra':", students_starting_ra)

# 8.Students whose name ends with 'na' or 'an'
ends_with_na_an = []
for student in total_unique:
    if student.endswith("na") or student.endswith("an"):
        ends_with_na_an.append(student)
print("Students whose name ends with 'na' or 'an':", ends_with_na_an)
