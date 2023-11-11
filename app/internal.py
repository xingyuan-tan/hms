from examine_data import *
from disease_data import *

def lab_examine_backend(patient_id, examination, conn):
    patient_id = int(patient_id)

    target_patient = conn.find_one({'patient_id': patient_id}, {'_id': 0})

    res = _lab_examine(target_patient, examination)

    conn.update_one({'patient_id': patient_id}, {"$set": {"examined." + examination: ' '.join(res)}})

    update_symptoms(patient_id, examination, conn)

    return


def _lab_examine(target_patient, examination):
    set_patient_sym = set(target_patient['symptoms'])
    set_exam_result = set(examination_list[examination])

    print(set_patient_sym.intersection(set_exam_result))

    return set_patient_sym.intersection(set_exam_result)


# Update the symptoms of this patient
def update_symptoms(patient_id, examination_done, conn):
    target_patient = conn.find_one({'patient_id': patient_id}, {'_id': 0})
    patient_symptoms = target_patient['symptoms']

    # get the symptoms of the examination done
    exam_symptoms = examination_list[examination_done]

    # update the patient's symptoms
    for symptom in exam_symptoms:
        if symptom in patient_symptoms:
            patient_symptoms[symptom] = True

    # update the patient's symptoms in the database
    conn.update_one({'patient_id': patient_id}, {"$set": {"symptoms": patient_symptoms}})

    return

########## HELPER FUNCTIONS ################# =========================================================


# Filter Diagnoses based on examinations done Function

def update_diagnoses(examined, symptoms):

    diagnoses = []
    # if examined is empty, return diseases
    if not examined:
        return None

    for symptom in symptoms:
        if symptoms[symptom]:
            if check_symptom_1(symptom):
                return check_symptom_1(symptom)
            diagnoses += check_symptom(symptom)

    for disease in diagnoses:
        for symptom in symptoms: 
            if symptom not in get_symptoms(disease) and disease in diagnoses and symptoms[symptom]:
                diagnoses.remove(disease)
    
    # print(diagnoses)
    if diagnoses == []:
        diagnoses = list(diseases.keys())

    for exam, revealed_symptoms in examined.items():
        # If examined but revealed no symptoms, remove diseases that have the symptoms this exam reveals
        if not revealed_symptoms:
            not_diseases = check_not_diseases(exam)
            for disease in not_diseases:
                if disease in diagnoses:
                    diagnoses.remove(disease)

    return list(set(diagnoses))
        


def check_symptom(symptom_checked):
    return_diseases = []
    for disease in diseases:
        for symptom in diseases[disease]['Symptoms']:
            if symptom['GameDBSymptomRef'] == symptom_checked:
                return_diseases.append(disease)
    return return_diseases


def check_symptom_1(symptom_checked):
    return_diseases = []
    for disease in diseases:
        for symptom in diseases[disease]['Symptoms']:
            if symptom['GameDBSymptomRef'] == symptom_checked and symptom['ProbabilityPercent'] == 100:
                return_diseases.append(disease)
    return return_diseases


def check_not_diseases(exam):
    not_symptoms = examination_list[exam]
    # print("Not Symptoms ===================================================================")
    # print(not_symptoms)
    not_diseases = []
    for symptom in not_symptoms:
        not_diseases += check_symptom_1(symptom)
    # print(not_diseases)
    return not_diseases


def get_symptoms(disease):
    return_symptoms = []
    for disease in diseases:
        for symptom in diseases[disease]['Symptoms']:
            return_symptoms.append(symptom['GameDBSymptomRef'])
    return return_symptoms