# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:32:30 2023

@author: battl
"""

from data import *
import random

target_disease = 'Bronchitis'

# Generate Patient
patient = {'main': target_disease,'sym':[]}

for symptom in diseases[target_disease]:
    if symptom['ProbabilityPercent'] > random.random():
        patient['sym'].append(symptom['GameDBSymptomRef'])


# Test examination
# remember to put a filter before calling these function, or else the programme will break
def lab_examine(
    patient,
    examination: str
) -> set:
    '''
    :param patient: the patient object
    :param examination:the target examination
    :return: set of exisitng illness, if detect none return empty set
    '''

    # may want to include raise errors

    set_patient_sym = set(patient['sym'])
    set_exam_result = set(lab_examination[examination])

    return set_patient_sym.intersection(set_exam_result)


# Test examination
def doctor_examine(patient, examination):
    result = any(sym in doctor_examination[examination] for sym in patient['sym'])
    
    return result