#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

#include "TimSepakbola.cpp"

int main(){

    int n =0, i = 0; //variabel untuk jumlah tim dan untuk iterasi

    //meminta inputan banyaknya daftar tim sepakbola
    cout << "Masukan Jumlah Tim : ";
    cin>>n;

    TimSepakbola football[n]; //membuat array objek sebanyak n

    for(i=0; i<n; i++){ //looping untuk menginput informasi tim dan untuk instansiasi objek array

        //deklarasi atribut daftar tim sepakbola
        string NamaTim;
        string NegaraTim;
        string TahunBerdiri;
        int Pemain;

        //lakukan input nama, asal negara, dan tahun berdiri tim
        cout << "Masukan Nama Tim ke " << i+1 << " : ";
        cin >> NamaTim; 
        cout << "Masukan Asal Negara Tim " << i+1 << " : ";
        cin >> NegaraTim; 
        cout << "Masukan Tahun Berdiri Tim " << i+1 << " : ";
        cin >> TahunBerdiri; 

        //gunakan setter dari objek untuk instansiasi
        football[i].setNamaTim(NamaTim);
        football[i].setNegaraTim(NegaraTim);
        football[i].setTahunBerdiri_Tim(TahunBerdiri);

        //input jumlah pemain pada setiap tim
        cout << "Masukan jumlah pemain dalam tim " << i+1 << " : ";
        cin >> Pemain;

        football[i].setJumlahPemain(Pemain); //instansiasi jumlah pemain menggunakan setter objek

        int j = 0; //untuk iterasi

        if(Pemain < 12){ //jika jumlah pemain kurang dari 12

            //melakukan input setiap informasi pemain pada setiap tim
            cout << "Masukan nama dan nomor punggung pemain" << endl;
            for(j=0; j<Pemain; j++){

                //deklarasi atribut daftar pemain pada tim sepakbola
                string namaPemain;
                string NoPemain;

                cin >> namaPemain >> NoPemain; //input nama pemain dan no punggung pemain

                //instansiasi array ojek inner class 
                football[i].pemain[j].setNamaPemain(namaPemain);
                football[i].pemain[j].setNoPemain(NoPemain);
                
            
            }
        }

    }

    //menampilkan infromasi untuk setiap tim sepakbola sebanyak n
    for(i=0; i<n; i++){

        cout << "============================" << endl;
        cout << " INFORMASI TIM SEPAKBOLA " << i+1 << endl;
        cout << "============================" << endl;

        football[i].getInfoTeam(); //memanggil metode untuk menampilkan informasi tim dan pemainnya

        cout << "\n"; //menambahkan new line
    }


    return 0;

}