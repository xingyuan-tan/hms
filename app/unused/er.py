target = {
  "Database": {
    "GameDBMedicalCondition": [
      {
        "AbbreviationLocID": "Pork Tapeworm Infection",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VITAMIN_DEFICIENCY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_HUNGER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PORK_TAPEWORM_PRESENT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_STOOL_ANALYSIS_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTITAPEWORM_PILLS",
            "TRT_ANALGESICS",
            "TRT_VITAMIN_SUPPLEMENTATION",
            "TRT_STOMACHICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1027,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Beef Tapeworm Infection",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BEEF_TAPEWORM_PRESENT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_STOOL_ANALYSIS_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTITAPEWORM_PILLS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1027,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Chickenpox",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ITCHY_BLISTERS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PAPULAS_AND_VESICLES"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIVIROTICS",
            "TRT_NUMBING_OINTMENT",
            "TRT_STOMACHICS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1029,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 100,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Iron deficiency anemia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_CRUMBLY_NAIL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 10,
              "GameDBSymptomRef": "SYM_HEMOGLOBIN_LOW"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_PALE_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LOW_HEMATOCRIT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_IRON_SUPPLEMENT",
            "TRT_DIET_MODIFICATION",
            "TRT_BRONCHODILATORS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1035,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Lactose Intolerance",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_ABDOMINAL_CRAMPS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BLOATING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FLATULENCE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LACTOSE_INTOLERANCE_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_DIET_MODIFICATION",
            "TRT_ANTIDIARRHEALS",
            "TRT_STOMACHICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1037,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Acute Pharyngitis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_RED_SWOLLEN_TONSILS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWALLOW_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SNEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DYSPHAGIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HOARSENESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_WHITE_PATCHES_ON_TONSILS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_CHEST_LISTENING",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_STOMACHICS",
            "TRT_MUCOLYTICS",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1043,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 100,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Acute Bronchitis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BRONCHIAL_INFECTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CHEST_LISTENING",
            "EXM_X_RAY_TORSO",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTITUSICS",
            "TRT_ANTIPYRETICS",
            "TRT_NSAIDS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1047,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Golfer’s Elbow",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_ELBOW_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FINGER_NUMBNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HAND_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ELBOW_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ELBOW_TENDONS_DAMAGED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_X_RAY_UPPER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_COLD_TILING",
            "TRT_REST",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1053,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Scoliosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BACK_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLE_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_NUMBNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SCOLIOTIC_FINDINGS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_BACK",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EXERCISE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1055,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Chronic Fatigue Syndrome",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_NIGHT_SWEATS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SLEEPING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_TROUBLE_RISING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LONG_REACT_TIME"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CHR._FATIGUE_SYNDROME"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_SPEECH_LISTENING",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_EVALUATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_DOCTOR'S_RECOMMENDATIONS",
            "TRT_ANTIDEPRESSIVES",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1059,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 100,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Insomnia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SLEEPING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DEPRESSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_ANXIETY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LONG_REACT_TIME"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INSOMNIA_REVEALED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_EVALUATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_SLEEPING_DRUGS",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1061,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 100,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Forearm Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FOREARM_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_UPPER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NUMBING_OINTMENT",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1129,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Wrist Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_HAND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HAND_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HAND_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_WRIST_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_UPPER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NUMBING_OINTMENT",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1131,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Foot Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_FOOT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INSTEP_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_LOWER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NUMBING_OINTMENT",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1133,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Ankle Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_ANKLE_INJURY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_ANKLE_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_INABILITY_TO_MOVE_THE_JOINT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ANKLE_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_LOWER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NUMBING_OINTMENT",
            "TRT_LEG_ORTHOSIS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1133,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Calf Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_LEG"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CALF_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_LOWER_LIMB",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NUMBING_OINTMENT",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1135,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Thorax Contusion",
        "Duration": 1,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_CHEST"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_THORAX_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_X_RAY_TORSO",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_NUMBING_OINTMENT",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_BRONCHODILATORS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1137,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 400,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Influenza B",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_NASAL_CONGESTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 90,
              "GameDBSymptomRef": "SYM_SNEEZING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INFLUENZA_B_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_NASAL_CAVITY_INSPECTION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIVIROTICS",
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2236,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Influenza A",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_NASAL_CONGESTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SNEEZING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INFLUENZA_A_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_NASAL_CAVITY_INSPECTION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIVIROTICS",
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1045,
        "DepartmentRef": "DPT_EMERGENCY",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      }
    ]
  }
}

