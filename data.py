# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:03:20 2023

@author: battl
"""

# Generate Patient


diseases = {
    "Bronchitis":
        [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .80,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "ProbabilityPercent": 1.00,
              "GameDBSymptomRef": "SYM_BRONCHIAL_INFECTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": .20,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
              }
        ]
    }


lab_examination = {
    "EXM_BACTERIA_CULTIVATION_SAMPLING": [
        'SYM_BRONCHIAL_INFECTION',
        'SYM_S._PYOGENES_PRESENT'
        ]
    }
    
doctor_examination = {
    "EXM_TEMPERATURE_MEASUREMENT": [
        'SYM_FEVER'
        ],
    "EXM_NASAL_CAVITY_INSPECTION": [
        'SYM_NASAL_CONGESTION'
        ]
    }