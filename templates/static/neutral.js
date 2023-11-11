var btnFetchPatient = document.getElementById("fetch-patient");
var btnSendExamine = document.getElementById("send-examine");
var selectedPatient = document.getElementById("selected-patient");
var selectedExamine = document.getElementById("selected-examine");

const URL = window.location.host;

btnSendExamine.onclick = function() {
    console.log("Sending examination");
    fetch('http://' + URL + '/examine?patient_id='+selectedPatient.value+'&examination='+selectedExamine.value);
    //update info screen
};

btnFetchPatient.onclick = function () {
    console.log('Fetch Patient');
    fetch('http://' + URL + '/patient-data/' + selectedPatient.value)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .catch(() => {
                        // Couldn't parse the JSON
                        throw new Error(response.status);
                    })
                    .then(({message}) => {
                        // Got valid JSON with error response, use it
                        throw new Error(message || response.status);
                    });
            }
            // Successful response, parse the JSON and return the data
            return response.json();
        })
        .then((data) => {
            // 'data' now contains the JSON data
            updateExamine(data);
            console.log(data);
        })
        .catch((error) => {
            console.error('Fetch error:', error);
        });
};

