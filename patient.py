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
def lab_examine(patient, examination):
    result = any(sym in lab_examination[examination] for sym in patient['sym'])
    
    return result


# Test examination
def doctor_examine(patient, examination):
    result = any(sym in doctor_examination[examination] for sym in patient['sym'])
    
    return result