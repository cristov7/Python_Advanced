def students_credits(*student_courses_tuple):
    def calculate_credits_function():
        current_course_name = course_info_list[0]
        current_credits = int(course_info_list[1])
        current_max_test_points = int(course_info_list[2])
        current_student_points = int(course_info_list[3])
        current_result_percents = (current_student_points / current_max_test_points) * 100
        current_result_credits = (current_credits * current_result_percents) / 100
        current_calculate_dict = {current_course_name: current_result_credits}
        return current_calculate_dict

    def output_function():
        current_output_list = []
        student_credits = sum(course_credits_dict.values())
        diploma_credits = 240
        if student_credits >= diploma_credits:
            current_output = f"Diyan gets a diploma with {student_credits:.1f} credits."
            current_output_list.append(current_output)
        else:
            need_more_credits = abs(student_credits - diploma_credits)
            current_output = f"Diyan needs {need_more_credits:.1f} credits more for a diploma."
            current_output_list.append(current_output)
        sorted_course_credits_dict = dict(sorted(course_credits_dict.items(), key=lambda x: -x[1]))
        for course_name, course_credits in sorted_course_credits_dict.items():
            current_output = f"{course_name} - {course_credits:.1f}"
            current_output_list.append(current_output)
        return current_output_list

    course_credits_dict = {}
    for course_info in student_courses_tuple:
        course_info_list = course_info.split("-")
        calculate_dict = calculate_credits_function()
        course_credits_dict.update(calculate_dict)
    output_list = output_function()
    return "\n".join(output_list)


# def students_credits(*student_courses_tuple):
#     course_credits_dict = {}
#     for course_info in student_courses_tuple:
#         course_info_list = course_info.split("-")
#         current_course_name = course_info_list[0]
#         current_credits = int(course_info_list[1])
#         current_max_test_points = int(course_info_list[2])
#         current_student_points = int(course_info_list[3])
#         result_percents = (current_student_points / current_max_test_points) * 100
#         result_credits = (current_credits * result_percents) / 100
#         course_credits_dict[current_course_name] = result_credits
#     student_credits = sum(course_credits_dict.values())
#     diploma_credits = 240
#     output_list = []
#     if student_credits >= diploma_credits:
#         output = f"Diyan gets a diploma with {student_credits:.1f} credits."
#         output_list.append(output)
#     else:
#         need_more_credits = abs(student_credits - diploma_credits)
#         output = f"Diyan needs {need_more_credits:.1f} credits more for a diploma."
#         output_list.append(output)
#     sorted_course_credits_dict = dict(sorted(course_credits_dict.items(), key=lambda x: -x[1]))
#     for course_name, course_credits in sorted_course_credits_dict.items():
#         output = f"{course_name} - {course_credits:.1f}"
#         output_list.append(output)
#     return "\n".join(output_list)


# print(students_credits("Computer Science-12-300-250",
#                        "Basic Algebra-15-400-200",
#                        "Algorithms-25-500-490"))


# print(students_credits("Discrete Maths-40-500-450",
#                        "AI Development-20-400-400",
#                        "Algorithms Advanced-50-700-630",
#                        "Python Development-15-200-200",
#                        "JavaScript Development-12-500-480",
#                        "C++ Development-30-500-405",
#                        "Game Engine Development-70-100-70",
#                        "Mobile Development-25-250-225",
#                        "QA-20-300-300"))


# print(students_credits("Python Development-15-200-200",
#                        "JavaScript Development-12-500-480",
#                        "C++ Development-30-500-405",
#                        "Java Development-10-300-150"))
