import java.util.*;

public class Main{

    public static void main(String[] args){
        
        int n =0, i = 0;

        System.out.print("Masukan Jumlah Tim : ");
        
        Scanner sc = new Scanner(System.in);

        try{

            n = Integer.parseInt(sc.nextLine());

        }catch(Exception e){}


        TimSepakbola[] football = new TimSepakbola[n];

        for(i=0; i<n; i++){

            String NamaTim = "";
            String NegaraTim = "";
            String TahunBerdiri = "";
            int Pemain = 0;

            //lakukan input nama, asal negara, dan tahun berdiri tim
            System.out.print("Masukan Nama Tim ke " + (i+1) + " : ");
            try{

                NamaTim = sc.nextLine();

            }catch(Exception e){}

            System.out.print("Masukan Asal Negara Tim " + (i+1) + " : ");
            try{

                NegaraTim = sc.nextLine();

            }catch(Exception e){}

            System.out.print("Masukan Tahun Berdiri Tim " + (i+1) + " : ");
            try{

                TahunBerdiri = sc.nextLine();

            }catch(Exception e){}
           
            football[i] = new TimSepakbola(); //instantiation

            //gunakan prosedur setter dari objek 
            football[i].setNamaTim(NamaTim);
            football[i].setNegaraTim(NegaraTim);
            football[i].setTahunBerdiri_Tim(TahunBerdiri);

            

            //input jumlah pemain pada setiap tim
            System.out.print("Masukan jumlah pemain dalam tim  " + (i+1) + " : ");
            try{

                Pemain = Integer.parseInt(sc.nextLine());

            }catch(Exception e){}

            football[i].setJumlahPemain(Pemain); //instansiasi jumlah pemain menggunakan setter objek

            int j = 0;

            if(Pemain < 12){

                System.out.println("Masukan nama dan nomor punggung pemain");

                for(j=0; j<Pemain; j++){

                    //deklarasi dan inisialisasi atribut untuk inner class
                    String namaPemain = "";
                    String NoPemain = "";

                    try{

                        namaPemain = sc.nextLine(); //meminta inputan nama pemain

                    }catch(Exception e){}

                    try{

                        NoPemain = sc.nextLine(); //meminta inputan nomor punggung pemain

                    }catch(Exception e){}

                    //instantiation 
                    football[i].pemain[j] = football[i].new Player(); 

                    //memanggil prosedur setter
                    football[i].pemain[j].setNamaPemain(namaPemain);
                    football[i].pemain[j].setNoPemain(NoPemain);   
                    
                }
            }

        }

        //menampilkan infromasi untuk setiap tim sepakbola sebanyak n
        for(i=0; i<n; i++){

            System.out.println("============================");
            System.out.println(" INFORMASI TIM SEPAKBOLA " + (i+1));
            System.out.println("============================");

            football[i].getInfoTeam(); //memanggil metode untuk menampilkan informasi tim dan pemainnya

            System.out.println(); //menambahkan new line
        }
    }
}