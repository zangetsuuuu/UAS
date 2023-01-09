from model.daftar_nilai import *
from view.view_nilai import *

print("\nProgram Data Mahasiswa")
print("======================\n")

while True:
    menu = input("[ (1) Lihat Data,  (2) Tambah Data,  (3) Ubah Data,  (4) Cari Data,  (5) Hapus Data,  (6) Keluar ]\nPilih menu: ")
    print()

    if menu == "1":
        cetak_daftar_nilai()
    elif menu == "2":
        tambah_data()
    elif menu == "3":
        ubah_data()
    elif menu == "4":
        cari_data()
    elif menu == "5":
        hapus_data()
    elif menu == "6":
        print("> Anda telah keluar dari program")
        break
    else:
        print("Kode tidak valid!\n")