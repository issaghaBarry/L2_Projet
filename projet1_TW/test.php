<<<<<<< HEAD
<?php
require_once('lib/AgrumentEntreprise.class.php');

$chaine = file_get_contents('test.json');
$data = json_decode($chaine);
//$data1 = $data->records[0]->fields;
//$arg=new ArgumentEntreprise($data1);
//var_dump($arg->getSiret());
var_dump($data->lieu)
?>
=======
<?php
require_once('lib/AgrumentEntreprise.class.php');

$chaine = file_get_contents('test.json');
$data = json_decode($chaine);
//$data1 = $data->records[0]->fields;
//$arg=new ArgumentEntreprise($data1);
//var_dump($arg->getSiret());
var_dump($data->lieu)
?>
>>>>>>> 60aa6f809ca21129a6ec218a3b06ade165d7a34b
