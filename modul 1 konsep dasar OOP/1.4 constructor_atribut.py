class Kendaraan:
    # Class attribute (berbagi nilai untuk semua object)
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        # Instance attributes (unik untuk setiap object)
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk}, Warna: {self.warna}, Tahun: {self.tahun}"

# Instansiasi object
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda Beat", "Putih", 2023)

print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())
print(f"Jenis Bahan Bakar (Class Attribute): {Kendaraan.bahan_bakar}")