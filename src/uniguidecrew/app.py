__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from main import run
import time
import json
from decoder import decoder
import streamlit_authenticator as stauth
import pickle
from key_generator import names, usernames
from knowledge import credits_codes

st.set_page_config(initial_sidebar_state="collapsed")


# Load hashed passwords from the file
with open('./src/uniguidecrew/hashed_pw.pkl', 'rb') as file:
    hashed_pass = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_pass, 'uniguide', 'abc1234', cookie_expiry_days=10)
name, status, username = authenticator.login('Login', 'main')

if status == False:
    st.error('Username or password is incorrect 😢️')
elif status == None:
    st.warning('Please enter your username and password ☺️')
elif status:
    # background
    st.image('./assets/bg.png')

    # intro
    st.title(f"Welcome {name} at UniGuide 🎓️")
    st.markdown('*We are here to help you ❤️*')
    st.text('UniGuide V1.2 is a smart, AI-powered app designed to make university life easier for students. Whether you need help with course registration, academic advice, campus resources, or time management, UniGuide has got you covered. With personalized recommendations, real-time assistance, and an intuitive interface, the app ensures you stay on top of your studies while making the most of your university experience. Say goodbye to confusion and hello to a smoother academic journey with UniGuide! 🚀')
    st.markdown('---')

    # course selections
    st.header('Please select your completed couses')

    # Level 1
    semester_1 = [
        "Pharmaceutical Analytical Chemistry I",
        "Pharmaceutical Organic Chemistry I",
        "Pharmacy Orientation",
        "Medicinal Plants",
        "Information Technology",
        "Mathematics",
        "Human Rights and Fighting Corruption"
    ]

    semester_2 = [
        "Pharmaceutical Analytical Chemistry II",
        "Pharmaceutical Organic Chemistry II",
        "Cell Biology",
        "Medical Terminology",
        "Anatomy & Histology",
        "Physical Pharmacy",
        "Pharmacognosy I",
        "Psychology"
    ]

    # Level 2
    semester_3 = [
        "Pharmaceutical Analytical Chemistry III",
        "Pharmaceutical Organic Chemistry III",
        "Pharmacognosy II",
        "Physiology and Pathophysiology",
        "Pharmaceutics I",
        "Scientific Writing",
        "Scientific Thinking",
        "Sinai History"
    ]

    semester_4 = [
        "Biochemistry I",
        "General Microbiology and Immunology",
        "Instrumental Analysis",
        "Pathology",
        "Pharmaceutics II",
        "Presentation & Communication Skills",
        "Biostatistics"
    ]

    # Level 3
    semester_5 = [
        "Biochemistry II",
        "Pharmaceutical Microbiology",
        "Phytochemistry",
        "Pharmaceutics III",
        "Medicinal Chemistry I",
        "Pharmacology I"
    ]

    semester_6 = [
        "Parasitology",
        "Biopharmaceutics & Pharmacokinetics",
        "Applied and Forensic Pharmacognosy",
        "Pharmaceutics IV",
        "Pharmacology II",
        "Medicinal Chemistry II"
    ]

    # Level 4
    semester_7 = [
        "Medical Microbiology",
        "Pharmacology III",
        "Drug Design",
        "Clinical Biochemistry",
        "Pharmaceutical Technology I",
        "Pharmaceutical Legislations & Professional Ethics",
        "Elective"
    ]

    semester_8 = [
        "Clinical Pharmacokinetics",
        "Drug Information",
        "Toxicology & Forensic Chemistry",
        "Hospital Pharmacy",
        "Pharmaceutical Technology II",
        "Clinical Pharmacy and Pharmacotherapeutics I",
        "Elective"
    ]

    # Level 5
    semester_9 = [
        "Biotechnology",
        "Community Pharmacy Practice",
        "Public Health",
        "Phytotherapy and Aromatherapy",
        "Good Manufacturing Practice",
        "Marketing & Pharmacoeconomics",
        "Clinical Pharmacy and Pharmacotherapeutics II",
        "Elective"
    ]

    semester_10 = [
        "Quality Control of Pharmaceuticals",
        "First Aid",
        "Drug Interaction",
        "Advanced Drug Delivery Systems",
        "Clinical Pharmacy and Pharmacotherapeutics III",
        "Entrepreneurship",
        "Clinical Research, Pharmacoepidemiology & Pharmacovigilance",
        "Elective"
    ]

    st.subheader('Level One: Semester One')
    semester_1_selected = st.pills('s1', options= semester_1, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level One: Semester Two')
    semester_2_selected = st.pills('s2', options= semester_2, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Two: Semester One')
    semester_3_selected = st.pills('s3', options= semester_3, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Two: Semester Two')
    semester_4_selected = st.pills('s4', options= semester_4, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Three: Semester One')
    semester_5_selected = st.pills('s5', options= semester_5, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Three: Semester Two')
    semester_6_selected = st.pills('s6', options= semester_6, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Four: Semester One')
    semester_7_selected = st.pills('s7', options= semester_7, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Four: Semester Two')
    semester_8_selected = st.pills('s8', options= semester_8, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Five: Semester One')
    semester_9_selected = st.pills('s9', options= semester_9, selection_mode="multi", label_visibility='collapsed')

    st.subheader('Level Five: Semester Two')
    semester_10_selected = st.pills('s10', options= semester_10, selection_mode="multi", label_visibility='collapsed')

    student_selected_courses = semester_1_selected + semester_2_selected + semester_3_selected + semester_4_selected + semester_5_selected + semester_6_selected + semester_7_selected + semester_8_selected + semester_9_selected + semester_10_selected

    # CGPA input
    st.header('Please enter your CGPA')
    student_cgpa = st.number_input('Enter you CGPA', min_value=0.0, max_value=4.0)
    print(student_cgpa)

    # Current semester input
    st.header('Please enter your current semester')
    student_curr_sem = st.number_input('Enter you semester number', min_value=0, max_value=10, step=1)

    # English Level input
    st.header('Please enter your English Level')
    st.write('1: Low Level, 2: Intermediate, 3:High Level, 4: Completed English Course')
    student_eng_level = st.number_input('Enter you level', min_value=0, max_value=4, step=1)


    # Additional Notes
    st.header('If you have any additional notes')
    st.text_area('Enter your notes here')

    def guide_me():
        result, extra, credits_json_content = run(cgpa=float(student_cgpa), 
                     eng_lvl=int(student_eng_level), 
                     curr_sem=int(student_curr_sem), 
                     comp_courses=student_selected_courses)

        results_container.write(result['reasoning'])
        results_container.markdown(f"*CGPA: {student_cgpa}*")
        results_container.markdown(f"*Current Semester: {student_curr_sem}*")
        results_container.markdown(f"*Registration Semester: {credits_json_content['registration_semester']}*")
        results_container.markdown(f"*Semester Total Credit Hours: {credits_json_content['ordinary_registration_semester_credit_hours']}*")
        results_container.markdown(f"*Student Total Credit Hours: {result['total_credit_hours']}*")


        for course in result['selected_courses']:
            with results_container.expander(f"📚️ {decoder([course['course']])[0]} ---------------- {course['course']}"):
                st.markdown(f"*Credit Hours: {course['credits']}*")
                st.write(f"Reasoning: {course['reasoning']}")

        for course in extra['prioritisied_courses']:
            if course['course'] not in [selected['course'] for selected in result['selected_courses']]:
                with extra_container.expander(f"📚️ {decoder([course['course']])[0]} ---------------- {course['course']}"):
                    st.markdown(f"*Credit Hours: {credits_codes[course['course']]}*")
                    st.write(f"Priority: {course['priority']}")
            
        
    # generate button
    st.button('Guide Me 🚀️', type = 'primary', on_click = guide_me, use_container_width = True)

    # Results
    st.markdown('---')
    st.header('Here is your Guide 🤓️')

    results_container = st.container()

    # extra
    st.markdown('---')
    st.header('Extra Courses 💫️')
    st.write('Here are some extra courses you can take for overload and handle unexpected scenarios:')

    extra_container = st.container()


    # sidebar
    st.sidebar.write('Every logout breaks a little piece of our server\'s heart 💔️.')
    st.sidebar.write('You logout now, but you’ll be back. They always come back 😠️.')
    authenticator.logout('Logout', 'sidebar')

    
        





    



