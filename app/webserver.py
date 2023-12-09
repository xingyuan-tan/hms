from flask import Response, make_response, request, Flask, render_template, jsonify
from pymongo import MongoClient

from examine_data import *
from internal import *

URL = 'mongodb+srv://HMS-user1:NJq36J0vSngNXtv7@hmscluster.obiqt5i.mongodb.net/?retryWrites=true&w=majority'
EXAM_LIST = set(examination_list.keys())

# initialize a flask object
app = Flask(__name__, template_folder='../templates', static_folder='../templates/static/')

client = MongoClient(URL, tlsAllowInvalidCertificates=True)
db = client.patientDatabase
collections = db.HMSCollection


@app.route("/")
def home():
    return render_template("home.html")


# Doctor page
@app.route("/doctor")
def doctor():

    patient_list = []

    for patient in list(collections.find()):
        patient_list.append(patient["patient_id"])

    return render_template("doctor.html", patient_list=patient_list)


# Get One Patient by ID
@app.route('/patient-data/<int:patient_id>', methods=['GET'])
def get_patient_by_id(patient_id):

    patient = collections.find_one({'patient_id': patient_id})

    examined = patient['examined']
    symptoms = patient['symptoms']
    patient_diagnoses = update_diagnoses(examined, symptoms)

    if patient:
        possible_list = EXAM_LIST.difference(set(patient['examined']))

        patient_dict = {
            'patient_id': patient['patient_id'],
            'disease': patient["disease"],
            'symptoms': patient['symptoms'],
            'examined': patient['examined'],
            'possible_exam': list(possible_list),
        }
        return jsonify(
            {
                "code": 200,
                "message": "Retrieved 1 Patient",
                "data": {
                    "patient": patient_dict,
                    "diagnoses": patient_diagnoses
                }
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 400,
                "message": "Patient not found"
            }
        ), 400


# Update Patient Details
@app.route('/patient-data/<int:patient_id>', methods=['PUT'])
def edit_patient_info(patient_id):
    try:
        data = request.get_json()
        # patient_id = data["patient_id"]
        examined = data['examined']

        collections.update_one({"patient_id": patient_id}, {
                              "$set": {"examined": examined}})
        print("updated")
        return jsonify({
                "code": 200,
                "message": "Updated Patient Examination Details",
                "data": {
                    "patient": getPatientByID_helper_function(patient_id, collections)
                }
            }), 200
    except:
        return jsonify(
            {
                "code": 400,
                "message": "Error updating patient details",
            }
        ), 400


@app.route("/neutral")
def neutral():

    db_iterator = collections.find()
    patient_list = []

    for p in db_iterator:
        patient_list.append(p['patient_id'])

    return render_template("neutral.html", patient_list=patient_list)



# @app.route("/examine")
# def examine():
#     params = request.args

#     # CHECK IF THE EXAMINATION AND PATIENT ID IS VALID
#     patient_id = params.get('patient_id')
#     examination = params.get('examination')

#     print(patient_id, examination)

#     if not patient_id and not examination:

#         return ('bad request', 400)

#     lab_examine_backend(patient_id, examination)

#     return ('success', 200)

@app.route("/examine", methods=['POST'])
def examine():
    data = request.get_json()
    patient_id = data['patient_id']
    examination = data['examination']

    if patient_id == None or not examination:
        return ('bad request', 400)

    lab_examine_backend(patient_id, examination, collections)

    return ('success', 200)

app.run(port=5000, debug=True, threaded=True, host='0.0.0.0')




# if __name__ == '__main__':
#     # construct the argument parser and parse command line arguments
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-i", "--ip", type=str, required=True,
#         help="ip address of the device")
#     ap.add_argument("-o", "--port", type=int, required=True,
#         help="ephemeral port number of the server (1024 to 65535)")
#     ap.add_argument("-f", "--frame-count", type=int, default=32,
#         help="# of frames used to construct the background model")
#     args = vars(ap.parse_args())
#
#     # Initialise the DB
#
#     # start a thread that will perform motion detection
#     t = threading.Thread(target=detect_motion, args=(
#         args["frame_count"],))
#     t.daemon = True
#     t.start()
#     # start the flask app
#     app.run(host=args["ip"], port=args["port"], debug=True,
#         threaded=True, use_reloader=False)