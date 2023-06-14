student_scores = {
    "May": 98,
    "Nana Yaa": 78,
    "Zigi Boot": 96,
    "Archimedes": 99,
    "Rhay": 99,
    "Parker": 97,
    "Koo Mungele": 70
}
# range(91, 101): "Outstanding",
# range(81, 91): "Exceeds expectation",
# range(71, 81): "Acceptable",
# range(70): "Fail"

student_grades = {}

for student in student_scores:
    if student_scores[student] in range(91, 101):
        student_grades[student] = {student_scores[student]: "Outstanding!"}
    elif student_scores[student] in range(81, 91):
        student_grades[student] = {student_scores[student]: "Exceeds Expectations!"}
    elif student_scores[student] in range(71, 81):
        student_grades[student] = {student_scores[student]: "Acceptable"}
    else:
        student_grades[student] = {student_scores[student]: "Fail"}
# print(student_scores)
print(student_grades)
