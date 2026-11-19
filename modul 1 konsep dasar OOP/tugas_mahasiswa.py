class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan diri
    def perkenalan_diri(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}, jurusan {self.jurusan} di {Mahasiswa.universitas}."

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}."

    # Method predikat kelulusan berdasarkan ketentuan IPK
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Memenuhi Syarat Kelulusan"

# Instansiasi 3 object mahasiswa dengan data berbeda
mhs1 = Mahasiswa("Padila", "202512053", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Budi Santoso", "202512054", "Teknik Informatika", 3.20)
mhs3 = Mahasiswa("Siti Aminah", "202512055", "Teknik Informatika", 2.65)

# Demonstrasi semua method untuk mhs1
print(mhs1.perkenalan_diri())
print(f"IPK Awal: {mhs1.ipk} | Predikat: {mhs1.predikat_kelulusan()}")
print(mhs1.update_ipk(3.85))
print(f"Predikat Terbaru: {mhs1.predikat_kelulusan()}")
print("-" * 50)

# Demonstrasi mhs2 dan mhs3
print(mhs2.perkenalan_diri())
print(f"IPK: {mhs2.ipk} | Predikat: {mhs2.predikat_kelulusan()}")
print("-" * 50)
print(mhs3.perkenalan_diri())
print(f"IPK: {mhs3.ipk} | Predikat: {mhs3.predikat_kelulusan()}")