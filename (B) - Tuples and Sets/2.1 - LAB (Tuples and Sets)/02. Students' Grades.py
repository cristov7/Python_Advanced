students_record_dict = {}
count_students = int(input())
for student in range(1, count_students + 1):
    info_list = input().split()   # name, grade = input().split()
    name = info_list[0]
    grade = float(info_list[1])
    if name not in students_record_dict.keys():
        students_record_dict[name] = [grade]
    else:
        students_record_dict[name].append(grade)
for student_name, grades_list in students_record_dict.items():
    sum_grades = sum(grades_list)
    count_grades = len(grades_list)
    average_grade = sum_grades / count_grades
    convert_grades = " ".join(map(lambda x: f"{x:.2f}", grades_list))
    print(f"{student_name} -> {convert_grades} (avg: {average_grade:.2f})")


# students_record_dict = {}
# count_students = int(input())
# for student in range(1, count_students + 1):
#     name, grade = input().split()
#     if name not in students_record_dict.keys():
#         students_record_dict[name] = [grade]
#     else:
#         students_record_dict[name].append(grade)
# for student_name, grades_list in students_record_dict.items():
#     sequence_of_grades = ' '.join(grades_list)
#     grades_list = [float(grade) for grade in grades_list]
#     sum_grades = sum(grades_list)
#     count_grades = len(grades_list)
#     average_grade = sum_grades / count_grades
#     print(f"{student_name} -> {sequence_of_grades} (avg: {average_grade:.2f})")
