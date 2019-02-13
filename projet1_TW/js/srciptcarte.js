window.addEventListener("load",dessinerCarte);

//aa

/*
Fonction who create carte and applique the event in all li
*/
function dessinerCarte(){

    var map = L.map('carte').setView([50.60702, 3.13909], 16);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    putButtonAMark(L, map);


    map.on("popupopen",activerBouton);
    //applique event in all li
    var listes = document.querySelectorAll("li");
    for (var i = 0; i<listes.length; i++){
        listes[i].addEventListener("click", boutonActive1);
    }
    var div = document.querySelector("#listeEnt");
    div.style.border = "2px solid white";
}




/*
Fonction who applique the event in the button
*/
function activerBouton(ev) {
    var noeudPopup = ev.popup._contentNode; // le noeud DOM qui contient le texte du popup
    var bouton = noeudPopup.querySelector("button"); // le noeud DOM du bouton inclu dans le popup
    bouton.addEventListener("click",boutonActive); // en cas de click, on déclenche la fonction boutonActive
}


/*
Fonction who put the table concern the detail of entreprises when you click the button in map
*/
function boutonActive(ev) {
    // this est ici le noeud DOM de <button>. La valeur associée au bouton est donc this.value
    var body = document.querySelectorAll("body");
    var result = "";
    var lastSection = document.querySelector("#comple");

    if (lastSection)
        body[0].removeChild(lastSection);

    var idi = this.value;
    var thisli = document.getElementById(idi);
    var newSection = document.createElement("table");
    newSection.id = "comple";
    result += "<tbody>";
    result += "<tr><th> nom de l'entreprise: </th><td>"+thisli.dataset.nomen_long+" </td></tr>\n";
    result += "<tr><th> adress: </th><td>"+thisli.dataset.l2_normalisee+"  "+thisli.dataset.l6_normalisee+ "  "+thisli.dataset.libcom+"  </td></tr>\n";
    result += "<tr><th> Activité: </th><td>"+thisli.dataset.activite+"  </td></tr>\n";
    result += "<tr><th> Catégorie: </th><td>"+thisli.dataset.categorie+"  </td></tr>\n";
    result += "<tr><th> Tranche d'effectif: </th><td>"+thisli.dataset.libtefet+"  </td></tr>\n";
    result += "<tr><th> Nature juridique: </th><td>"+thisli.dataset.libnj+"  </td></tr>\n";
    result += "</tbody>";
    newSection.innerHTML = result;
    body[0].appendChild(newSection);

  }

  /*
  Fonction who put the table concern the detail of entreprises when you click the element in liste entreprise
  */
  function boutonActive1(ev) {
      // this est ici le noeud DOM de <button>. La valeur associée au bouton est donc this.value

      var body = document.querySelectorAll("body");
      var result = "";
      var lastSection = document.querySelector("#comple");
      if (lastSection)
          body[0].removeChild(lastSection);
      var idi = this.id;
      var thisli = document.getElementById(idi);

      var newSection = document.createElement("table");
      newSection.id = "comple";
      result += "<tbody>";
      result += "<tr><th> Nom: </th><td>"+thisli.dataset.nomen_long+" </td></tr>\n";
      result += "<tr><th> Adresse: </th><td>"+thisli.dataset.l2_normalisee+"  "+thisli.dataset.l6_normalisee+ "  "+thisli.dataset.libcom+"  </td></tr>\n";
      result += "<tr><th> Activité: </th><td>"+thisli.dataset.activite+"  </td></tr>\n";
      result += "<tr><th> Catégorie: </th><td>"+thisli.dataset.categorie+"  </td></tr>\n";
      result += "<tr><th> Tranche d'effectif: </th><td>"+thisli.dataset.libtefet+"  </td></tr>\n";
      result += "<tr><th> Nature juridique: </th><td>"+thisli.dataset.libnj+"  </td></tr>\n";
      result += "</tbody>";
      newSection.innerHTML = result;
      body[0].appendChild(newSection);

    }

/*
Fonction put all button in map
*/
function putButtonAMark(L, map){
      var liste = document.querySelectorAll("li");
      var pointList = [];
      var lent = liste.length;
      for (var i=0; i<liste.length; i=i+1){
            var nom = liste[i].textContent;
            var siret = liste[i].dataset.siret;
            var texte = nom + "<button value=\""+siret+"\"> choisir </button>";
            var point = [parseFloat(liste[i].dataset.lat), parseFloat(liste[i].dataset.long)];
            L.marker(point).addTo(map).bindPopup(texte);
            pointList.push(point);
      }
      map.fitBounds(pointList);
}
