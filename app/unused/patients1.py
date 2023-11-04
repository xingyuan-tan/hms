from pymongo import MongoClient
import random
from disease import *

client = MongoClient(
    'mongodb+srv://HMS-user1:NJq36J0vSngNXtv7@hmscluster.obiqt5i.mongodb.net/?retryWrites=true&w=majority') # ?retryWrites=true&w=majority
db = client['patientDatabase']
collection = db['HMSCollection']

# Patient Class
class patient:

    def __init__(self, patient_id, disease, symptoms={}): # patient_id,
        self.patient_id = patient_id
        self.disease = disease
        self.symptoms = symptoms
        self.examined = {}

target_disease = 'Bronchitis'

symptoms = {}
for symptom in diseases[target_disease]:
    if symptom['ProbabilityPercent'] > random.random():
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