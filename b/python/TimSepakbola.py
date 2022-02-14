class TimSepakbola():

    #atribut private 

    __NamaTim = "" #atribut untuk nama tim
    __NegaraTim = "" #atribut untuk negara tim
    __TahunBerdiri = "" #atribut untuk tahun berdiri tim
    __jumlahPemain = 0 #atribut untuk jumlah pemain pada tim

    def __init__(self): #Constructor
       
        self.__NamaTim = "" 
        self.__NegaraTim = "" 
        self.__TahunBerdiri = "" 
        self. __jumlahPemain = 0 

    # metode untuk getter dan setter

    def setNamaTim(self, NamaTim):
        self.__NamaTim = NamaTim
    

    def getNamaTim(self):
        return self.__NamaTim
    

    def setNegaraTim(self, NegaraTim):
        self.__NegaraTim = NegaraTim
    

    def getNegaraTim(self):
        return self.__NegaraTim
    

    def setTahunBerdiri_Tim(self, TahunBerdiri):
        self.__TahunBerdiri = TahunBerdiri
    

    def getTahunBerdiri_Tim(self):
        return self.__TahunBerdiri
    

    def setJumlahPemain(self, jumlahPemain):
        self.__jumlahPemain = jumlahPemain
    

    def getJumlahPemain(self):
        return self.__jumlahPemain
    

    class Player(): # inner class Player
        
        # atribut private untuk inner class
        __namaPemain = ""
        __noPunggung = ""

        def __init__(self): #Constructor

            self.__namaPemain = ""
            self.__noPunggung = ""

        # metode getter dan setter inner class
        def setNamaPemain(self, namaPemain):
            self.__namaPemain = namaPemain
        
        def getNamaPemain(self):
            return self.__namaPemain
    
        def setNoPemain(self, noPunggung):
            self.__noPunggung = noPunggung
        
        def getNoPemain(self):
            return self.__noPunggung
        
 

    def innerclass_list(self, jumlahPemain): # prosedur untuk instansiasi objek array inner class
    
        self.pemain = [TimSepakbola.Player() for i in range(jumlahPemain)]
   

    i = 0

    def getInfoTeam(self): # prosedur untuk menampilkan informasi tim sepakbola
        print("Nama Tim           : " + str(self.__NamaTim))
        print("Negara Asal Tim    : " + str(self.__NegaraTim))
        print("Tahun Berdiri Tim  : " + str(self.__TahunBerdiri) + '\n')

        print("--- Daftar Pemain Tim ---")

        for i in range(self.__jumlahPemain):
            print(str(i+1) + ". " + self.pemain[i].getNamaPemain() + " " + self.pemain[i].getNoPemain())
        
        print()
