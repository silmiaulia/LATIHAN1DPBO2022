<?php
include "TimSepakbola.php";

$team1 = new TimSepakbola(1, 2);
$team1->setNamaTim("Real Madrid");
$team1->setNegaraTim("Spanyol");
$team1->setTahunBerdiri_Tim("1902");
$team1->Pemain(0, "David Alaba", "4");
$team1->Pemain(1, "Thibaut Courtois", "1");

$team2 = new TimSepakbola(2, 4);
$team2->setNamaTim("Paris Saint-Germain");
$team2->setNegaraTim("Prancis");
$team2->setTahunBerdiri_Tim("1970");
$team2->Pemain(0, "Neymar", "10");
$team2->Pemain(1, "L. Messi", "30");
$team2->Pemain(2, "K. Mbappé", "7");
$team2->Pemain(3, "A. Hakimi", "2");

$team3 = new TimSepakbola(3, 1);
$team3->setNamaTim("Manchester United");
$team3->setNegaraTim("Inggris");
$team3->setTahunBerdiri_Tim("1878");
$team3->Pemain(0, "Cristiano Ronaldo", "7");


$team1->getInfoTeam();
$team2->getInfoTeam();
$team3->getInfoTeam();
