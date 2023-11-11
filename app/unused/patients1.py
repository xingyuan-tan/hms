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

generatedPatient = patient(patient_id, target_disease, symptoms)

collection.insert_one(generatedPatient.__dict__)

print("Patient added to database")