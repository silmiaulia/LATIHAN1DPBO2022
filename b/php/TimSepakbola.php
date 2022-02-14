<?php

class TimSepakbola{

    private $NamaTim = ""; //atribut untuk nama tim
    private $NegaraTim = ""; //atribut untuk negara tim
    private $TahunBerdiri = ""; //atribut untuk tahun berdiri tim
    private $jumlahPemain = 0; ////atribut untuk jumlah pemain pada tim
    private $noPemain = 0;
    private $namaPemain = array();
    private $noPunggung = array();
    private $noUrutanTim = 0;


    public function __construct($noUrutanTim = 0, $jumlahPemain = 0){
        
        $this->noUrutanTim = $noUrutanTim;
        $this->jumlahPemain = $jumlahPemain;

    }

    public function setNamaTim($NamaTim){
        $this->NamaTim = $NamaTim;
    }

    public function setNegaraTim($NegaraTim){
        $this->NegaraTim = $NegaraTim;
    }

    public function setTahunBerdiri_Tim($TahunBerdiri){
        $this->TahunBerdiri = $TahunBerdiri;
    }

    public function Pemain($noPemain, $namaPemain, $noPunggung){
    
        $this->namaPemain[$noPemain] = $namaPemain;
        $this->noPunggung[$noPemain] = $noPunggung;
        
    }

    public function getInfoTeam(){

        echo "====================". "<br>";
        echo " Informasi Tim ". $this->noUrutanTim. "<br>";
        echo "====================". "<br>";

        echo "Nama Tim           : ". $this->NamaTim. "<br>";
        echo "Negara Asal Tim    : ". $this->NegaraTim. "<br>";
        echo "Tahun Berdiri Tim  : ". $this->TahunBerdiri. "<br>";

        echo "<br/>";
        echo "--- Daftar Pemain Tim --- "."<br>";

        for($i=0; $i<$this->jumlahPemain; $i++){
            echo ($i+1). ". ". $this->namaPemain[$i]. " - ". $this->noPunggung[$i]. "<br>";
        }

        echo "<br/>";
    }
}

?>