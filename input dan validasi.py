def tambah_mahasiswa(self):
    try:
        nama = input("Masukkan nama mahasiswa: ").strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong")

        nilai = float(input("Masukkan nilai mahasiswa (0-100): "))
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 dan 100")

        mahasiswa = "Mahasiswa"(nama, nilai)
        self.data_mahasiswa.append(mahasiswa)

        print("Data berhasil ditambahkan")

    except ValueError as error:
        print(f"Terjadi kesalahan: {error}")
