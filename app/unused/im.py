target = {
  "Database": {
    "GameDBMedicalCondition": [
      {
        "AbbreviationLocID": "Salmonellosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEMATOCHEZIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ABDOMINAL_CRAMPS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SALMONELLOSIS_CONFIRMED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 15,
              "GameDBSymptomRef": "SYM_DEHYDRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BACTEREMIA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_STOOL_ANALYSIS_SAMPLING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTIDIARRHEALS",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_REHYDRATION",
            "TRT_STOMACHICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1143,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Amoebiasis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_CRAMPS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_EXCESSIVE_BURPING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FLATULENCE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_E._HISTOLYTICA_DISCOVERED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTIDIARRHEALS",
            "TRT_STOMACHICS",
            "TRT_SPASMOLYTICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1145,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Giardiasis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_CRAMPS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FLATULENCE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_GIARDIA_LAMBLIA_DISCOVERED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DEHYDRATION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_REHYDRATION",
            "TRT_SPASMOLYTICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1147,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Pulmonary mycobacterial infection",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
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
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NIGHT_SWEATS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LOSS_OF_APETITE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_MAC_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_SEPTIC_SHOCK"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 15,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_CHEST_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CRP",
            "EXM_X_RAY_TORSO",
            "EXM_MRI",
            "EXM_CBC_SAMPLING",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANTITUSICS",
            "TRT_ANTIPYRETICS",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_THORACENTESIS"
          ]
        },
        "IconIndex": 1149,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1000,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Infectious mononucleosis",
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
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 00,
              "GameDBSymptomRef": "SYM_PETECHIAE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_PURPURA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPHAGIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NIGHT_SWEATS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_EBV_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_NECK_PALPATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_TORSO",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_CORTICOSTEROIDS",
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 1041,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Histoplasmosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_RARE",
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
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_PAINFUL_CERVICAL_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HISTOPLASMA_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_X_RAY_TORSO",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIMYCOTICS",
            "TRT_ANTITUSICS",
            "TRT_NSAIDS",
            "TRT_REST",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1029,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Aspergillosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ASPERGILLOMA_DISCOVERED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 10,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_MRI",
            "EXM_X_RAY_TORSO",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANTIMYCOTICS",
            "TRT_THORACENTESIS",
            "TRT_OXYGENOTHERAPY",
            "TRT_NSAIDS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1163,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Hemolytic anaemia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_PALE_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_JAUNDICE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DARK_URINE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HAPTOGLOBIN_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_URINE_SAMPLE_ANALYSIS_SAMPLING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_DIET_MODIFICATION",
            "TRT_ANTIPYRETICS",
            "TRT_BRONCHODILATORS"
          ]
        },
        "IconIndex": 1035,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Thrombocytopenia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 00,
              "GameDBSymptomRef": "SYM_PURPURA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PETECHIAE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_HEMATURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_PROLONGED_BLEEDING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_THROMBOCYTOPENIA_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_URINE_SAMPLE_ANALYSIS_SAMPLING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_PLATELET_TRANSFUSION",
            "TRT_DIET_MODIFICATION"
          ]
        },
        "IconIndex": 2798,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Hemophilia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEMATURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEMATOCHEZIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PURPURA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_PROLONGED_BLEEDING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CLOTTING_FACTOR_LOW"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_URINE_SAMPLE_ANALYSIS_SAMPLING",
            "EXM_STOOL_ANALYSIS_SAMPLING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_DESMOPRESSIN",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1169,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Thalassaemia",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_PALE_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_JAUNDICE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DARK_URINE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_SWELLING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_THALASSEMIA_DISCOVERED"
            },
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_URINE_SAMPLE_ANALYSIS_SAMPLING",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_BLOOD_TRANSFUSION",
            "TRT_BETA_BLOCKERS"
          ]
        },
        "IconIndex": 2800,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1300,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Sarcoidosis - Lungs",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 10,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_GRANULOMAS_LUNGS"
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
            "EXM_THORAX_PERCUSSION",
            "EXM_MRI",
            "EXM_X_RAY_TORSO",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROIDS",
            "TRT_THORACENTESIS",
            "TRT_NSAIDS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1171,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Sarcoidosis - Eye",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_RED_EYE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PHOTOPHOBIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_GRANULOMAS_EYES"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_NEUROLOGICAL_TESTING",
            "EXM_OPHTHALMOSCOPY",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROIDS",
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1175,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Sarcoidosis - Heart",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_EDEMA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_FAINTING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PALPITATIONS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_GRANULOMAS_HEART"
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
            "EXM_THORAX_PERCUSSION",
            "EXM_NEUROLOGICAL_TESTING",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_CORTICOSTEROIDS",
            "TRT_NSAIDS",
            "TRT_OXYGENOTHERAPY",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_BETA_BLOCKERS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1173,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1800,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Diabetes",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_POLYURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_HUNGER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_THIRST"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HYPERLIPIDEMIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HIGH_SUGAR_LEVEL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_ATHEROSCLEROSIS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ECHO",
            "EXM_CC_ECHO",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_INSULIN_THERAPY",
            "TRT_DIET_MODIFICATION",
            "TRT_ACE_INHIBITOR",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1177,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Cystic Fibrosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_CONSTIPATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HIGH_CHLORIDE_LEVEL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_OSTEOPOROSIS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_CHEST_LISTENING",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CT",
            "EXM_SWEAT_CHLORIDE_TEST",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_BRONCHODILATORS",
            "TRT_BONE_STRENGTH_PILLS",
            "TRT_PURGATIVES"
          ]
        },
        "IconIndex": 1179,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Otitis Externa",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_OTALGIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RINGING_IN_THE_EARS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_EDEMA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEARING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ITCHING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_EAR_CANAL"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_EAR_CANAL_INFECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_AUDIOMETRY",
            "EXM_EAR_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_EAR_DROPS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1181,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Acute Suppurative Otitis Media",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_OTALGIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIMINISHED_HEARING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_EAR_CANAL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_EAR_FLUID_DRAINAGE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_TYMPANIC_MEMBRANE_INFLAMMED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_AUDIOMETRY",
            "EXM_EAR_EXAMINATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_EAR_DROPS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1183,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Acute Mastoiditis",
        "Duration": 3,
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
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_EAR_FLUID_DRAINAGE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_OTALGIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_EAR_LOBE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_MASTOID_CELLS_INFECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_DIMINISHED_HEARING"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_EAR_EXAMINATION",
            "EXM_AUDIOMETRY",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1185,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Pneumonia",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TREMOR"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWEATING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_LEUKOCYTOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_MUSCLE_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PNEUMONIC_LUNGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BACTEREMIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_EXHAUSTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_CRP",
            "EXM_CBC_SAMPLING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_X_RAY_TORSO",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_ANTIPYRETICS",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_ANALGESICS",
            "TRT_THORACENTESIS",
            "TRT_NSAIDS",
            "TRT_REST"
          ]
        },
        "IconIndex": 1191,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1500,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Bronchopneumonia",
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
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NIGHT_SWEATS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWEATING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_LEUKOCYTOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LUNG_TISSUE_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BACTEREMIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_EXHAUSTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CRP",
            "EXM_CBC_SAMPLING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_MRI",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_ANTIPYRETICS",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_THORACENTESIS",
            "TRT_ANALGESICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 2804,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1500,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Bronchiectasis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_BAD_BREATH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_PALE_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_A1AT_DEFICIENCY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_LEUKOCYTOSIS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_AIRWAYS_INFECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BACTEREMIA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_CHEST_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_CBC_SAMPLING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_BRONCHODILATORS",
            "TRT_MUCOLYTICS",
            "TRT_ANTIPYRETICS",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1193,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 800,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Simple Chronic Bronchitis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CONSTANT_BRONCHIAL_INFECTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_A1AT_DEFICIENCY"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_X_RAY_TORSO",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTITUSICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1047,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Emphysema",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_A1AT_DEFICIENCY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_ANXIETY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_EMPHYSEMA_DISCOVERED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_CT",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_OXYGENOTHERAPY",
            "TRT_BRONCHODILATORS",
            "TRT_ANTIPYRETICS",
            "TRT_A1AT_REPLACEMENT",
            "TRT_THORACENTESIS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 2802,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Chronic obstructive pulmonary disease",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ANXIETY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_A1AT_DEFICIENCY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OBSTRUCTED_AIRWAYS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_CRP",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_SPIROMETRY",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_OXYGENOTHERAPY",
            "TRT_BRONCHODILATORS",
            "TRT_ANTITUSICS",
            "TRT_A1AT_REPLACEMENT",
            "TRT_BETA_BLOCKERS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1179,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1200,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Asthma",
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
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SLEEPING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ANXIETY"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BRONCHIAL_HYPERREACTIVITY"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_SPIROMETRY",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_BRONCHODILATORS",
            "TRT_ANTITUSICS",
            "TRT_SLEEPING_DRUGS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1047,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Pneumothorax",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PALE_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PULMONARY_DAMAGE"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_X_RAY_TORSO",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_THORACENTESIS",
            "TRT_OXYGENOTHERAPY",
            "TRT_ANALGESICS",
            "TRT_ANTI_ARRHYTMICALS",
            "TRT_BRONCHODILATORS"
          ]
        },
        "IconIndex": 1195,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 3600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Cellulitis",
        "Duration": 2,
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_REDNESS_OF_SKIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PAINFUL_VESICULAR_RASH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_STREP_SKIN_INFECTION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_NUMBING_OINTMENT",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1051,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Lupus",
        "Duration": 6,
        "OccurrenceRef": "OCCURRENCE_RARE",
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 45,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_PROTEINURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEMATURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_LEUKOPENIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LUPUS_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BUTTERFLY_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_ANEMIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BRADYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_CRP",
            "EXM_URINE_SAMPLE_ANALYSIS_SAMPLING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_CBC_SAMPLING",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_EVALUATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_CORTICOSTEROIDS",
            "TRT_NSAIDS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_BETA_BLOCKERS"
          ]
        },
        "IconIndex": 1197,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Pulmonary Contusion - Blunt",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_CHEST"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPOTENSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BLUNT_PULMONARY_CONTUSION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_BLOOD_PRESSURE_AND_PULSE_MEASUREMENT",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_MRI",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_EMERGENCY_CARE",
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_OXYGENOTHERAPY",
            "TRT_THORACENTESIS",
            "TRT_ANALGESICS",
            "TRT_ANTI_ARRHYTMICALS"
          ]
        },
        "IconIndex": 1201,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1300,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Carbon Monoxide Poisoning",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HALLUCINATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLE_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LOSS_OF_VISION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CARBOXYHEMOGLOBIN_HIGH_LEVEL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_RESPIRATORY_FAILURE"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_EEG",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_OPHTHALMOSCOPY",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_OXYGENOTHERAPY",
            "TRT_ARTIFICIAL_VENTILATION",
            "TRT_BETA_BLOCKERS",
            "TRT_ANALGESICS",
            "TRT_ANTI_ARRHYTMICALS"
          ]
        },
        "IconIndex": 1203,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1700,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Chlorine Gas Poisoning",
        "Duration": 3,
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SNEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RED_EYE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CREATINE_KINASE_HIGH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CHLORINE_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_RESPIRATORY_FAILURE"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_CHEST_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_EEG",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_OXYGENOTHERAPY",
            "TRT_BRONCHODILATORS",
            "TRT_HOSPITALIZATION_ICU",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1203,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1900,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Methanol Poisoning",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LOSS_OF_VISION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ACIDOSIS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_FORMATE_TOXIC_LEVEL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_COMA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_SPEECH_LISTENING",
            "EXM_OPHTHALMOSCOPY",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_ETHANOL_DOSES",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_TRANQUILIZERS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1203,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1100,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Lead Poisoning",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SLEEPING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TREMOR"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HALLUCINATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLE_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LEAD_LEVELS_HIGH"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_EEG",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_CHELATION_THERAPY",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1203,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1500,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Pleurisy",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLE_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_SWELLING_JOINTS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BACTERIAL_INFECTION_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_THORAX_PERCUSSION",
            "EXM_CHEST_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_MRI",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_THORACENTESIS",
            "TRT_BRONCHODILATORS",
            "TRT_ANTIPYRETICS",
            "TRT_ANTI_ARRHYTMICALS",
            "TRT_ANTITUSICS",
            "TRT_STOMACHICS"
          ]
        },
        "IconIndex": 2248,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Asbestosis",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WHEEZING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_ASBESTOSIS_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_CRP",
            "EXM_X_RAY_TORSO",
            "EXM_CT",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_OXYGENOTHERAPY",
            "TRT_ANALGESICS",
            "TRT_BRONCHODILATORS"
          ]
        },
        "IconIndex": 2250,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2200,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Miliaria",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH_ON_NECK"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH_ON_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH_ON_TORSO"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWEATING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HEAT_RASH"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_EVALUATION",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_STEROID_TOPICAL_CREAM",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2252,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Ciguatera Fish Poisoning",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NUMBNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ITCHING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HYPOTENSION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CIGUATOXIN_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_PRESSURE_AND_PULSE_MEASUREMENT",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_MANNITOL_DOSES",
            "TRT_STOMACHICS",
            "TRT_ANTIHISTAMINES",
            "TRT_ANALGESICS",
            "TRT_ANTI_ARRHYTMICALS"
          ]
        },
        "IconIndex": 2254,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1200,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Pleural Empyema",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PLEURAL_FLUID_INFECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_MRI",
            "EXM_X_RAY_TORSO",
            "EXM_BIOPSY_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_THORACENTESIS",
            "TRT_OXYGENOTHERAPY",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANTITUSICS"
          ]
        },
        "IconIndex": 2256,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2500,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Chylothorax",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CHYLOTHORAX_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_MRI",
            "EXM_X_RAY_TORSO",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_THORACENTESIS",
            "TRT_BRONCHODILATORS",
            "TRT_ANALGESICS",
            "TRT_ANTITUSICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 2258,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Parapneumonic Effusion",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_PLEURAL_EFFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PLEURAL_TRANSUDATE"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_X_RAY_TORSO",
            "EXM_MRI",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_THORACENTESIS",
            "TRT_ANTIPYRETICS",
            "TRT_BRONCHODILATORS",
            "TRT_NSAIDS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 2260,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Cholesteatoma",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEARING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIMINISHED_HEARING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RINGING_IN_THE_EARS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_EAR_CANAL"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_OTALGIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CHOLESTEATOMA_DISCOVERED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_EAR_EXAMINATION",
            "EXM_AUDIOMETRY",
            "EXM_CT"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_MIEP",
            "TRT_EAR_DROPS",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2262,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Croup",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NASAL_CONGESTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HOARSENESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_CROUP_PRESENT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_NASAL_CAVITY_INSPECTION",
            "EXM_CHEST_LISTENING",
            "EXM_EVALUATION"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_CORTICOSTEROIDS",
            "TRT_BRONCHODILATORS",
            "TRT_ANTIPYRETICS",
            "TRT_SALINE_NASAL_SPRAY"
          ]
        },
        "IconIndex": 2264,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Nasal Polyp",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NASAL_CONGESTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SNEEZING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_NASAL_POLYPS_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_NASAL_CAVITY_INSPECTION",
            "EXM_CHEST_LISTENING",
            "EXM_CT"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_MIEP",
            "TRT_BRONCHODILATORS",
            "TRT_SALINE_NASAL_SPRAY",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2266,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1800,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Meniere's Disease",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEARING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RINGING_IN_THE_EARS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_FREQUENT_FALLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_SWEATING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ANXIETY"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_MENIERES_DISEASE_PRESENT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_EAR_EXAMINATION",
            "EXM_AUDIOMETRY",
            "EXM_EVALUATION"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_DIURETICS",
            "TRT_EAR_DROPS",
            "TRT_STOMACHICS",
            "TRT_ANXIOLYTICS",
            "TRT_DOCTOR'S_RECOMMENDATIONS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2268,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Essential Thrombocythemia",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NUMBNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_NOSEBLEEDS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SLURRED_SPEECH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BLURRED_VISION"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_THROMBOCYTHEMIA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_THORAX_PERCUSSION",
            "EXM_BASIC_VISUAL_TEST",
            "EXM_CBC_SAMPLING"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_HYDROXYUREA",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 2270,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 900,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Poison Ivy Rash",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_REDNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_ITCHING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWELLING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_POISON_IVY_RASH"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_EVALUATION"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_STEROID_TOPICAL_CREAM",
            "TRT_ANTIPYRETICS",
            "TRT_BRONCHODILATORS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 2272,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 200,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Hemothorax",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIZZINESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_CHEST"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_HEMOTHORAX_DISCOVERED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
           "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_USG",
            "EXM_FAST",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_THORACENTESIS",
            "TRT_ANALGESICS",
            "TRT_OXYGENOTHERAPY",
            "TRT_ANTI_ARRHYTMICALS"
          ]
        },
        "IconIndex": 2274,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1800,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Tension Pneumothorax",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_TACHYCARDIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPOTENSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CYANOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DYSPNEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PUNCTURED_LUNGS"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_THORAX_PERCUSSION",
            "EXM_CHEST_LISTENING",
            "EXM_BLOOD_PRESSURE_AND_PULSE_MEASUREMENT",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_USG",
            "EXM_FAST"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_THORACENTESIS",
            "TRT_ANALGESICS",
            "TRT_BRONCHODILATORS",
            "TRT_OXYGENOTHERAPY",
            "TRT_ANTI_ARRHYTMICALS"
          ]
        },
        "IconIndex": 2276,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1800,
        "Tags": {
          "Tag": "trauma"
        }
      },
      {
        "AbbreviationLocID": "Classical Cholera",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_DEHYDRATION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_CRAMPS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_IRRITABILITY"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_THIRST"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_OLIGURIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPOTENSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_VIBRIO_CHOLERAE_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_BLOOD_PRESSURE_AND_PULSE_MEASUREMENT",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_BETA_BLOCKERS",
            "TRT_REHYDRATION",
            "TRT_REST"
          ]
        },
        "IconIndex": 1139,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1000,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Typhoid Fever",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_TENDERNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SALMONELLA_TYPHI_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 40,
              "GameDBSymptomRef": "SYM_EXHAUSTION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_GASTROSCOPY",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_DIET_MODIFICATION",
            "TRT_ANALGESICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 1141,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1100,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Tuberculosis of Lung",
        "Duration": 5,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 80,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_WEIGHT_LOSS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NIGHT_SWEATS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LOSS_OF_APETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_LEUKOCYTOSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CRP_HIGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_M._TUBERCULOSIS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_EXHAUSTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CRP",
            "EXM_CBC_SAMPLING",
            "EXM_X_RAY_TORSO",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_REST"
          ]
        },
        "IconIndex": 1149,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Tularaemia",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_PAINFUL_CERVICAL_LYMPH_NODES"
            },
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
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_F._TULARENSIS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_EXHAUSTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 10,
              "GameDBSymptomRef": "SYM_SEPTIC_SHOCK"
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
            "EXM_THORAX_PERCUSSION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_CBC_SAMPLING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_INTRAVENOUS_INFUSION",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 1151,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1200,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Pulmonary Anthrax",
        "Duration": 5,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SORE_THROAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SWALLOW_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LUNG_FINDINGS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_B._ANTHRACIS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_BACTEREMIA"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ORAL_CAVITY_INSPECTION",
            "EXM_NECK_PALPATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_X_RAY_TORSO",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_CC_BLOOD_ANALYSIS",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS",
            "TRT_NSAIDS"
          ]
        },
        "IconIndex": 1153,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Rat-bite Fever",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_RASH_ON_ARM"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_STREPTOBACILLUS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANALGESICS",
            "TRT_BETA_BLOCKERS",
            "TRT_ANTIPYRETICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1155,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Cat-Scratch Disease",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_RARE",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_BACK_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_B._HENSELAE_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_NECK_PALPATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANALGESICS",
            "TRT_BETA_BLOCKERS",
            "TRT_REST",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1157,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Pertussis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_NASAL_CONGESTION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_RED_EYE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_IRRITABLE_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_B._PERTUSSIS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_DEHYDRATION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_NASAL_CAVITY_INSPECTION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_BACTERIA_CULTIVATION_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANTITUSICS",
            "TRT_REHYDRATION"
          ]
        },
        "IconIndex": 1159,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Legionnaires Disease",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPERPYREXIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SPUTUM_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CHEST_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEMOPTYSIS"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LEGIONELLA_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_SPEECH_LISTENING",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_THORAX_PERCUSSION",
            "EXM_PCR_SAMPLING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_HIGH_PRIORITY",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANTITUSICS",
            "TRT_ANALGESICS",
            "TRT_REST"
          ]
        },
        "IconIndex": 1161,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Typhus Fever",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_R._TYPHI_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_DEHYDRATION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CHEST_LISTENING",
            "EXM_BLOOD_TEST_SAMPLING",
            "EXM_GASTROSCOPY",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_REHYDRATION",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1029,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 2700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "American Trypanosomiasis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
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
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DIARRHEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_TRYPANOSOMA_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 30,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_ECG",
            "EXM_ECHO",
            "EXM_CC_ECHO",
            "EXM_HEART_MONITORING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANTIPARASITIC_DRUGS",
            "TRT_BETA_BLOCKERS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1165,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1700,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Toxoplasmosis",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_CONFUSION"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_TOXOPLASMOSIS_DETECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_RED_EYE"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_SPEECH_LISTENING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_ANTIPARASITIC_DRUGS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1157,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 600,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Babesios",
        "Duration": 2,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
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
              "GameDBSymptomRef": "SYM_MALAISE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_CHILLS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_NAUSEA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_ABDOMINAL_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_DRY_COUGH"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_BABESIOSIS_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_CHEST_LISTENING",
            "EXM_ABDOMINAL_PALPATION",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_PCR_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_ANALGESICS"
          ]
        },
        "IconIndex": 1167,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 500,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Lyme Disease",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_RASH"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_LEUKOPENIA"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_VOMITING"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_IRREGULAR_HEARTBEAT"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_BREATHING_DIFFICULTIES"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_LYME_DISEASE_DETECTED"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_CHEST_LISTENING",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_CBC_SAMPLING",
            "EXM_ECG",
            "EXM_HEART_MONITORING",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_NORMAL",
            "TRT_INTRAVENOUS_ANTIBIOTICS",
            "TRT_BETA_BLOCKERS",
            "TRT_ANALGESICS",
            "TRT_ANTIPYRETICS"
          ]
        },
        "IconIndex": 1167,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 1000,
        "Tags": {
          "Tag": "disease"
        }
      },
      {
        "AbbreviationLocID": "Mumps",
        "Duration": 3,
        "OccurrenceRef": "OCCURRENCE_UNCOMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FEVER"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_HEADACHE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_SWOLLEN_LYMPH_NODES"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_SWALLOW_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 60,
              "GameDBSymptomRef": "SYM_MUSCLES_AND_JOINTS_PAIN"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_WEAKNESS"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_FATIGUE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 50,
              "GameDBSymptomRef": "SYM_LOSS_OF_APPETITE"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PAROTID_INFECTED"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 20,
              "GameDBSymptomRef": "SYM_DIMINISHED_HEARING"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_TEMPERATURE_MEASUREMENT",
            "EXM_NECK_PALPATION",
            "EXM_AUDIOMETRY",
            "EXM_SEROLOGY_TESTING_SAMPLING",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_ANTIBIOTICS",
            "TRT_ANTIPYRETICS",
            "TRT_REST",
            "TRT_ANALGESICS",
            "TRT_HOME_TREATMENT"
          ]
        },
        "IconIndex": 1189,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 300,
        "Tags": {
          "Tag": [
            "disease",
            "clinic"
          ]
        }
      },
      {
        "AbbreviationLocID": "Pulmonary Laceration - Penetrating",
        "Duration": 4,
        "OccurrenceRef": "OCCURRENCE_COMMON",
        "Symptoms": {
          "GameDBSymptomRules": [
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_INJURY_TO_THE_CHEST"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_SEVERE_HEMORRHAGE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 70,
              "GameDBSymptomRef": "SYM_HYPOVOLEMIC_SHOCK"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 0,
              "GameDBSymptomRef": "SYM_PNEUMATOCELE"
            },
            {
              "DayOfFirstOccurence": 0,
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_OPEN_WOUND"
            },
            {
              "ProbabilityPercent": 100,
              "GameDBSymptomRef": "SYM_PENETRATING_PULMONARY_LACERATION"
            }
          ]
        },
        "Examinations": {
          "ExaminationRef": [
            "EXM_INTERVIEW",
            "EXM_PHYSICAL_AND_VISUAL_EXAMINATION",
            "EXM_FAST",
            "EXM_DIFFERENTIAL_DIAGNOSIS"
          ]
        },
        "Treatments": {
          "TreatmentRef": [
            "TRT_HOSPITALIZATION_TRAUMA",
            "TRT_EMERGENCY_CARE",
            "TRT_PULMONARY_SURGERY",
            "TRT_ANALGESICS",
            "TRT_BLOOD_TRANSFUSION"
          ]
        },
        "IconIndex": 1199,
        "DepartmentRef": "DPT_INTERNAL_MEDICINE_DEPARTMENT",
        "InsurancePayment": 3100,
        "Tags": {
          "Tag": "trauma"
        }
      }
    ]
  }
}

