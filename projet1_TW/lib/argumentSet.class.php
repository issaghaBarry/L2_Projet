<?php

/**
Fonction permettant de recupperer les valeur entrer dans le formulaire et de verifier leur validite
autheur : barry-Fremaux
*/


class ArgumentSet{
      private $value = array();

      private $imputType;




      public function __construct($inputType=INPUT_GET){

    		$this->inputType = $inputType;


        $name = "nom";
    		$v = filter_input($this->inputType, $name, FILTER_SANITIZE_STRING);
    		$this->value[$name] = trim($v);


        $name = "localite";
    		$v = filter_input($this->inputType, $name, FILTER_SANITIZE_STRING);
    		$this->value[$name] = trim($v);


        $name = "activite";
      	$v = filter_input($this->inputType, $name, FILTER_SANITIZE_STRING);
      	$this->value[$name] = trim($v);

        $name = "categorie";
        $v = filter_input($this->inputType, $name, FILTER_SANITIZE_STRING);
      	$this->value[$name] = trim($v);




      }

      public function getNom(){
          if (isset($this->value["nom"]) && $this->value["nom"]!=="")
              return $this->value["nom"];
          else
              return NULL;
      }

      public function getLocalite(){
          if (isset($this->value["localite"])&& $this->value["localite"]!=="")
              return $this->value["localite"];
          else
              return NULL;
      }

      public function getActivite(){
          if (isset($this->value["activite"]) && $this->value["activite"]!=="")
              return $this->value["activite"];
          else
              return NULL;
      }

      public function getCategorie(){
          if (isset($this->value["categorie"]))
              return $this->value["categorie"];
          else
              return NULL;
      }



}







 ?>
