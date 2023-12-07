# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 03:47:45 2023

@author: battl
"""

import json
from pymongo import MongoClient
from disease_data import diseases
from examine_data import examination_list
import random
import csv

client = MongoClient(
    'mongodb+srv://HMS-user1:NJq36J0vSngNXtv7@hmscluster.obiqt5i.mongodb.net/?retryWrites=true&w=majority') # ?retryWrites=true&w=majority
db = client['patientDatabase']
collection = db['HMSCollection']


def generate_patient(target_disease):
    symptoms = {}
    for symptom in diseases[target_disease]:
        if symptom['ProbabilityPercent'] > random.random()*100:
            symptoms[symptom['GameDBSymptomRef']] = False

    # Helper Function for add_patient
    def get_next_sequence_value(sequence_name):
        counter = db.counters
        sequence_value = counter.find_one_and_update(
            {"_id": sequence_name}, {"$inc": {"seq": 1}})
        return sequence_value['seq']

    patient_id = get_next_sequence_value("patient_id")
    generatedPatient = patient(patient_id, target_disease, symptoms)

    collection.insert_one(generatedPatient.__dict__)

print("Patient added to database")

def rip_json(d_json, name='untitled'):
    target = d_json["Database"]["GameDBMedicalCondition"]

    output = {}

    for i in range(len(target)):
        output[target[i]['AbbreviationLocID']]={'Symptoms':target[i]["Symptoms"]['GameDBSymptomRules']}

    with open(str(name)+'.json', 'w') as f:
        json.dump(output, f)
    print("done")

def interview_only():
    with open('json/patientdata.json') as f:
        file_contents = f.read()


    # print(file_contents)

    parsed_json = json.loads(file_contents)


    for i in range(len(parsed_json)):
        l = []

        keys = list(parsed_json[i]['symptoms'].keys())

        for sym in keys:
            if sym in examination_list["EXM_INTERVIEW"]:
                l.append(sym)
        print(l)
        with open('output.csv', 'a') as f1:
            f1.write(str([parsed_json[i]['patient_id']] +l)[1:-1]+'\n')