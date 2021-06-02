# ********************************************
# Program Kalkulasi Gaji Karyawan Perusahaan
# Nama : David Nasrulloh | 190441100060
# Fakultas : Teknik
# Prodi : Sistem Informasi
# *******************************************

import sys

def keluar():
    sys.exit()

def pindah(label):
    global nomor
    nomor = label


datalist = ["PT. JAYA KUSUMA", "Dir. Keuangan", "David Nasrulloh", "Anas Al Ayubi"]


def cetak():
    print()
    print()
    print()
    print("=============================================================")
    print("=================  Aplikasi Kalkulasi Gaji   ================")
    print("=============================================================")
    print("================== Hasil Akhir Perhitungan ==================")
    print("=============================================================")
    print("                   ***", datalist[0], "***")
    print()
    print("| Nama\t\t\t\t\t\t\t\t\t\t: ", nama)
    print("| NIP\t\t\t\t\t\t\t\t\t\t: ", nip)
    print("| Jabatan\t\t\t\t\t\t\t\t\t: ", jabatan)
    print()
    print()
    print("| Jumlah Bulan\t\t\t\t\t\t\t\t: ", jumbulan)
    print("| Gaji Pokok\t\t\t\t\t\t\t\t: Rp. ", hitunggapok)
    print("| Tunjangan Anak\t\t\t\t\t\t\t: Rp. ", hitunganak)
    print("| Tunjangan Transportasi\t\t\t\t\t: Rp. ", hitungjarak)
    print("| Lembur (", jumlem, ")\t\t\t\t\t\t\t\t: Rp. ", hitunglembur)
    print()
    print("| Gaji Kotor adalah\t\t\t\t\t\t\t: Rp. ", gajikotor)
    print()
    print("| Potongan Kehadiran dan potongan 5% ")
    print("| Cuti (", jumcuti, ")\t\t\t\t\t\t\t\t: Rp. ", hitungcuti)
    print("| Sakit (", jumsakit, ")\t\t\t\t\t\t\t\t: Rp. ", hitungsakit)
    print("| Ijin (", jumijin, ")\t\t\t\t\t\t\t\t: Rp. ", hitungijin)
    print("| T. Keterangan (", jumnoketerangan, ")\t\t\t\t\t\t: Rp. ", hitungnoketerangan)
    print("| Potongan 5% dari gaji kotor\t\t\t\t: Rp. ", hitungpersen)
    print()
    print("| Jumlah Semua potongan\t\t\t\t\t\t: Rp. ", potongan)
    print()
    print("\t\t\t\t\t\t\t\t\t\t\t==================")
    print("| Jumlah Gaji Bersih adalah\t\t\t\t\t: Rp. ", total)
    print()
    print()
    print("                      **", datalist[1], "**")
    print()
    print()
    if user == "davidutm" and password == "190441100060":
        print("                      **", datalist[2], "**")
    elif user == "anasutm" and password == "190441100044":
        print("                      **", datalist[3], "**")

def rumus():
    global anak, jumsakit, transportasi, cuti, jumbulan, potongan, hitungpersen, hitungcuti, sakit, hasilpotongankehadiran, hitungsakit, ijin, hitungijin, hitungnoketerangan, noketerangan, gapok, gajikotor, hitunglembur, hitunganak, persen, total, hitungjarak
    anak = 200000
    transportasi = 50000
    cuti = 10000
    sakit = 5000
    ijin = 7000
    noketerangan = 20000

    if jumcuti >= 0:
        hitungcuti = jumcuti * cuti

    if jumsakit >= 0:
        hitungsakit = jumsakit * sakit

    if jumijin >= 0:
        hitungijin = jumijin * ijin

    if jumnoketerangan >= 0:
        hitungnoketerangan = jumnoketerangan * noketerangan

    if jarakrumah >= 0:
        hitungjarak = jarakrumah * transportasi
        if jumbulan > 0:
            hitungjarak = (jarakrumah * jumbulan) * transportasi

    if jumanak >= 0:
        hitunganak = jumanak * anak
        if jumbulan > 0:
            hitunganak = (jumanak * jumbulan) * anak

    hasilpotongankehadiran = hitungijin + hitungcuti + hitungnoketerangan + hitungsakit
    hitunglembur = jumlem * lembur
    gajikotor = hitunggapok + hitunglembur + hitunganak + hitungjarak
    hitungpersen = ((gajikotor * 5) / 100) * jumbulan
    potongan = hasilpotongankehadiran + hitungpersen
    total = gajikotor - potongan

import os

def ulang():
    print()
    ulang = (input("Apakah anda ingin mengulang  lagi ? [y/n] "))
    if ulang == "y" or ulang == "Y":
        os.system('cls')
        pindah(0)

    elif ulang == "n" or ulang == "N":
        print()
        print("Terimakasih telah menggunakan Sistem Aplikasi Kalkulasi Gaji ini")
        keluar()

