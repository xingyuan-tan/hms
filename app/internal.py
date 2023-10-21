from data import *


def lab_examine_backend(patient_id, examination, conn):
    patient_id = int(patient_id)

    target_patient = conn.find_one({'patient_id': patient_id}, {'_id': 0})

    res = _lab_examine(target_patient, examination)

    conn.update_one({'patient_id': patient_id}, {"$set": {"examined." + examination: ''.join(res)}})

    return


def _lab_examine(target_patient, examination):
    set_patient_sym = set(target_patient['symptoms'])
    set_exam_result = set(examination_list[examination])

    return set_patient_sym.intersection(set_exam_result)


########## HELPER FUNCTIONS ################# =========================================================

# get patient by id helper function
def getPatientByID_helper_function(patient_id, conn):
    patient = conn.find_one({'patient_id': patient_id})
    if patient:
        patient_dict = {
            'patient_id': patient['patient_id'],
            'disease': patient["disease"],
            'symptoms': patient['symptoms'],
            'examined': patient['examined'],
        }
        return patient_dict


# Filter Diagnoses based on examinations done Function

def update_diagnoses(examined):
    diagnoses = list(diseases.keys())
    # if examined is empty, return diseases
    if not examined:
        return diagnoses

    else:
        for exam in examined:
            # exam done is in lab_examination and is true, return disease that contains that symptom
            if exam in examination_list and examined[exam]:
                diagnosis = check_symptom(examined[exam])
                return diagnosis

            # exam done is in doctor_examination and is true, return diseases that contain that symptom
            elif exam in examination_list and examined[exam]:
                diagnoses = check_symptom(examined[exam])
                return diagnoses

            # else, eliminate diseases that contain that symptom
            else:
                not_diseases = check_exam(exam)
                for disease in not_diseases:
                    diagnoses.remove(disease)
                return diagnoses


def check_symptom(symptom_checked):
    return_diseases = []
    for disease in diseases:
        for symptom in diseases[disease]:
            if symptom['GameDBSymptomRef'] == symptom_checked:
                return_diseases.append(disease)
    return return_diseases


def check_symptom_1(symptom_checked):
    return_diseases = []
    for disease in diseases:
        for symptom in diseases[disease]:
            if symptom['GameDBSymptomRef'] == symptom_checked and symptom['ProbabilityPercent'] == 1.00:
                return_diseases.append(disease)
    return return_diseases


def check_exam(exam):
    not_symptoms = examination_list[exam]

    not_diseases = []
    for symptom in not_symptoms:
        not_diseases += check_symptom_1(symptom)
    return not_diseases
