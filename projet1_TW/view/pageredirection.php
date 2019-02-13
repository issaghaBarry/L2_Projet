
<?php
require_once('../lib/argumentSet.class.php');
$argSet = new argumentSet(INPUT_GET);
if ($argSet->getNom()!==NULL || $argSet->getLocalite()!==NULL || $argSet->getActivite()!==NULL){
      $tes = '<script type="text/javascript" src="../js/srciptcarte.js"></script>';
      echo $tes;
      if($argSet->getNom()!==NULL){
              $result = "q=nomen_long:".$argSet->getNom()."&refine.categorie=".$argSet->getCategorie();
              if ($argSet->getLocalite()!==NULL && $argSet->getActivite()!==NULL){
                $result.="q=(libcom:".$argSet->getLocalite().")+and+(activite:".$argSet->getActivite().")";}
              }
      elseif($argSet->getLocalite()!==NULL && $argSet->getActivite()!==NULL){
                $result = "q=(libcom:".$argSet->getLocalite().")+and+(activite:".$argSet->getActivite().")&refine.categorie=".$argSet->getCategorie();}


      $a = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=base-sirene&rows=20&".$result;
      require_once('ListeEntreprise.php');
}

?>
