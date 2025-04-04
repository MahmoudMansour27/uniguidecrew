from knowledge import courses_prerequisites_codes
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