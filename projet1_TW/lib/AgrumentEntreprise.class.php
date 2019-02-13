<?php


class ArgumentEntreprise{

    private $siret;
    private $nomen_long;
    private $l2_normalisee;
    private $l6_normalisee;
    private $libcom;
    private $libtefet;
    private $libapet;
    private $libnj;
    private $categorie;
    private $activite;
    private $coordonnees;
    private $fields;


    public function __construct($fields){
          $this->fields = $fields;

          $this->siret = $this->fields->siret;
          $this->nomen_long = $this->fields->nomen_long;
          $this->l2_normalisee = $this->fields->l2_normalisee;
          $this->l6_normalisee = $this->fields->l6_normalisee;
          $this->libcom = $this->fields->libcom;
          $this->libtefet = $this->fields->libtefet;
          $this->libapet = $this->fields->libapet;
          $this->libnj = $this->fields->libnj;
          $this->categorie = $this->fields->categorie;
          $this->activite = $this->fields->activite;
          $this->coordonnees = $this->fields->coordonnees;


    }

    public function getSiret(){
        return $this->siret;
    }

    public function getnomen_long(){
        return $this->nomen_long;
    }

    public function getL2_norm(){
        return $this->l2_normalisee;
    }

    public function getL6_norm(){
        return $this->l6_normalisee;
    }

    public function getLibcom(){
        return $this->libcom;
    }

    public function getLibapet(){
        return $this->libapet;
    }

    public function getLibtefet(){
        return $this->libtefet;
    }

    public function getLibnj(){
        return $this->libnj;
    }

    public function getCategorie(){
        return $this->categorie;
    }

    public function getActivite(){
        return $this->activite;
    }

    public function getCoordonnees(){
        return $this->coordonnees;
    }


    private function toHtmlWindow(){
        $result = "<section>\n";
        $result.= "<p>Nom de l'entreprise: ".$this->getnomen_long()."</p>\n";
        $result.= "<p>"


        $result .="</section>\n"
    }



}






 ?>
