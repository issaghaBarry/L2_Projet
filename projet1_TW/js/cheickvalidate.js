/*
Fonction cheick when the formular must validate
*/
function validateform(){
    var nom = document.getElementById("nom");
    var localite = document.getElementById("localite");
    var activite = document.getElementById("activite");
    if (localite.value.trim() && activite.value.trim()){
        return true;
    }
    if (nom.value.trim()){
        return true;
    }
    return false;
}
