var btnDoctor = document.getElementById("home-doctor");
var btnNeutral = document.getElementById("home-neutral");
var host = window.location.host;

btnDoctor.onclick = function () {
    window.location.href = 'doctor';
};

btnNeutral.onclick = function () {
    window.location.href = 'neutral';
}