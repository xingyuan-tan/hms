var btnFetchPatient = document.getElementById("fetch-patient");
var selectedPatient = document.getElementById("selected-patient");

var patientDisease = document.getElementById("patient-disease");
var discoveredList = document.getElementById("discovered-list");
var undiscoveredList = document.getElementById("undiscovered-list");
var examineSelectList = document.getElementById("selected-examine");

const URL = window.location.host;

btnFetchPatient.onclick = function () {
    console.log('Fetch Patient');
    console.log(URL)
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
            // updateExamine(data);
            updatePatient(data);
            console.log(data);
        })
        .catch((error) => {
            console.error('Fetch error:', error);
        });
};

function updatePatient(data) {
    patient = data.data.patient;
    console.log(data.data)
    data = data.data;

    // Initiate Value
    patientDisease.textContent = '';
    discoveredList.textContent = '';
    undiscoveredList.textContent = '';
    examineSelectList.textContent = '';

    console.log('Update Patient Disease');
    if (patient['disease']) {
        console.log(patient['disease']);
        patientDisease.textContent = patient['disease'];
    }
    
    console.log("Update Discovered and Undiscovered Lists")
    Object.keys(patient['symptoms']).forEach(function(key){

        if (patient['symptoms'][key]) {
            console.log(patient['symptoms'][key]);

            const newItem = document.createElement('li');
            newItem.className = 'list-group-item';
            newItem.textContent = key;
            discoveredList.appendChild(newItem);
        } else {
            const newItem = document.createElement('li');
            newItem.className = 'list-group-item';
            newItem.textContent = key;
            undiscoveredList.appendChild(newItem);
        }
    });

    console.log("Update Possible Examinations List")
    Object.keys(patient['possible_exam']).forEach(function(key){
        const newItem = document.createElement('option');
        newItem.textContent = patient['possible_exam'][key];
        examineSelectList.appendChild(newItem);
    });
    
    console.log("Update Completed Examination List")
    Object.keys(patient['examined']).forEach(function(key){
        const newItem = document.createElement('li');
        newItem.className = 'list-group-item';
        newItem.textContent = key;
        completedExamList.appendChild(newItem);
    });
}