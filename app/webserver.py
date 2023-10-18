from flask import Response, make_response, request, Flask, render_template, jsonify
from pymongo import MongoClient

from internal import *

URL = 'mongodb+srv://HMS-user1:NJq36J0vSngNXtv7@hmscluster.obiqt5i.mongodb.net/?retryWrites=true&w=majority'

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

    db_iterator = collections.find()
    patient_list = []

    for p in db_iterator:
        patient_list.append(p['patient_id'])

    return render_template("doctor.html", patient_list=patient_list)


@app.route("/neutral")
def neutral():

    db_iterator = collections.find()
    patient_list = []

    for p in db_iterator:
        patient_list.append(p['patient_id'])

    return render_template("neutral.html", patient_list=patient_list)


@app.route("/patient-data/<int:patient_id>")
def patient_data(patient_id):

    result = collections.find_one({'patient_id':patient_id},{'_id':0})

    if result is not None:
        return jsonify(result)

    return ('', 204)


@app.route("/examine")
def examine():
    params = request.args

    # CHECK IF THE EXAMINATION AND PATIENT ID IS VALID
    patient_id = params.get('patient_id')
    examination = params.get('examination')

    print(patient_id, examination)

    if not patient_id and not examination:

        return ('bad request', 400)

    lab_examine_backend(patient_id, examination)

    return ('success', 200)

app.run(port=5000, debug=True, threaded=True)




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