def kepastian():
    global keep_kepastian
    keep_kepastian = True
    while keep_kepastian:
        print("--------------------------------------------------------------------")
        print("Tekan ( t ) untuk tidak melanjutkan program dan keluar ")
        print("Tekan ( c ) untuk lanjut cetak ")
        #print("Tekan ( u ) untuk ulang proses input")
        try:
            kepastian = input("Masukkan Pilihan Selajutnya: ")
            if kepastian == "t" or kepastian == "T":
                print()
                print("Terimakasih telah menggunakan Sistem Aplikasi Kalkulasi Gaji ini")
                print("Run ulang untuk melakukan proses kalkulasi gaji kembali")
                keluar()
            elif kepastian == "c" or kepastian == "C":
                pindah(0)
                keep_kepastian = False
            elif kepastian != "t" or kepastian != "c" or kepastian != "T" or kepastian != "C":
                print()
                print("Mohon maaf, yang anda inputkan salah")
        except ValueError:
            print()
            print("Mohon maaf, Yang anda inputkan salah")

    #elif perbaikan == "u":
     #   pindah(0)

# Proses masuk
print("=============================================================")
print("======================  Halaman Log in  =====================")
print("=============================================================")
stop = False
while not stop:
    print()
    user = input("Masukkan Username\t\t\t: ")
    password = input("Masukkan Password\t\t\t: ")
    if user == "davidutm" and password == "190441100060":
        print()
        print("Selamat anda berhasil Log in")
        stop = True
    elif user == "anasutm" and password == "190441100044":
        print()
        print("Selamat anda berhasil Log in")
        stop = True
    else:
        print()
        print("Mohon maaf anda tidak bisa login")
        print("Silahkan Login Kembali")

nomor = 0
while True:
    if nomor == 0:
        print()
        print()
        print()
        print("=============================================================")
        print("=================  Aplikasi Kalkulasi Gaji   ================")
        print("=============================================================")
        print("===================== Proses Input Data =====================")
        print("=============================================================")
        nama = str(input("Masukkan nama\t\t\t\t\t\t\t\t: "))
        keep_gol =  True
        while keep_gol:
            try :
                print("------------------------------------------------------")
                print("Jenis pilihan golongan di perusahaan PT. Jaya Kusuma")
                print("     1. Direktur ")
                print("     2. Manager ")
                print("     3. Supervisor ")
                print("     4. Staf operator")
                print("     5. Staf karyawan ")
                print("------------------------------------------------------")
                golongan = int(input("Golongan\t\t\t\t\t\t\t\t\t: "))
                keep_gol = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_nip = True
        while keep_nip:
            try:
                nip = int(input("Masukkan NIP\t\t\t\t\t\t\t\t: "))
                keep_nip = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumbulan = True
        while keep_jumbulan:
            try:
                jumbulan = int(input("Masukkan Jumlah Bulan yang ingin dihitung\t: "))
                keep_jumbulan = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumcuti = True
        while keep_jumcuti:
            try:
                jumcuti = int(input("Masukkan jumlah cuti(hari)\t\t\t\t\t: "))
                keep_jumcuti = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumsakit = True
        while keep_jumsakit:
            try:
                jumsakit = int(input("Masukkan jumlah sakit(hari)\t\t\t\t\t: "))
                keep_jumsakit = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumijin = True
        while keep_jumijin:
            try:
                jumijin = int(input("Masukkan jumlah ijin(hari)\t\t\t\t\t: "))
                keep_jumijin = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumnoketerangan = True
        while keep_jumnoketerangan:
            try:
                jumnoketerangan = int(input("Masukkan jumlah T.Keterengan(hari)\t\t\t: "))
                keep_jumnoketerangan = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumlem = True
        while keep_jumlem:
            try:
                jumlem = int(input("Jumlah Lembur(jam)\t\t\t\t\t\t\t: "))
                keep_jumlem = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jarakrumah = True
        while keep_jarakrumah:
            try:
                jarakrumah = int(input("Masukkan Jarak rumah ke kantor(km)\t\t\t: "))
                keep_jarakrumah = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")
        keep_jumanak = True
        while keep_jumanak:
            try:
                jumanak = int(input("Jumlah Anak\t\t\t\t\t\t\t\t\t: "))
                keep_jumanak = False
            except ValueError:
                print("Maaf yang anda inputkan salah")
                print("Yang anda masukkan bukan tipe integer. Mohon ulangi kembali...")

        kepastian()

        if golongan == 1:
            pindah(1)
        elif golongan == 2:
            pindah(2)
        elif golongan == 3:
            pindah(3)
        elif golongan == 4:
            pindah(4)
        elif golongan == 5 :
            pindah(5)

    if nomor == 1:
        jabatan = "Direktur"
        gapok = 8000000
        if jumbulan > 0:
            hitunggapok = jumbulan * gapok
        lembur = 100000
        rumus()
        cetak()
        ulang()


    elif nomor == 2:
        jabatan = "Manajer"
        gapok = 6000000
        if jumbulan > 0:
            hitunggapok = jumbulan * gapok
        lembur = 80000
        rumus()
        cetak()
        ulang()

    elif nomor == 3:
        jabatan = "Supervisor"
        gapok = 4000000
        if jumbulan > 0:
            hitunggapok = jumbulan * gapok
        lembur = 60000
        rumus()
        cetak()
        ulang()

    elif nomor == 4:
        jabatan = "Staff Operator"
        gapok = 2000000
        if jumbulan > 0:
            hitunggapok = jumbulan * gapok
        lembur = 40000
        rumus()
        cetak()
        ulang()
    elif nomor == 5:
        jabatan = "Staf Karyawan"
        gapok = 1500000
        if jumbulan > 0:
            hitunggapok = jumbulan * gapok
        lembur = 30000
        rumus()
        cetak()
        ulang()
    else:
        ulang()


