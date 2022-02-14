<?php
include "Mahasiswa.php"; //include file class 

$Student1 = new Mahasiswa(); //membuat objek untuk student 1

//instansiasi menggunakan setter dari objek
$Student1->setNIM("2000312");
$Student1->setNama("Dian Satro");
$Student1->setKelamin("P");
$Student1->setProdi("Biologi");
$Student1->setSemester("6");

//instansiasi objek student 2 dan 3 dengan menggunakan contructor dari objek
$Student2 = new Mahasiswa("2000318", "Silmi Aulia Rohmah", "P", "Ilmu Komputer", "4");
$Student3 = new Mahasiswa("2000318", "Silmi Aulia ", "P", "Ilmu Komputer", "4");

//menampilkan informasi mengenai daftar mahasiswa 
$Student1->info_DaftarMahasiswa();
$Student2->info_DaftarMahasiswa();
$Student3->info_DaftarMahasiswa();

?>