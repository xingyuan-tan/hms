var btnFetchPatient = document.getElementById("fetch-patient");
var selectedPatient = document.getElementById("selected-patient");
var symptomList = document.getElementById("symptom-list")
var completedExamList = document.getElementById("completed-exam-list")
const URL = window.location.host;

btnFetchPatient.onclick = function () {
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
            updateSymptoms(data);
            updateExamination(data);
            console.log(data);
        })
        .catch((error) => {
            console.error('Fetch error:', error);
        });
};

function updateSymptoms(patient) {
    console.log('Update Symptoms');
    symptomList.textContent = '';

    Object.keys(patient['symptoms']).forEach(function(key){
        console.log(key, patient['symptoms'][key]);

        if (patient['symptoms'][key]) {
            const newItem = document.createElement('li');
            newItem.className = 'list-group-item';
            newItem.textContent = key;
            symptomList.appendChild(newItem);
        }
    });
}

function updateExamination(patient){
    console.log('Update Symptoms');
    completedExamList.textContent = '';

    Object.keys(patient['examined']).forEach(function(key){
        console.log(key, patient['examined'][key]);
        const newItem = document.createElement('li');
        newItem.className = 'list-group-item';
        newItem.textContent = key;
        completedExamList.appendChild(newItem);
    });
}

function updateCompletedExamine(patient) {
    console.log('Update Completed Examine');


}
