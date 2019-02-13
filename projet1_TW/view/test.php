<?php
$resultat = "";

$resultat.='<form action="pageredirection.php" method = "get" onsubmit="return validateform()">
  <fieldset>
    <label for="nom"> Nom de l'entreprise: </label><input type="text" id="nom" name="nom" size="25" maxlength="100" /><br/>
      <label for="localite">Localite : </label><input type="text" id="localite" name="localite"  size="25" maxlength="100" /><br />
      <label for="activite">activite : </label><input type="text" id="activite" name="activite"  size="60" maxlength="256" /><br />

      <p>filtre par rapport à une categorie d'entreprise </p>
      <select name="categorie">
        <option value="">ALL</option>
        <option value="PME">PME</option>
        <option value="ETI">ETI</option>
        <option value="GE">GE</option>
      </select><br/>
        <button type="reset">Effacer</button>
        <button type="submit" name="valid" value="envoyer">Envoyer</button>
  </fieldset>
</form>';
?>
