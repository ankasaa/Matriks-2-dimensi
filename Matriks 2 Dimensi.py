# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lXe3yeZd9p6rVibBY-AnfGNj8Uq16NYS
"""



#I GEDE OKTA ANDIKA YASA
#***1010***
#INFORMATIKA
#KELAS L

import numpy as np
matriks = None
matriksB = None
matriksC = None

while True:
    print("\nMenu:")
    print("1. Membuat matriks A")
    print("2. Membuat Matriks B")
    print("3. Mengisi matriks")
    print("4. Mencetak isi matriks")
    print("5. Mengganti nilai matriks")
    print("6. Perkalian Matriks A X B")
    print("7. Penjumlahan Matriks A + B")
    print("8. Pengurangan Matriks A - B")
    print("0. Keluar")

    print("-----------------------------------------")
    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        baris = int(input("Masukkan jumlah baris untuk Matriks A: "))
        kolom = int(input("Masukkan jumlah kolom untuk Matriks A: "))
        matriks = np.zeros((baris, kolom), dtype=int)
        print("-----------------------------------------")
        print(f"Matriks A {baris}x{kolom} berhasil dibuat.")
    elif pilihan == "2":
        baris = int(input("Masukkan jumlah baris untuk Matriks B: "))
        kolom = int(input("Masukkan jumlah kolom untuk Matriks B: "))
        matriksB = np.zeros((baris, kolom), dtype=int)
        print("-----------------------------------------")
        print(f"Matriks B {baris}x{kolom} berhasil dibuat.")

    elif pilihan == "3":
        print("Pilih matriks yang ingin diisi:")
        print("1. Matriks A")
        print("2. Matriks B")
        pilih_matriks = input("Pilih matriks (1/2): ")

        if pilih_matriks == "1" and matriks is not None:
            print("Masukkan nilai untuk setiap elemen Matriks A:")
            for i in range(matriks.shape[0]):
                for j in range(matriks.shape[1]):
                    matriks[i, j] = int(input(f"Masukkan nilai untuk posisi [{i}][{j}]: "))
        elif pilih_matriks == "2" and matriksB is not None:
            print("Masukkan nilai untuk setiap elemen Matriks B:")
            for i in range(matriksB.shape[0]):
                for j in range(matriksB.shape[1]):
                    matriksB[i, j] = int(input(f"Masukkan nilai untuk posisi [{i}][{j}]: "))
        else:
            print("Matriks belum dibuat! Pilih menu 1 atau 2 terlebih dahulu.")

    elif pilihan == "4":
        print("Pilih matriks yang ingin dicetak:")
        print("1. Matriks A")
        print("2. Matriks B")
        pilih_matriks = input("Pilih matriks (1/2): ")

        if pilih_matriks == "1" and matriks is not None:
            print("Isi Matriks A:")
            print(matriks)
        elif pilih_matriks == "2" and matriksB is not None:
            print("Isi Matriks B:")
            print(matriksB)
        else:
            print("Matriks belum dibuat atau pilihan tidak valid.")

    elif pilihan == "5":
        print("Pilih matriks yang ingin diganti nilainya:")
        print("1. Matriks A")
        print("2. Matriks B")
        pilih_matriks = input("Pilih matriks (1/2): ")

        if pilih_matriks == "1" and matriks is not None:
            baris = int(input("Masukkan baris yang ingin diubah: "))
            kolom = int(input("Masukkan kolom yang ingin diubah: "))
            if 0 <= baris < matriks.shape[0] and 0 <= kolom < matriks.shape[1]:
                nilai_baru = int(input("Masukkan nilai baru: "))
                matriks[baris, kolom] = nilai_baru
                print(f"Nilai pada posisi [{baris}][{kolom}] di Matriks A berhasil diubah.")
            else:
                print("Indeks tidak valid!")
        elif pilih_matriks == "2" and matriksB is not None:
            baris = int(input("Masukkan baris yang ingin diubah: "))
            kolom = int(input("Masukkan kolom yang ingin diubah: "))
            if 0 <= baris < matriksB.shape[0] and 0 <= kolom < matriksB.shape[1]:
                nilai_baru = int(input("Masukkan nilai baru: "))
                matriksB[baris, kolom] = nilai_baru
                print(f"Nilai pada posisi [{baris}][{kolom}] di Matriks B berhasil diubah.")
            else:
                print("Indeks tidak valid!")
        else:
            print("Matriks belum dibuat atau pilihan tidak valid.")

    elif pilihan == "6":
        # Perkalian matriks A x B
        if matriks is not None and matriksB is not None:
            if matriks.shape[1] == matriksB.shape[0]:
                matriksC = np.dot(matriks, matriksB)  # Perkalian matriks
                print("Hasil perkalian matriks A x B disimpan di matriks C:")
                print(matriksC)
            else:
                print("Perkalian tidak valid! Jumlah kolom A harus sama dengan jumlah baris B.")
        else:
            print("Matriks A atau B belum dibuat!")

    elif pilihan =="7":
      # Penjumlahan Matriks A + B
        if matriks is not None and matriksB is not None:
            if matriks.shape[1] == matriksB.shape[0]:
              matriksC = matriks + matriksB
              print("Hasil penjumlahan matriks A + B disimpan di matriks C:")
              print(matriksC)
            else:
              print("Penjumlahan tidak valid! Jumlah kolom A harus sama dengan jumlah baris B.")
        else:
          print("Matriks A atau B belum dibuat!")

    elif pilihan =="8":
      # Pengurangan Matriks A - B
        if matriks is not None and matriksB is not None:
            if matriks.shape[1] == matriksB.shape[0]:
              matriksC = matriks - matriksB
              print("Hasil pengurangan matriks A - B disimpan di matriks C:")
              print(matriksC)
            else:
              print("Pengurangan tidak valid! Jumlah kolom A harus sama dengan jumlah baris B.")

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu dari 1 sampai 6.")
