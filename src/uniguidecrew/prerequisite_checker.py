from knowledge import courses_prerequisites_codes, semester_courses_codes
from encoder import encoder
from decoder import decoder

def eligiablitiy_filter(comp_courses):
    encoded_courses = encoder(comp_courses)
    eligiable_courese = []
    for course in courses_prerequisites_codes:
        if course not in encoded_courses:
            if courses_prerequisites_codes[course] in encoded_courses:
                eligiable_courese.append(course)
    
    return eligiable_courese


def current_sem_not_completed(current_sem, completed_courses):
    encoded_courses = encoder(completed_courses)
    current_semester_courses_codes = semester_courses_codes[current_sem]
    for course in completed_courses:
        if course in current_semester_courses_codes:
            current_semester_courses_codes.remove(course)
    return current_semester_courses_codes


