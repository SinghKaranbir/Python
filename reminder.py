names = input("Enter the name of the students seprated by comas: ").split(',')
assignments = input("Enter the no of assignments left: ").split(',')
grades = input("Enter current grades of the students: ").split(',')
estimate_grades = input("Enter estimation of grades if assignments gets submitted: ").split(',')
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade, estimate_grade in zip(names, assignments, grades, estimate_grades):
    print(message.format(name, assignment, grade, estimate_grade))
