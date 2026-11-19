class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengampu mata kuliah {mata_kuliah}."

# Instansiasi 2 object dosen
dosen1 = Dosen("Dr. Rinnandya Chandra H", "0686177267")
dosen2 = Dosen("M. Abadi Nugroho.", "0686177268")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Algoritma dan Struktur Data"))
print(dosen2.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))