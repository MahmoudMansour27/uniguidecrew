#!/usr/bin/env python
import sys
import warnings
from crew import RulesCrew, PriorityCrew, SelectionCrew
from knowledge import pharmacy_regulations, pharmacy_semesters_credit_hours, semester_courses_codes, key_courses_codes, credits_codes, completed_courses
from prerequisite_checker import eligiablitiy_filter
import time

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(cgpa, eng_lvl, curr_sem, comp_courses):
    """
    Run the all crews.
    """
    rules_inputs = {
      'cgpa': cgpa,
      'eng_level': eng_lvl,
      'regulations': pharmacy_regulations,
      'curr_semester': curr_sem,
      'sem_credits': pharmacy_semesters_credit_hours,
    }
    credit_json_content = RulesCrew().crew().kickoff(inputs=rules_inputs)
    print('rules crew kickoff done')
  
    time.sleep(5)
    print('sleep 5 done')

    priority_inputs={
      'credits':credit_json_content['student_maximum_credit_hours'],
      'reg_sem_credit':credit_json_content['ordinary_registration_semester_credit_hours'],
      'shortlist_cou': eligiablitiy_filter(comp_courses),
      'reg_sem_courses': semester_courses_codes[credit_json_content['registration_semester']], 
      'curr_sem': credit_json_content['current_semester'],
      'next_sem': credit_json_content['registration_semester'],
      'key_courses': key_courses_codes
    }
    prioritise_json_content = PriorityCrew().crew().kickoff(inputs=priority_inputs)
    print('priority crew kickoff done')

    time.sleep(5)
    print('sleep 5 done')


    english_course = credit_json_content['english_course']
    if english_course.lower() == 'No':
        english_course = 'Completed'
      
    selection_inputs={
      'prioritized_list': prioritise_json_content['prioritisied_courses'],
      'crdits_limit': credit_json_content['student_maximum_credit_hours'],
      'english_course': english_course,
      'credits': credits_codes,
    }
    selected_json = SelectionCrew().crew().kickoff(inputs=selection_inputs)
    print('selection crew kickoff done')
    print('Agent has finished its task!!!')

    return selected_json


# test
# print(run(
#     cgpa=3.5,
#     eng_lvl= 1,
#     curr_sem= 1,
#     comp_courses=completed_courses
# ))