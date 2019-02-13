<?php

class argumentAllEnt{

    private $records;

    private $nhits;


    public function __construct($objet){
        $this->records = $objet->records;
        $this->nhits = $objet->nhits;


    }

    public function toHtml(){
		$result .= "<article>";
		$result .="<h2 id=\"Titrediv\">".sizeof($this->records)." résultats trouvés : </h2>";
        $result .= "<div id=\"listeEnt\"><ul data-nhits=\"".$this->nhits."\">\n";
        for ($i=0 ; $i<sizeof($this->records); $i++){
            $nomen_long = $this->records[$i]->fields->nomen_long;
            $result .= $this->htmlli($i);
            $result .= " ".$this->records[$i]->fields->nomen_long." ";
            $result .= "</li>\n";
        }
        $result .= "</ul></div>\n";
        $result .= "</article>";
        return $result;

    }

    private function htmlli($i){
        $nomen_long = $this->records[$i]->fields->nomen_long;
        $siret= $this->records[$i]->fields->siret;
        $l2_normalisee= $this->records[$i]->fields->l2_normalisee;
        $l6_normalisee= $this->records[$i]->fields->l6_normalisee;
        $libcom= $this->records[$i]->fields->libcom;
        $libtefet=$this->records[$i]->fields->libtefet;
        $libapet=$this->records[$i]->fields->libapet;
        $libnj=$this->records[$i]->fields->libnj;
        $categorie= $this->records[$i]->fields->categorie;
        $activite=$this->records[$i]->fields->activite;
        $coordonnees=$this->records[$i]->fields->coordonnees;
        $result = "<li id=\"".$siret."\" data-siret=\"".$siret."\"";
        $result .= " data-nomen_long=\"".$nomen_long."\" ";
        $result .= " data-l2_normalisee=\"".$l2_normalisee."\" ";
        $result .= " data-l6_normalisee=\"".$l6_normalisee."\" ";
        $result .= " data-libcom=\"".$libcom."\" ";
        $result .= " data-libtefet=\"".$libtefet."\" ";
        $result .= " data-libapet=\"".$libapet."\" ";
        $result .= " data-libnj=\"".$libnj."\" ";
        $result .= " data-categorie=\"".$categorie."\" ";
        $result .= " data-activite=\"".$activite."\" ";
        $result .= " data-libcom=\"".$libcom."\" ";
        $result .= " data-long=\"".$coordonnees[1]."\" ";
        $result .= " data-lat=\"".$coordonnees[0]."\" ";
        $result .= ">\n";
        return $result;
    }

}



 ?>
