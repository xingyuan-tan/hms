target = {
  "Database": {
    "GameDBMedicalCondition": [
      {
        "AbbreviationLocID": "Carpal Tunnel Syndrome",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FINGER_NUMBNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_WRIST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_CRAMPS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HAND_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HAND_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_THUMB_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_MEDIAN_NERVE_COMPRESSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ENDOSCOPIC_SURGERY",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1205,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 2900,
        "Tags": {
          "Tag": "disease"
        }
      },

      {
        "AbbreviationLocID": "Rheumatoid Arthiritis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_REDNESS_OF_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_SWELLING_JOINTS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_STIFFNESS_OF_THE_JOINTS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_STIFFNESS_IN_THE_KNEE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_STIFFNESS_IN_THE_HIP"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WALKING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_ANEMIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_RHEUMATOID_FACTOR"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_OSTEOPOROSIS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CRP",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_CT",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_CORTICOSTEROIDS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_BONE_STRENGTH_PILLS",
            "TRT_REHABILITATION"
          ]
        },
        "IconIndex": 1207,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 1100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Hip Osteoarthritis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WADDLING_GAIT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ASTASIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SLEEPING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WALKING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_STIFFNESS_IN_THE_HIP"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BACK_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HIP_JOINTS_DAMAGED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_HIP_REPLACEMENT_SURGERY",
            "TRT_ANALGESICS",
            "TRT_SLEEPING_DRUGS"
          ]
        },
        "IconIndex": 1209,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 3000,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Knee Osteoarthritis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING_KNEE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ASTASIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WALKING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WADDLING_GAIT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_STIFFNESS_IN_THE_KNEE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_KNEE_JOINT_DAMAGED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROID_INJECTIONS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1211,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 700,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Dermatomyositis",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TROUBLE_RISING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HOARSENESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLE_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CREATINE_KINASE_HIGH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_MUSCLES_INFLAMMED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROIDS",
            "TRT_STEROID_TOPICAL_CREAM",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1029,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Osteomyelitis",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING_LIMBS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_LEUKOCYTOSIS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BONE_INFECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CBC_SAMPLING",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_OSTEOMYELITIS_SURGERY",
            "TRT_ANTIBIOTICS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1221,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 3100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Bursitis of Hand",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_WRIST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HAND_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HAND_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_REDNESS_OF_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HAND_BURSAE_INFLAMMED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_USG",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROID_INJECTIONS",
            "TRT_COLD_TILING",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1223,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Adult Osteomalacia",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLE_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_FREQUENT_FALLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ASTASIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPOCALCAEMIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_OSTEOPOROSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VITAMIN_DEFICIENCY"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PSEUDOFRACTURES"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_CHOLECALCIFEROL_SUPPLEMENT",
            "TRT_VITAMIN_SUPPLEMENTATION",
            "TRT_BONE_STRENGTH_PILLS",
            "TRT_INTRAVENOUS_CALCIUM_GLUCONATE",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1221,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 1000,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Olecranon Bursitis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ELBOW_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_REDNESS_OF_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_ELBOW_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OLECRANON_BURSAE_INFLAMMED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_USG",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROID_INJECTIONS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1225,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Bursitis of Knee",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_STIFFNESS_IN_THE_KNEE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING_KNEE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_REDNESS_OF_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_KNEE_BURSAE_INFLAMMED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_USG",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROID_INJECTIONS",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_REHABILITATION",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1227,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "disease"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Deep Wound Hand",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_HAND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SKIN_AVULSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_DEGLOVED_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HAND_PENETRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_INFECTED_WOUND"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_REPLANTATION",
            "TRT_WOUND_CLOSURE",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1229,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Deep Wound Arm",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SKIN_AVULSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ARM_PENETRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_INFECTED_WOUND"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_WOUND_CLOSURE",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1231,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Deep Wound Leg",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_SKIN_AVULSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LEG_PENETRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_INFECTED_WOUND"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_WOUND_CLOSURE",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1235,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
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
        "AbbreviationLocID": "Deep Wound Feet",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_SKIN_AVULSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_DEGLOVED_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FEET_PENETRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_INFECTED_WOUND"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_REPLANTATION",
            "TRT_WOUND_CLOSURE",
            "TRT_BANDAGE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1233,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "trauma"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "Shoulder Sprain",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SHOULDER_INJURY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPASMS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SHOULDER_SPRAIN"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NSAIDS",
            "TRT_COLD_TILING",
            "TRT_REST",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANALGESICS",
            "TRT_SPASMOLYTICS",
            "TRT_REHABILITATION"
          ]
        },
        "IconIndex": 1237,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Knee Sprain",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_KNEE_INJURY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPASMS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_KNEE_SPRAIN"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NSAIDS",
            "TRT_COLD_TILING",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_REHABILITATION",
            "TRT_ANALGESICS",
            "TRT_SPASMOLYTICS"
          ]
        },
        "IconIndex": 1241,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "trauma"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Ankle Sprain",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ANKLE_INJURY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPASMS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ANKLE_SPRAIN"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_NSAIDS",
            "TRT_COLD_TILING",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_REHABILITATION",
            "TRT_ANALGESICS",
            "TRT_SPASMOLYTICS"
          ]
        },
        "IconIndex": 1245,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "trauma"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_limp"
      },
      {
        "AbbreviationLocID": "acl tear",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_KNEE_INJURY"
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
              "GameDBSymptomRef": "SYM_WALKING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ACL_INJURY"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_RICE",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
       "IconIndex": 1249,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 700,
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
        "AbbreviationLocID": "Simple Fracture Ulna",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
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
              "GameDBSymptomRef": "SYM_ULNA_FRACTURE"
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
            "TRT_ARM_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1251,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Open Fracture Ulnar",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SEVERE_ARM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BONE_FRACTURE_VISIBLE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_DEPICTION_OF_ULNAR_FRACTURE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HYPOVOLEMIC_SHOCK"
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
            "TRT_HOSPITALIZATION_TRAUMA",
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_FRACTURE_SURGERY_ARM",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_BANDAGE"
          ]
        },
        "IconIndex": 1253,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 2800,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Simple Fracture Radius",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_RADIUS_FRACTURE"
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
            "TRT_ARM_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1251,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Simple Fracture Humerus",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_LIMITED_ARM_MOTION"
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HUMERUS_FRACTURE"
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
            "TRT_ARM_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1257,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Open Fracture Humerus",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SEVERE_ARM_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BONE_FRACTURE_VISIBLE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_DEPICTION_OF_HUMERUS_FRACTURE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HYPOVOLEMIC_SHOCK"
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
            "TRT_HOSPITALIZATION_TRAUMA",
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_FRACTURE_SURGERY_ARM",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_BANDAGE"
          ]
        },
        "IconIndex": 1259,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 2800,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Simple Femur Fracture",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FEMUR_FRACTURE"
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
            "TRT_LEG_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1265,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Open Fracture Femur",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_LEG"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SEVERE_LEG_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BONE_FRACTURE_VISIBLE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_DEPICTION_OF_FEMUR_FRACTURE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HYPOVOLEMIC_SHOCK"
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
            "TRT_HOSPITALIZATION_TRAUMA",
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_FRACTURE_SURGERY_LEG",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_BANDAGE"
          ]
        },
        "IconIndex": 1267,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 2800,
        "Tags": {
          "Tag": "trauma"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Simple Fracture Tibia",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_TIBIA_FRACTURE"
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
            "TRT_LEG_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1271,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Spiral Fracture Tibia",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_TIBIA_SPIRAL_FRACTURE"
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
            "TRT_LEG_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1271,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Simple Fracture Fibula",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
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
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_BRUISE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FIBULA_FRACTURE"
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
            "TRT_LEG_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1271,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Open Fracture Tibia",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_LEG"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SEVERE_LEG_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BONE_FRACTURE_VISIBLE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_SKIN_DAMAGED"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_DEPICTION_OF_TIBIA_FRACTURE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HYPOVOLEMIC_SHOCK"
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
            "TRT_HOSPITALIZATION_TRAUMA",
            "TRT_EMERGENCY_CARE",
            "TRT_ANTIHEMORRHAGICS",
            "TRT_FRACTURE_SURGERY_LEG",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_BANDAGE"
          ]
        },
        "IconIndex": 1273,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 2800,
        "Tags": {
          "Tag": "trauma"
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Ankle Fracture",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ANKLE_INJURY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SPASMS"
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
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LIMITED_LEG_MOTION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ANKLE_FRACTURE"
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
            "TRT_LEG_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1275,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        },
        "WalkAnimSuffix": "_limp",
        "WalkSpeedModifier": 0.5,
        "WalkAnimSuffixTreated": "_crutch"
      },
      {
        "AbbreviationLocID": "Finger Fracture",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_HAND"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_STIFFNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WARMTH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SPASMS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HAND_PAIN"
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HAND_WEAKNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FINGER_FRACTURE"
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
            "TRT_ARM_CAST",
            "TRT_ANALGESICS",
            "TRT_NSAIDS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1279,
        "DepartmentRef": "DPT_ORTHOPAEDICS_AND_TRAUMATOLOGY",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "trauma",
            "clinic"
          ]
        }
      }
    ]
  }
}
