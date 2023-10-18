# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:32:30 2023

@author: battl
"""

from data import *
import random


class Patient:

    def __init__(self, patient_id, disease, symptoms=[]):
        self.patient_id = patient_id
        self.disease = disease
        self.symptoms = symptoms
        self.examined = {}

    def serialise(self):
        return {
            'patient_id': self.patient_id,
            'disease': self.disease,
            'symptoms': self.symptoms,
            'examined': self.examined
        }

    # def filter_result:


    # Test examination
    # remember to put a filter before calling these function, or else the programme will break
    def lab_examine(
            self,
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



# Generate Patient
patient_id = 123
target_disease = 'Bronchitis'
symptoms = {}

for symptom in diseases[target_disease]:
    if symptom['ProbabilityPercent'] > random.random():
        symptoms[symptom['GameDBSymptomRef']]=True

patient1 = Patient(patient_id, target_disease, symptoms)

patients = [patient1]
