var btnFetchPatient = document.getElementById("fetch-patient");
var selectedPatient = document.getElementById("selected-patient");
var symptomList = document.getElementById("symptom-list")
var completedExamList = document.getElementById("completed-exam-list")
var possibleExamList = document.getElementById("possible-exam-list")
var diagnosisList = document.getElementById("diagnosis-list")
var diagnosesFound = document.getElementById("diagnoses-found")



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
            updatePatient(data);
            console.log(data);
        })
        .catch((error) => {
            console.error('Fetch error:', error);
        });
};


function updatePatient(data) {
    console.log("Updating Patient Data")
    patient = data.data.patient;
    // console.log(data.data)
    data = data.data;

    symptomList.textContent = '';
    completedExamList.textContent = '';
    possibleExamList.textContent = '';
    diagnosisList.textContent = '';
    diagnosesFound.textContent = 'No';

    console.log('Update Symptoms');
    Object.keys(patient['symptoms']).forEach(function(key){
        // console.log(key, patient['symptoms'][key]);

        if (patient['symptoms'][key]) {
            console.log(patient['symptoms'][key]);

            const newItem = document.createElement('li');
            newItem.className = 'list-group-item';
            newItem.textContent = key;
            symptomList.appendChild(newItem);
        }
    });

    console.log('Update Completed Examination');
    Object.keys(patient['examined']).forEach(function(key){
        const newItem = document.createElement('li');
        newItem.className = 'list-group-item';
        newItem.textContent = key;
        completedExamList.appendChild(newItem);
    });

    console.log('Update possible examination')
    patient['possible_exam'].forEach(function(item){
        const newItem = document.createElement('li');
        newItem.className = 'list-group-item';
        newItem.textContent = item;
        possibleExamList.appendChild(newItem);
    });

    console.log('Update Diagnosis')
    if (data['diagnoses'] == null) {
        const newItem = document.createElement('li');
        newItem.className = 'list-group-item list-group-item-danger';
        newItem.textContent = "You have not completed any examination yet";
        diagnosisList.appendChild(newItem);
    }
    else {
        Object.keys(data['diagnoses']).forEach(function(key){

            if (data['diagnoses'][key]) {
                const newItem = document.createElement('li');
                newItem.className = 'list-group-item';
                newItem.textContent = data['diagnoses'][key];
                diagnosisList.appendChild(newItem);
            }
    
        });
        diagnosesFound.textContent = Object.keys(data['diagnoses']).length;
    }

    console.log("Update Patient Data Completed")
}