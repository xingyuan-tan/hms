var btnDoctor = document.getElementById("home-doctor");
var btnNetural = document.getElementById("home-neutral");
var host = window.location.host;

btnDoctor.onclick = function () {
    window.location.href = 'doctor';
};

btnNetural.onclick = function () {
    window.location.href = 'neutral';
};
