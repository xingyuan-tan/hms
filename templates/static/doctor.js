var btnFetchPatient = document.getElementById("fetch-patient");
var selectedPatient = document.getElementById("selected-patient");


btnFetchPatient.onclick = function () {
    fetch(url + '/patient-data/' + selectedPatient.getAttributeNode().value)
        .then(response => {
            d1 = response
            myChart.config.data.datasets[0].data = d1[1];
            myChart.config.data.labels = d1[0];
            myChart.update();
        })
};