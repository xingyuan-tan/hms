from disease_data import diseases
from pymongo import MongoClient

URL = 'mongodb+srv://HMS-user1:NJq36J0vSngNXtv7@hmscluster.obiqt5i.mongodb.net/?retryWrites=true&w=majority'


client = MongoClient(URL, tlsAllowInvalidCertificates=True)
db = client.patientDatabase
collections = db.HMSCollection

i = 0

for dis in diseases:
    patient = {}

    patient['patient_id']=i
    patient['disease'] = dis
    patient['symptoms'] = {}
    patient['examined'] = {}

    for sym in diseases[dis]['Symptoms']:
        patient['symptoms'][sym['GameDBSymptomRef']] = False

    collections.insert_one(patient)
    # print(patient)
    i+=1


# Helper Function for add_patient
def get_next_sequence_value(sequence_name):
    counter = db.counters
    sequence_value = counter.find_one_and_update(
        {"_id": sequence_name}, {"$inc": {"seq": 1}})
    return sequence_value['seq']

patient_id = get_next_sequence_value("patient_id")