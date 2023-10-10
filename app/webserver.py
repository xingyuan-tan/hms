from flask import Response, request, Flask, render_template, jsonify
import os
from patient import patients

# initialize a flask object
app = Flask(__name__, template_folder='../templates', static_folder='../templates/static/')


@app.route("/")
def home():
    return render_template("home.html")

# Doctor page
@app.route("/doctor")
def doctor():
    patient_list = []
    for patient in patients:
        patient_list.append(patient.patient_id)

    return render_template("doctor.html", patient_list=patient_list)

# Neural page
@app.route("/neutral")
def neutral():
    return render_template("neutral.html")

@app.route("/patient-data/<int:patient_id>")
def patient_data(patient_id):
    for p in patients:
        if p.patient_id == patient_id:
            return jsonify(p.serialise())
    return ('', 204)

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


