<?php
class Mahasiswa{

    //Enkapsulasi private untuk atribut
    private $NIM = "";
    private $Nama = "";
    private $Kelamin = "";
    private $Prodi = "";
    private $Semester = "";

    public function __construct($NIM = "", $Nama ="", $Kelamin = "", $Prodi = "", $Semester = ""){ //Constructor
        
        $this->NIM = $NIM;
        $this->Nama = $Nama;
        $this->Kelamin = $Kelamin;
        $this->Prodi = $Prodi;
        $this->Semester = $Semester;
    }

    //prosedur setter 
    public function setNIM($NIM){
        $this->NIM = $NIM;
    }
    public function setNama($Nama){
        $this->Nama = $Nama;
    }
    public function setKelamin($Kelamin){
        $this->Kelamin = $Kelamin;
    }
    public function setProdi($Prodi){
        $this->Prodi = $Prodi;
    }
    public function setSemester($Semester){
        $this->Semester = $Semester;
    }

    //fungsi getter
    public function getNIM(){
        return $this->NIM;
    }
    public function getNama(){
        return $this->Nama;
    }
    public function getKelamin(){
        return $this->Kelamin;
    }
    public function getProdi(){
        return $this->Prodi;
    }
    public function getSemester(){
        return $this->Semester;
    }

    //fungsi untuk menampilkan informasi mahasiswa
    function info_DaftarMahasiswa(){

        echo "NIM      : ".$this->NIM."<br/>";
        echo "Nama     : ".$this->Nama."<br/>";
        echo "Kelamin  : ".$this->Kelamin."<br/>";
        echo "Prodi    : ".$this->Prodi."<br/>";
        echo "Semester : ".$this->Semester."<br/>";
        echo "<br/>";
    }

    function __destruct(){ //Destructor
    }
}
?>