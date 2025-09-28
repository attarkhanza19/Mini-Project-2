# Sistem Air PDAM Sederhana v2

tarif_per_m3 = 2500
pelanggan_dict = {
    1: {"nama": "Attar", "pemakaian": 100},
    2: {"nama": "Doni", "pemakaian": 15},
    3: {"nama": "Bastian", "pemakaian": 10}
}

def hitung_tagihan(pemakaian):
    return pemakaian * tarif_per_m3

def tampilkan_data():
    try:
        if not pelanggan_dict:
            print("\nData pelanggan kosong.\n")
            return
        print("\n========== Daftar Tagihan Air ==========")
        for id, data in pelanggan_dict.items():
            print(f"{id}. {data['nama']} | Pemakaian: {data['pemakaian']} m3 | Tagihan: Rp {hitung_tagihan(data['pemakaian'])}")
        print("========================================\n")
    except KeyboardInterrupt:
        print("Jangan Tekan CTRL C")

def tambah_data():
    try:
        nama = input("Masukkan nama pelanggan: ").strip()
        pemakaian = float(input("Masukkan pemakaian air (m3): "))
        if pemakaian < 0:
            raise ValueError
        new_id = max(pelanggan_dict.keys(), default=0) + 1
        pelanggan_dict[new_id] = {"nama": nama, "pemakaian": pemakaian}
        print(f"Data {nama} berhasil ditambahkan.")
    except ValueError:
        print("Error : Masukkan angka dan angka tidak boleh negatif")
    except KeyboardInterrupt:
        print("Jangan Tekan CTRL C")

def ubah_data():
    tampilkan_data()
    try:
        pilih = int(input("Masukkan ID pelanggan yang ingin diubah: "))
        if pilih not in pelanggan_dict:
            raise KeyError("ID tidak ditemukan.")
        nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ").strip()
        pemakaian = input("Masukkan pemakaian baru (kosongkan jika tidak diubah): ").strip()
        
        if nama:
            pelanggan_dict[pilih]["nama"] = nama
        if pemakaian:
            pemakaian_baru = float(pemakaian)
            if pemakaian_baru < 0:
                raise ValueError
            pelanggan_dict[pilih]["pemakaian"] = pemakaian_baru
        print("Data berhasil diupdate.")
    except KeyError:
        print("Error : ID Tidak ditemukan")
    except ValueError:
        print("Error : Masukkan angka dan angka tidak boleh negatif")
    except KeyboardInterrupt:
        print("Error : Jangan tekat CTRL C")
    

def hapus_data():
    tampilkan_data()
    try:
        pilih = int(input("Masukkan ID pelanggan yang ingin dihapus: "))
        if pilih not in pelanggan_dict:
            raise KeyError("ID tidak ditemukan.")
        data = pelanggan_dict.pop(pilih)
        print(f"Data {data['nama']} berhasil dihapus.")
    except KeyError:
        print("Error : ID Tidak ditemukan")
    except ValueError:
        print("Error : Pilih nomor pada ID")
    except KeyboardInterrupt:
        print("Error : Jangan tekat CTRL C")

def menu_admin():
    while True:
        print("""
========== Menu Admin ==========
1. Tambah Data Pemakaian
2. Lihat Data
3. Ubah Data
4. Hapus Data
5. Keluar
""")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Keluar dari menu admin.\n")
            break
        else:
            print("Pilihan tidak valid.")

def menu_user():
    while True:
        print("""
========== Menu User ==========
1. Lihat Data
2. Keluar
""")
        pilihan = input("Pilih menu (1-2): ").strip()
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            print("Keluar dari menu user.\n")
            break
        else:
            print("Pilihan tidak valid.")

#Program Utama
while True:
    print("""
========== Sistem Air PDAM ==========
Pilih Role:
1. Admin
2. User
3. Keluar
""")
    role = input("Masukkan pilihan (1-3): ").strip()
    if role == "1":
        menu_admin()
    elif role == "2":
        menu_user()
    elif role == "3":
        print("Program ditutup. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid.")
