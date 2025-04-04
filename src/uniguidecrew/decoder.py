from knowledge import pharmacy_course_codes

def decoder(registration_courses):
    courses_decoded = []
    for code in registration_courses:
        courses_decoded.append(pharmacy_course_codes[code])

    return courses_decoded
