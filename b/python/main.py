from TimSepakbola import TimSepakbola #melakukan import class

n = 0 # untuk menyimpan jumlah tim
i = 0 # untuk iteras

n = int(input("Masukan Jumlah Tim : ")) # meminta inputan banyaknya jumlah tim


football = [TimSepakbola() for i in range(n)] # membuat array objek 

for i in range(n):

    # melakukan input data tim sepakbola
    print("Masukan Nama Tim ke " + str(i+1) + " : ", end ="")
    NamaTim = str(input())

    print("Masukan Asal Negara Tim " + str(i+1) + " : ", end ="")
    NegaraTim = str(input())

    print("Masukan Tahun Berdiri Tim " + str(i+1) + " : ", end ="")
    TahunBerdiri = str(input())

    # memanggil prosedur setter
    football[i].setNamaTim(NamaTim)
    football[i].setNegaraTim(NegaraTim)
    football[i].setTahunBerdiri_Tim(TahunBerdiri)

    # meminta input jumlah pemain dalam tim
    print("Masukan jumlah pemain dalam tim " + str(i+1) + " : ", end ="")
    Pemain = int(input())

    football[i].setJumlahPemain(Pemain) # untuk menampung jumlah pemain dengan menggunakan prosedur setter

    j = 0

    football[i].innerclass_list(Pemain) # memanggil prosedur untuk membuat array objek inner class

    if(Pemain < 12):

        # melakukan input setiap informasi pemain pada setiap tim
        print("Masukan nama dan nomor punggung pemain")
        for j in range(Pemain):

            namaPemain, NoPemain =  map(str, input().split()) # input nama pemain dan nomor punggung
            # memanggil prosedur setter
            football[i].pemain[j].setNamaPemain(namaPemain)
            football[i].pemain[j].setNoPemain(NoPemain)




for i in range(n):
    # menampilkan informasi setiap tim sepakbola sebanyak n
    print("============================")
    print(" INFORMASI TIM SEPAKBOLA " + str(i+1))
    print("============================")

    football[i].getInfoTeam()

    

