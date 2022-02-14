from TimSepakbola import TimSepakbola

n = 0
i = 0


n = int(input("Masukan Jumlah Tim : "))


football = [TimSepakbola() for i in range(n)]

for i in range(n):

    print("Masukan Nama Tim ke " + str(i+1) + " : ", end ="")
    NamaTim = str(input())

    print("Masukan Asal Negara Tim " + str(i+1) + " : ", end ="")
    NegaraTim = str(input())

    print("Masukan Tahun Berdiri Tim " + str(i+1) + " : ", end ="")
    TahunBerdiri = str(input())

    football[i].setNamaTim(NamaTim)
    football[i].setNegaraTim(NegaraTim)
    football[i].setTahunBerdiri_Tim(TahunBerdiri)

    print("Masukan jumlah pemain dalam tim " + str(i+1) + " : ", end ="")
    Pemain = int(input())

    football[i].setJumlahPemain(Pemain)

    j = 0

    football[i].innerclass_list(Pemain)

    if(Pemain < 12):

        print("Masukan nama dan nomor punggung pemain")
        for j in range(Pemain):

            namaPemain, NoPemain =  map(str, input().split())
  
            football[i].pemain[j].setNamaPemain(namaPemain)
            football[i].pemain[j].setNoPemain(NoPemain)




for i in range(n):

    print("============================")
    print(" INFORMASI TIM SEPAKBOLA " + str(i+1))
    print("============================")

    football[i].getInfoTeam()

    

