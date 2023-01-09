from view.input_nilai import *

data_mahasiswa = {}

def tambah_data():
    print("Tambah Data")
    global data_mahasiswa
    while True:
        nama = input_nama()
        nim = input_nim()
        tugas = input_tugas()
        uts = input_uts()
        uas = input_uas()
        akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
        data_mahasiswa[nama] = nim, tugas, uts, uas, akhir

        ulangi = input('\nTambah data lagi? (Y/T): ')
        if ulangi.lower() == 'y':
            continue
        elif ulangi.lower() == 't':
            print('Data berhasil ditambahkan!\n')
            break
        else:
            break

def ubah_data():
    print("Ubah Data")
    nama = input_nama()
    if nama in data_mahasiswa.keys():
        print("\nMengubah data")
        nim = input_nim()
        tugas = input_tugas()
        uts = input_uts()
        uas = input_uas()
        total = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
        data_mahasiswa[nama] = nim, tugas, uts, uas, total
        print("Data berhasil diubah!\n")
    else:
        print("Data '{}' tidak ditemukan!\n".format(nama))


def hapus_data():
    print("Hapus Data")
    nama = input_nama()
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
        print("Data '{}' berhasil dihapus!\n".format(nama))
    else:
        print("Data '{}' tidak ditemukan!\n".format(nama))


def cari_data():
    print("Cari Data")
    nama = input_nama()
    if nama in data_mahasiswa.keys():
        print("================================================================================================")
        print("|           Nama           |       NIM       |   Tugas   |   UTS   |   UAS   |   Nilai Akhir   |")
        print("================================================================================================")
        print("| {0:24s} | {1:15s} | {2:9d} | {3:7d} | {4:7d} | {5:15f} |"
              .format(nama, data_mahasiswa[nama][0], data_mahasiswa[nama][1], data_mahasiswa[nama][2], data_mahasiswa[nama][3], data_mahasiswa[nama][4]))
        print("================================================================================================\n")
    else:
        print("Data '{}' tidak ditemukan!\n".format(nama))