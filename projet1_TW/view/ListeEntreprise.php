
  <?php
  require_once('../lib/ArgumentAllEnt.class.php');
  $data = file_get_contents($a);
  $datadeco = json_decode($data);
  $arg = new ArgumentAllEnt($datadeco);
  echo $arg->toHtml();
   ?>
