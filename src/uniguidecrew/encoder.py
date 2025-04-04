from knowledge import pharmacy_course_names

def encoder(comp_courses):
    completed_courses_codes = ["Registration"]
    for course in comp_courses:
        completed_courses_codes.append(pharmacy_course_names[course])

    return completed_courses_codes