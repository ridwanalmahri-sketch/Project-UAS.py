def main():
    proses = "MahasiswaProcess"()
    view = "MahasiswaView"()

    while True:
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            proses.tambah_mahasiswa()
        elif pilihan == "2":
            view.tampilkan_tabel(proses.get_data())
        elif pilihan == "3":
            break
