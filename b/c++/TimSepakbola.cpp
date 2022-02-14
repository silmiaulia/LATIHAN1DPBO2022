#include <iostream>
#include <string>

using namespace std;

class TimSepakbola{ //Outer class 

    //Enkapsulasi private untuk atribut
    private:

        string NamaTim; //atribut untuk nama tim
        string NegaraTim; //atribut untuk negara tim
        string TahunBerdiri; //atribut untuk tahun berdiri tim
        int jumlahPemain; ////atribut untuk jumlah pemain pada tim
        
    //Enkapsulasi public 
    public:

        TimSepakbola(){ //Constructor
            
        }

        //Prosedur dan fungsi getter dan setter
        void setNamaTim(string NamaTim){
            this->NamaTim = NamaTim;
        }

        string getNamaTim(){
            return this->NamaTim;
        }

        void setNegaraTim(string NegaraTim){
            this->NegaraTim = NegaraTim;
        }

        string getNegaraTim(){
            return this->NegaraTim;
        }

        void setTahunBerdiri_Tim(string TahunBerdiri){
            this->TahunBerdiri = TahunBerdiri;
        }

        string getTahunBerdiri_Tim(){
            return this->TahunBerdiri;
        }

        
        void setJumlahPemain(int jumlahPemain){
            this->jumlahPemain = jumlahPemain;
        }

        int getJumlahPemain(){
            return this->jumlahPemain;
        }

        class Player{ //Inner class untuk pemain dalam tim

            //Enkapsulasi private untuk atribut
            private:

                string namaPemain;
                string noPunggung;
            
            //Enkapsulasi public
            public:

                Player(){ //Constructor inner class

                }

                //prosedur dan fungsi setter & getter
                void setNamaPemain(string namaPemain){
                    this->namaPemain = namaPemain;
                }

                string getNamaPemain(){
                    return this->namaPemain;
                }

                void setNoPemain(string noPunggung){
                    this->noPunggung = noPunggung;
                }

                string getNoPemain(){
                    return this->noPunggung;
                }

                ~Player(){ //Destructor inner class
                    
                }
        };

        Player pemain[12]; //membuat array inner class sebanyak 12

        int i; //untuk iterasi
        
        void getInfoTeam(){ //prosedur untuk menampilkan informasi setiap tim sepakbola

            cout << "Nama Tim           : " << this->NamaTim << endl;
            cout << "Negara Asal Tim    : " << this->NegaraTim << endl;
            cout << "Tahun Berdiri Tim  : " << this->TahunBerdiri << endl;
            cout << "\n";
            cout << "--- Daftar Pemain Tim ---" << endl;

            if(this->jumlahPemain < 12){

                //jika jumlah pemain kurang dari 12 maka tampilkan setiap pemain

                for(i=0; i<this->jumlahPemain; i++){
                    cout << i+1 << ". " << pemain[i].getNamaPemain() << " " << pemain[i].getNoPemain() << endl; 
                }
            }
        }

        ~TimSepakbola(){ //Destructor outer class

        }

};