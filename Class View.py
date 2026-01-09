class MahasiswaView:
    def tampilkan_tabel(self, data):
        print("+----+----------------+-------+")
        print("| No | Nama           | Nilai |")
        print("+----+----------------+-------+")

        for i, mhs in enumerate(data, start=1):
            print(f"| {i:<2} | {mhs.nama:<14} | {mhs.nilai:<5} |")

        print("+----+----------------+-------+")
