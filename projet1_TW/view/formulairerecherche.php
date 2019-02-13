<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Formulaire de Recherche</title>

 <script type="text/javascript" src="../js/cheickvalidate.js"></script>
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" />
 <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>
 <link rel="stylesheet" href="../css/leaftcss.css" />
 <link rel="stylesheet" href="../css/styleformulaire.css" />

</head>
<body>

    <header><h1>Recherche d'entreprise de la MEL :</h1>
    <img src="../image/image.png" alt="Logo MEL" id="logo"/>

    </header>
    <img src="../image/lille.png" alt="Logo MEL" id="logolille"/>
    <form action="formulairerecherche.php" method = "get" onsubmit="return validateform()">
      <fieldset>
          <label for="nom"> Nom de l'entreprise : </label><input type="text" id="nom" name="nom" size="25" maxlength="100" /><br/>
          <label for="localite">Localité : </label><input type="text" id="localite" name="localite"  size="25" maxlength="100" /><br />
          <label for="activite">Activité: </label><input type="text" id="activite" name="activite"  size="25" maxlength="256" /><br />

          <p>Catégorie :</p>
          <select name="categorie">
            <option value="">ALL</option>
            <option value="PME">PME</option>
            <option value="ETI">ETI</option>
            <option value="GE">GE</option>
          </select><br/>
            <button type="reset">Effacer</button>
            <button type="submit" name="valid" value="envoyer">Envoyer</button>
      </fieldset>
  </form>


  <?php
  require_once("pageredirection.php");
   ?>
  <div id="carte"> </div>

  <footer>
      <a href="http://webtp.fil.univ-lille1.fr/~barry/projet/view/mentionlegal.html">MENTIONS LEGALES</a>
  </footer>

</body>
</html>
