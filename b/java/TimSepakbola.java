public class TimSepakbola{ // outer class

    //Enkapsulasi private untuk atribut
    private String NamaTim;
    private String NegaraTim = "";
    private String TahunBerdiri = "";
    private int jumlahPemain = 0;

    public TimSepakbola(){ //Constructor

    }

    // metode setter dan getter
    public void setNamaTim(String NamaTim){
        this.NamaTim = NamaTim;
    }

    public String getNamaTim(){
        return NamaTim;
    }

    public void setNegaraTim(String NegaraTim){
        this.NegaraTim = NegaraTim;
    }

    public String getNegaraTim(){
        return NegaraTim;
    }

    public void setTahunBerdiri_Tim(String TahunBerdiri){
        this.TahunBerdiri = TahunBerdiri;
    }

    public String getTahunBerdiri_Tim(){
        return TahunBerdiri;
    }

    
    public void setJumlahPemain(int jumlahPemain){
        this.jumlahPemain = jumlahPemain;
    }

    public int getJumlahPemain(){
        return jumlahPemain;
    }

    class Player{ // inner class

        //Enkapsulasi private untuk atribut inner class
        private String namaPemain = "";
        private String noPunggung = "";

        public Player(){ //Constructor

        }

        // metode getter dan setter
        public void setNamaPemain(String namaPemain){
            this.namaPemain = namaPemain;
        }

        public String getNamaPemain(){
            return namaPemain;
        }

        public void setNoPemain(String noPunggung){
            this.noPunggung = noPunggung;
        }

        public String getNoPemain(){
            return noPunggung;
        }
    }

    Player[] pemain = new Player[12]; // membuat array objek inner class
    int i;

    public void getInfoTeam(){ //prosedur untuk menampilkan informasi tim

        System.out.println("Nama Tim           : " + NamaTim);
        System.out.println("Negara Asal Tim    : " + NegaraTim);
        System.out.println("Tahun Berdiri Tim  : " + TahunBerdiri);
        System.out.println();
        System.out.println("--- Daftar Pemain Tim ---");
        
        if(jumlahPemain < 12){
            
            for(i=0; i<jumlahPemain; i++){
                System.out.println((i+1) + ". " + pemain[i].getNamaPemain() + " " + pemain[i].getNoPemain());
            }
        }
    }
}

